#!/bin/bash

input_directory="crawl"
output_directory="binimages"

# Create the output directory if it doesn't exist
mkdir -p "$output_directory"

# Find image files and process them
while IFS= read -r -d '' file; do
    # Get the filename without extension
    filename=$(basename "$file")
    filename_noext="${filename%.*}"

    # Encode the image data as a base64 string
    base64 "$file" > "$output_directory/$filename_noext.base64"

    # Write the base64-encoded data to a .bin file
    echo "$(cat "$output_directory/$filename_noext.base64")" > "$output_directory/$filename_noext.bin"

    # Display a message for each file processed
    echo "File $filename processed."
done < <(find "$input_directory" -type f \( -iname "*.png" -o -iname "*.svg" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.bmp" \) -print0)

