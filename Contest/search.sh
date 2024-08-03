#!/bin/bash

# Check if the user provided a search substring
if [ -z "$1" ]; then
    echo "Usage: $0 <substring>"
    exit 1
fi

# Get the search substring from the first command-line argument
substring="$1"

# Specify the directory where you want to search
directory="."  # Replace with the actual directory path

# Perform the case-insensitive search using the find command
find "$directory" -type f -iname "*$substring*"
