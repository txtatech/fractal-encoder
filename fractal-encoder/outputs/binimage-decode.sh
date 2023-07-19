#!/bin/bash

input_directory="bintext"
output_directory="binimgdecode"

# Create the output directory if it doesn't exist
mkdir -p "$output_directory"

# Find bin and base64 files and process them
find "$input_directory" -type f \( -iname "*.bin" -o -iname "*.base64" \) -print0 | while IFS= read -r -d '' file; do
    filename=$(basename "$file")
    filename_noext="${filename%.*}"
    output_file="$output_directory/$filename_noext.bin"

    if [[ $filename == *.base64 ]]; then
        base64 -di "$file" > "$output_file"
    elif [[ $filename == *.bin ]]; then
        cp "$file" "$output_file"
    fi

    echo "File $filename processed. Output saved to $output_file"
done

