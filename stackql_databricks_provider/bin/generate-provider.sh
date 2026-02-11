#!/usr/bin/env bash

# Exit on error
set -e

# Get the script directory for relative paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

# Default values
PROVIDER_NAME=""
INPUT_DIR=""
OUTPUT_DIR=""
CONFIG_PATH=""
SERVERS=""
PROVIDER_CONFIG=""
SKIP_FILES=""
OVERWRITE=false
VERBOSE=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --provider-name)
      PROVIDER_NAME="$2"
      shift 2
      ;;
    --input-dir)
      INPUT_DIR="$2"
      shift 2
      ;;
    --output-dir)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --config-path)
      CONFIG_PATH="$2"
      shift 2
      ;;
    --servers)
      SERVERS="$2"
      shift 2
      ;;
    --provider-config)
      PROVIDER_CONFIG="$2"
      shift 2
      ;;
    --skip-files)
      SKIP_FILES="$2"
      shift 2
      ;;
    --overwrite)
      OVERWRITE=true
      shift
      ;;
    --verbose)
      VERBOSE=true
      shift
      ;;
    --help)
      echo "Usage: generate-provider.sh [OPTIONS]"
      echo ""
      echo "Options:"
      echo "  --provider-name NAME        Provider name/ID (required)"
      echo "  --input-dir DIR             Input directory containing split OpenAPI files (required)"
      echo "  --output-dir DIR            Output directory for provider (required)"
      echo "  --config-path PATH          Path to CSV mapping file (required)"
      echo "  --servers JSON              JSON string with servers configuration"
      echo "  --provider-config JSON      JSON string with provider configuration"
      echo "  --skip-files LIST           Comma-separated list of files to skip"
      echo "  --overwrite                 Overwrite existing files"
      echo "  --verbose                   Enable verbose output"
      echo "  --help                      Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      echo "Use --help for usage information"
      exit 1
      ;;
  esac
done

# Check required arguments
if [ -z "$PROVIDER_NAME" ] || [ -z "$INPUT_DIR" ] || [ -z "$OUTPUT_DIR" ] || [ -z "$CONFIG_PATH" ]; then
  echo "Error: Missing required arguments"
  echo "Use --help for usage information"
  exit 1
fi

echo "🔧 Generating StackQL provider extensions..."
echo "Provider: $PROVIDER_NAME"
echo "Input Directory: $INPUT_DIR"
echo "Output Directory: $OUTPUT_DIR"
echo "Config Path: $CONFIG_PATH"

# Build command arguments
ARGS=("--provider-name" "$PROVIDER_NAME" "--input-dir" "$INPUT_DIR" "--output-dir" "$OUTPUT_DIR" "--config-path" "$CONFIG_PATH")

if [ -n "$SERVERS" ]; then
  ARGS+=("--servers" "$SERVERS")
  echo "Custom servers configuration provided"
fi

if [ -n "$PROVIDER_CONFIG" ]; then
  ARGS+=("--provider-config" "$PROVIDER_CONFIG")
  echo "Custom provider configuration provided"
fi

if [ -n "$SKIP_FILES" ]; then
  ARGS+=("--skip-files" "$SKIP_FILES")
  echo "Skipping files: $SKIP_FILES"
fi

if [ "$OVERWRITE" = true ]; then
  ARGS+=("--overwrite")
  echo "Overwrite: Yes"
fi

if [ "$VERBOSE" = true ]; then
  ARGS+=("--verbose")
  echo "Verbose: Yes"
fi

# Run the Node.js script with arguments
node --experimental-modules "$SCRIPT_DIR/generate-provider.mjs" "${ARGS[@]}"

# Check if command succeeded
if [ $? -ne 0 ]; then
    echo "❌ Provider generation failed"
    exit 1
fi

echo "✅ Provider generated successfully at: $OUTPUT_DIR"