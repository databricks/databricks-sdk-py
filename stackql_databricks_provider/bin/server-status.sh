#!/bin/bash

# Default port
PORT="5444"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --port)
      PORT="$2"
      shift 2
      ;;
    --help)
      echo "Usage: server-status.sh [--port PORT]"
      echo "Check status of StackQL server"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: server-status.sh [--port PORT]"
      exit 1
      ;;
  esac
done

# Search for stackql process running on specified port
stackql_process=$(ps -ef | grep -E "[s]tackql.*--pgsrv.port=${PORT}")

# Check if the process is running
if [ -z "$stackql_process" ]; then
  echo "StackQL server is not running on port ${PORT}."
  exit 1
else
  # Extract PID using awk
  pid=$(echo "$stackql_process" | awk '{print $2}')
  
  # Get process start time
  if [ "$(uname)" == "Darwin" ]; then
    # macOS
    start_time=$(ps -p $pid -o lstart= 2>/dev/null)
  else
    # Linux
    start_time=$(ps -p $pid -o lstart= 2>/dev/null)
  fi
  
  # Get registry path if possible
  registry_info=$(echo "$stackql_process" | grep -o -E "registry=\{[^}]+\}")
  
  echo "StackQL server is running on port ${PORT} (PID: ${pid})"
  echo "Started: ${start_time}"
  
  if [ ! -z "$registry_info" ]; then
    echo "Registry: ${registry_info#*=}"
  fi
  
  # Check if we can connect to the server
  echo "Testing connection..."
  if command -v psql &> /dev/null; then
    if PGPASSWORD=stackql psql -h localhost -p ${PORT} -U stackql -d stackql -c "SELECT 1 as test" &> /dev/null; then
      echo "✅ Server is accepting connections"
    else
      echo "❌ Could not connect to server"
    fi
  else
    echo "Note: Install psql client to test connection"
  fi
  
  # Check server log
  BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
  LOG_FILE="${BASE_DIR}/stackql-server.log"
  
  if [ -f "$LOG_FILE" ]; then
    echo "Recent log entries:"
    tail -n 5 "$LOG_FILE"
  fi
  
  exit 0
fi