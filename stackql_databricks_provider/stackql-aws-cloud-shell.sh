#!/bin/sh

show_usage() {
    echo "Script to run StackQL in AWS Cloud Shell"
    echo     
    echo "Usage:"
    echo "  ./stackql-aws-cloud-shell.sh [--role-arn ARN] [shell | exec] [flags]"
    echo
    echo "  --role-arn (optional)" 
    echo "      If supplied, the program will assume the role specified;"
    echo "      if not, then the current user context in cloud shell will be used."
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
    echo "      # Launch the StackQL shell using the current user context"
    echo "      sh stackql-aws-cloud-shell.sh"
    echo
    echo "      # Assume a role and execute a query from a file, writing the output to a CSV file"    
    echo "      sh stackql-aws-cloud-shell.sh --role-arn arn:aws:iam::824532806693:role/SecurityReviewerRole exec --infile /path/to/query.sql --output csv --outfile /path/to/output.csv"
    echo
}

pull_aws_docs() {
    echo "Pulling latest AWS provider (aws)..."
    ./stackql exec "REGISTRY PULL aws"
}

fetch_and_export_aws_creds() {
    if [ -z "$AWS_CONTAINER_AUTHORIZATION_TOKEN" ] || [ -z "$AWS_CONTAINER_CREDENTIALS_FULL_URI" ]; then
        echo "Error: AWS_CONTAINER_AUTHORIZATION_TOKEN or AWS_CONTAINER_CREDENTIALS_FULL_URI environment variable not set. If you are not running in AWS Cloud Shell, please provide a role ARN."
        exit 1
    fi
    
    creds=$(curl -s -H "Authorization: $AWS_CONTAINER_AUTHORIZATION_TOKEN" "$AWS_CONTAINER_CREDENTIALS_FULL_URI")
    if [ -z "$creds" ]; then
        echo "Error: Failed to fetch AWS credentials."
        exit 1
    fi
    
    if ! jq -e . >/dev/null 2>&1 <<< "$creds"; then
        echo "Failed to retrieve AWS credentials, try refreshing your browser."
        exit 1
    else
        user_identity=$(aws sts get-caller-identity)
        user_name=$(echo "$user_identity" | jq -r '.Arn' | awk -F'/' '{print $NF}')
        echo "Launching StackQL as: $user_name..."
        export AWS_ACCESS_KEY_ID=$(echo "$creds" | jq -r '.AccessKeyId')
        export AWS_SECRET_ACCESS_KEY=$(echo "$creds" | jq -r '.SecretAccessKey')
        export AWS_SESSION_TOKEN=$(echo "$creds" | jq -r '.Token')
    fi
    
    if [ -z "$AWS_ACCESS_KEY_ID" ] || [ -z "$AWS_SECRET_ACCESS_KEY" ] || [ -z "$AWS_SESSION_TOKEN" ]; then
        echo "Error: Failed to set AWS credentials."
        exit 1
    fi
}

assume_role_and_export_creds() {
    if [ -z "$ROLE_ARN" ]; then
        echo "Error: ROLE_ARN not provided."
        exit 1
    fi
    
    ASSUME_ROLE_OUTPUT=$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name StackQLSession)
    if [ $? -ne 0 ] || [ -z "$ASSUME_ROLE_OUTPUT" ]; then
        echo "Error: Failed to assume role."
        exit 1
    fi
    
    export AWS_ACCESS_KEY_ID=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.AccessKeyId')
    export AWS_SECRET_ACCESS_KEY=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.SecretAccessKey')
    export AWS_SESSION_TOKEN=$(echo "$ASSUME_ROLE_OUTPUT" | jq -r '.Credentials.SessionToken')
    
    aws sts get-caller-identity # to show what you are about to run as
    
    if [ $? -ne 0 ]; then
        echo "Error: Failed to verify assumed role."
        exit 1
    fi
}

ROLE_ARN=""
CMD="shell" # Default to 'shell' command
FLAGS=""

# Parse command line arguments
while [ $# -gt 0 ]; do
    case "$1" in
        --role-arn)
            shift # Move to the value of --role-arn
            ROLE_ARN="$1" # Capture the role ARN
            shift # Move past the value
            ;;
        shell|exec|ext)
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

# Assume role and export credentials if ROLE_ARN is provided, else fetch from Cloud Shell
if [ -n "$ROLE_ARN" ]; then
    assume_role_and_export_creds
else
    fetch_and_export_aws_creds
fi

# Execute the StackQL command
if [ "$CMD" = "shell" ]; then
    pull_aws_docs
    echo "Entering StackQL shell..."
    eval "./stackql shell $FLAGS"
elif [ "$CMD" = "exec" ]; then
    pull_aws_docs
    echo "Executing StackQL query..."
    eval "./stackql exec $FLAGS"
elif [ "$CMD" = "ext" ]; then
    pull_aws_docs
    echo "Creds exported for use with external tools (like pystackql)..."
    echo $AWS_ACCESS_KEY_ID
else
    show_usage
    echo
    echo "Error: invalid command ($CMD)"    
    exit 1
fi
