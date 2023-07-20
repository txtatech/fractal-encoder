#!/bin/bash

output_file="integrity/metahashes.txt"

# Clear or create the output file
truncate --size 0 "$output_file"

# Function to extract metadata and hash of a file
extract_metadata_and_hash() {
    file="$1"
    echo "File: $file"
    echo "Metadata:"
    exiftool "$file" || echo "Error extracting metadata for $file"
    echo "Hash: $(md5sum "$file" | awk '{print $1}')"
    echo
}

# Loop through all files in the crawl folder
for file in crawl/*; do
    # Check if the file is PNG or SVG
    if [[ "$file" == *.png || "$file" == *.svg ]]; then
        extract_metadata_and_hash "$file" >> "$output_file"
    fi
done

echo "Extraction complete. The metadata and hashes are saved in $output_file."

