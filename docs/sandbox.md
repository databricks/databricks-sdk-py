# Sandboxes

Databricks Sandbox lets you run untrusted code in an isolated environment. For
sandbox lifecycle operations (create, delete, etc.), see the
[`WorkspaceClient.sandbox` reference](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sandbox/sandbox.html).

## Commands

### Prerequisites

Install the SDK with the `sandbox` extra:

```bash
pip install 'databricks-sdk[sandbox]'
```

Each method takes the sandbox's resource name, `sandboxes/{sandbox_id}`. This
value corresponds to the `name` field of the `Sandbox` object returned by
`create_sandbox`, `get_sandbox`, or `list_sandboxes` (a bare `{sandbox_id}` is
also accepted). If the sandbox is stopped, running a command starts it first.

### Run a command

`execute_command` starts a command and returns a `CommandProcess`. You can read
its standard output and standard error through `stdout` and `stderr`, and use
`wait()` to get the exit code.

Commands run without a shell. Wrap shell syntax in `/bin/bash -c`.

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
name = "sandboxes/my-sandbox"

process = w.sandbox.execute_command(
    name, "/bin/bash", args=["-c", "echo hello; echo oops 1>&2; exit 3"]
)
print(process.stdout.read())  # hello
print(process.stderr.read())  # oops
print(process.wait())  # 3
```

`read()` waits for the command to exit and returns all of the stream's output;
`read(size)` returns up to `size` characters (or bytes). Output is `str` by
default; pass `text=False` to `execute_command` to get `bytes`.

### Read output as it is produced

Iterate `stdout` or `stderr` to read it line by line as the command writes it,
or call `readline()` for a single line:

```python
script = "for i in 1 2 3; do echo step $i; sleep 1; done"
process = w.sandbox.execute_command(name, "/bin/bash", args=["-c", script])
for line in process.stdout:
    print(line, end="")
```

For output that arrives without a trailing newline (a prompt, a progress bar),
use `read1()` to receive output the instant it is written, without waiting for a
full line.

### Send input

Write to `stdin`, then call `close()` to signal end of input:

```python
process = w.sandbox.execute_command(name, "/bin/cat")
process.stdin.write("hello from stdin\n")
process.stdin.close()
print(process.stdout.read())  # hello from stdin
```

### Choose where output goes

The SDK keeps each stream's output in memory until you read it, so read
long-running output as it is produced rather than buffering it all; if you don't
need a stream, discard it with `StreamMode.DEVNULL`. On the sandbox side, only
the most recent output per command is retained (up to roughly 16 MB), so a
reader that stalls and resumes much later may miss the earliest output. To read
stdout and stderr together, send stderr to stdout with `StreamMode.STDOUT`:

```python
from databricks.sdk.mixins.sandbox import StreamMode

process = w.sandbox.execute_command(
    name,
    "/bin/bash",
    args=["-c", "echo out; echo err 1>&2"],
    stderr=StreamMode.STDOUT,
)
print(process.stdout.read())  # out and err

process = w.sandbox.execute_command(
    name, "/bin/bash", args=["-c", "echo noisy"], stdout=StreamMode.DEVNULL
)
print(process.wait())  # 0
```

### Stop waiting on a command

`wait(timeout=)` and `read(timeout=)` raise `TimeoutError` if the command does
not finish in time. Call `close()` to stop receiving its output and release the
connection; the handle is also a context manager that closes on exit. Closing
is client-side only and does not stop the command running in the sandbox; to
stop the process itself, run `kill <pid>` as a second command using
`process.pid`.

```python
with w.sandbox.execute_command(name, "/bin/sleep", args=["60"]) as process:
    try:
        print(process.stdout.read(timeout=5))
    except TimeoutError:
        print("still running; giving up")
# leaving the block closes the handle
```

### Reconnect to a command

If the connection is interrupted, the SDK reconnects and resumes the output
where it left off.

To get a new handle to a command, for example from another process, pass its
`command_id` to `connect_command`. The new handle replays the command's output
from the beginning:

```python
process = w.sandbox.execute_command(name, "/bin/echo", args=["saved"])
process.wait()

again = w.sandbox.connect_command(name, process.command_id)
print(again.stdout.read())  # saved
print(again.wait())  # 0
```

## Files

Pass the sandbox resource name (`sandboxes/{sandbox_id}`) to each method on `w.sandbox`:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
sandbox_name = "sandboxes/my-sandbox"

w.sandbox.create_directory(sandbox_name, "/home/sandbox/data")
w.sandbox.rename_path(sandbox_name, "/home/sandbox/input.csv", "/home/sandbox/data/input.csv")
info = w.sandbox.get_metadata(sandbox_name, "/home/sandbox/data/input.csv").file
for child in w.sandbox.list_directory_contents(sandbox_name, "/home/sandbox/data"):
    print(child.path, child.size)
w.sandbox.delete_path(sandbox_name, "/home/sandbox/data/input.csv")
```

- `create_directory` creates missing parents and succeeds if the directory exists. With `parents=False`, the parent must exist and the destination must be absent.
- `rename_path` moves to the exact destination path. It fails if the destination exists or the move crosses filesystems.
- `delete_path` removes files, symlinks, and empty directories. Use `recursive=True` for nonempty directories. Deleting a missing path succeeds.
- `get_metadata` describes the final symlink itself. The response's `file` field contains the metadata; `modify_time` preserves nanosecond precision.
- `list_directory_contents` includes dotfiles and fetches pages as you iterate. Concurrent directory changes can affect the results.

Uploads and downloads stream bytes:

```python
with open("report.bin", "rb") as source:
    w.sandbox.upload_file(parent=sandbox_name, path="/home/sandbox/report.bin", contents=source)

download = w.sandbox.download_file(parent=sandbox_name, path="/home/sandbox/report.bin")
with download.contents as source, open("report-copy.bin", "wb") as destination:
    for chunk in iter(lambda: source.read(1024 * 1024), b""):
        destination.write(chunk)
```

Uploads atomically replace the destination file. The parent directory must exist; `upload_file` has no `overwrite` option.

`download_file` returns a `DownloadFileResponse` with a readable `contents` stream and HTTP metadata, including `content_length`, `content_type`, `etag`, and `last_modified`. Pass `byte_range="bytes=0-1023"` for a byte range and `if_range=etag` to require a matching file version. A mismatch returns the full file; an unsatisfiable range raises an SDK error. Close the contents stream after use.

API and transport failures raise standard SDK exceptions.

## Port forwarding

`w.sandbox.port_forward` lets you open an app running in a sandbox, such as a web
server, a notebook server, or a dev server, from your machine. It forwards a port
on `127.0.0.1` to a port in the sandbox through your workspace, so the app doesn't
need a public address.

### Forward a port

This example starts a web server in the sandbox and fetches a page from it:

```python
import urllib.request

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
name = "sandboxes/my-sandbox"

server = w.sandbox.execute_command(
    name, "python3", args=["-m", "http.server", "10080", "--bind", "0.0.0.0"]
)
# Wait until the server accepts connections.
w.sandbox.execute_command(
    name, "/bin/bash", args=["-c", "until ss -ltn | grep -q ':10080 '; do sleep 0.2; done"]
).wait()

with w.sandbox.port_forward(name, 10080) as forward:
    with urllib.request.urlopen(f"{forward.url}/") as response:
        print(response.status)  # 200
        print(response.read().decode()[:15])  # <!DOCTYPE HTML>

w.sandbox.execute_command(name, "/bin/kill", args=[str(server.pid)]).wait()
server.close()
```

`forward.url` is `http://127.0.0.1:<local_port>`. Any HTTP client, or a browser
on the same machine, can use it while the forward is open. The forward stays
open until you call `close()` or leave the `with` block. It uses a free local
port unless you pass `local_port=`.

### Requirements and limits

- The app must listen on `0.0.0.0` inside the sandbox, not only on `127.0.0.1`.
- You can forward ports 10000-65535, except 10101, 18767, and 19090.
- HTTP/1.1 and WebSocket traffic is supported. HTTP/2 and other protocols, such
  as database connections, are not.
- Requests are sent with your workspace credentials. An `Authorization` header
  that your client sets doesn't reach the app, so an app that expects a token in
  that header needs another way to sign in, such as a token in the URL.
