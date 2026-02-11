#!/bin/bash

# Get command line arguments
PORT="5444"

while [[ $# -gt 0 ]]; do
  case $1 in
    --port)
      PORT="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: stop-server.sh [--port PORT]"
      exit 1
      ;;
  esac
done

# Find the process ID of the StackQL server on the specified port
PID=$(pgrep -f "stackql.*--pgsrv.port=${PORT}")

if [ -z "$PID" ]; then
  echo "No stackql server found running on port ${PORT}."
else
  echo "Stopping stackql server on port ${PORT} (PID: $PID)..."
  kill $PID
  
  # Check if server stopped
  sleep 2
  if ps -p $PID > /dev/null; then
    echo "Server did not stop gracefully, attempting force kill..."
    kill -9 $PID
    
    sleep 1
    if ps -p $PID > /dev/null; then
      echo "Failed to stop server. Please check manually with 'ps -ef | grep stackql'"
      exit 1
    fi
  fi
  
  echo "StackQL server stopped successfully."
fi