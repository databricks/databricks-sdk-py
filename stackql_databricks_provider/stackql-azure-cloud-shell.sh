#!/bin/sh

show_usage() {
    echo "Script to run StackQL in Azure Cloud Shell"
    echo     
    echo "Usage:"
    echo "  ./stackql-azure-cloud-shell.sh [shell | exec] [flags]"
    echo
    echo "  Command (optional):"
    echo "      'shell' (default) enters the StackQL command shell to execute queries interactively."
    echo "      'exec' is used to execute StackQL queries or files to provide batch outputs"
    echo "          (such as CSV or JSON output files). If not specified, 'shell' is assumed."
    echo
    echo "  Flags:"
    echo "      StackQL args are optional global flags, documented at https://stackql.io/docs/command-line-usage/global-flags"
    echo
    echo "  Examples:"
    echo "      # Launch the StackQL shell using interactive authentication (default in Azure)"
    echo "      sh stackql-azure-cloud-shell.sh"
    echo
    echo "      # Execute a query from a file, writing the output to a CSV file with interactive authentication"    
    echo "      sh stackql-azure-cloud-shell.sh exec --infile /path/to/query.sql --output csv --outfile /path/to/output.csv"
    echo
}

pull_azure_docs() {
    echo "Pulling latest Azure provider (azure)..."
    ./stackql exec "REGISTRY PULL azure"
    # echo "Pulling latest Azure Extras provider (azure_extras)..."
    # ./stackql exec "REGISTRY PULL azure_extras"
    # echo "Pulling latest Azure ISV provider (azure_isv)..."
    # ./stackql exec "REGISTRY PULL azure_isv"
    # echo "Pulling latest Azure Stack provider (azure_stack)..."
    # ./stackql exec "REGISTRY PULL azure_stack"
}

CMD="shell" # Default to 'shell' command
FLAGS=""

# Parse command line arguments
while [ $# -gt 0 ]; do
    case "$1" in
        shell|exec)
            CMD="$1"
            shift # Move past the command
            ;;
        *)
            # Check if the argument contains spaces
            if echo "$1" | grep -q " "; then
                # Argument contains spaces, wrap it in quotes
                FLAGS="$FLAGS \"$1\""
            else
                # Argument does not contain spaces, add as is
                FLAGS="$FLAGS $1"
            fi
            shift # Move past each flag
            ;;
    esac
done

# Execute the StackQL command
if [ "$CMD" = "shell" ]; then
    pull_azure_docs
    echo "Entering StackQL shell..."
    eval "./stackql shell $FLAGS"
elif [ "$CMD" = "exec" ]; then
    pull_azure_docs
    echo "Executing StackQL query..."
    eval "./stackql exec $FLAGS"
else
    show_usage
    echo
    echo "Error: invalid command ($CMD)"    
    exit 1
fi
