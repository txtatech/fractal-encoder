#!/bin/bash

input_directory="blob"
output_directory="bintext"

# Create the output directory if it doesn't exist
mkdir -p "$output_directory"

# Chunk size in bytes
chunk_size=8192

# Find text files and convert them to binary
find "$input_directory" -type f -name "*.txt" -print0 | while IFS= read -r -d '' file; do
    filename=$(basename "$file")
    filename_noext="${filename%.*}"
    base64_file="$output_directory/$filename_noext.base64"
    output_file="$output_directory/$filename_noext.bin"

    # Check if the text file is empty
    if [[ ! -s "$file" ]]; then
        echo "File $filename is empty. Skipping."
        continue
    fi

    # Encode text file as base64
    base64 "$file" > "$base64_file"

    # Convert base64 to binary in chunks
    if ! base64 -di "$base64_file" | dd of="$output_file" bs="$chunk_size" conv=sync,fsync,notrunc status=none; then
        echo "Failed to convert $filename to binary."
    else
        echo "File $filename converted to binary. Output saved to $output_file"
    fi

    # Remove temporary base64 file
    rm "$base64_file"
done

