# Running commands in sandboxes

Databricks Sandbox lets you run untrusted code in an isolated environment. For
sandbox lifecycle operations (create, delete, etc.), see the
[`WorkspaceClient.sandbox` reference](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/sandbox/sandbox.html).

This guide shows how to run a command in a sandbox, read its output as it is
being produced, send it input, and get its exit code.

## Prerequisites

Install the SDK with the `sandbox` extra:

```bash
pip install 'databricks-sdk[sandbox]'
```

Each method takes the sandbox's resource name, `sandboxes/{sandbox_id}`. This
value corresponds to the `name` field of the `Sandbox` object returned by
`create_sandbox`, `get_sandbox`, or `list_sandboxes` (a bare `{sandbox_id}` is
also accepted). If the sandbox is stopped, running a command starts it first.

## Run a command

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

## Read output as it is produced

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

## Send input

Write to `stdin`, then call `close()` to signal end of input:

```python
process = w.sandbox.execute_command(name, "/bin/cat")
process.stdin.write("hello from stdin\n")
process.stdin.close()
print(process.stdout.read())  # hello from stdin
```

## Choose where output goes

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

## Stop waiting on a command

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

## Reconnect to a command

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
