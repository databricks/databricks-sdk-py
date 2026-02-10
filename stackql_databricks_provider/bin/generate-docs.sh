#!/usr/bin/env bash

# Exit on error
set -e

# Get the script directory for relative paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --provider-name)
      PROVIDER_NAME="$2"
      shift 2
      ;;
    --provider-dir)
      PROVIDER_DIR="$2"
      shift 2
      ;;
    --output-dir)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --provider-data-dir)
      PROVIDER_DATA_DIR="$2"
      shift 2
      ;;
    --help)
      echo "Usage: generate-docs.sh [OPTIONS]"
      echo ""
      echo "Options:"
      echo "  --provider-name NAME      Provider name (default: snowflake)"
      echo "  --provider-dir DIR        Provider directory path (default: $PROVIDER_DIR)"
      echo "  --output-dir DIR          Output directory for docs (default: $OUTPUT_DIR)"
      echo "  --provider-data-dir DIR   Provider data directory (default: $PROVIDER_DATA_DIR)"
      echo "  --help                    Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      echo "Use --help for usage information"
      exit 1
      ;;
  esac
done

echo "📚 Generating documentation using @stackql/provider-utils..."

# Run the Node.js script with arguments
node --experimental-modules "$SCRIPT_DIR/generate-docs.mjs" \
  --provider-name "$PROVIDER_NAME" \
  --provider-dir "$PROVIDER_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --provider-data-dir "$PROVIDER_DATA_DIR"

# Check if command succeeded
if [ $? -ne 0 ]; then
    echo "❌ Documentation generation failed"
    exit 1
fi

echo "✅ Documentation generated successfully"