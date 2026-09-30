"""Committed gRPC stubs for the Sandbox command-execution service.

sandbox_service_pb2 / sandbox_service_pb2_grpc are generated from the shared
client proto (kept out of this package) at
compute-fabric/sandbox-sdk/proto/databricks/sandbox/sandbox_service.proto, a
dependency-stripped copy of
compute-fabric/sandbox-daemon/proto/sandbox_service.proto. The mixin uses only the
streaming RPCs (ExecuteCommand, AttachCommand, StreamInput); the stub also carries
the unary ListCommands, which the mixin does not use. Stubs are committed, not
built: the daemon proto pulls in internal imports that cannot ship publicly.

SDK codegen can't emit streaming clients yet. TODO(XTA-19715): migrate the mixin to
native streaming codegen and drop this package.

Regenerate after the shared proto changes, with a grpcio-tools whose bundled protoc
matches the pinned protobuf major (the sandbox extra in pyproject.toml). Stage the
proto at this package's path so the module path stays databricks.sdk._sandbox_grpc:

    root=$(mktemp -d)
    mkdir -p "$root/databricks/sdk/_sandbox_grpc"
    cp <universe>/compute-fabric/sandbox-sdk/proto/databricks/sandbox/sandbox_service.proto \\
        "$root/databricks/sdk/_sandbox_grpc/sandbox_service.proto"
    python -m grpc_tools.protoc -I "$root" \\
        --python_out="$root" --grpc_python_out="$root" \\
        databricks/sdk/_sandbox_grpc/sandbox_service.proto
    cp "$root"/databricks/sdk/_sandbox_grpc/sandbox_service_pb2*.py \\
        databricks/sdk/_sandbox_grpc/
"""
