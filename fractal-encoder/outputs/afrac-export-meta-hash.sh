#!/bin/bash

output_file="integrity/metahashes.txt"

# Create or clear the output file
> "$output_file"

# Function to extract metadata and hash of a file
extract_metadata_and_hash() {
    file="$1"
    echo "File: $file" >> "$output_file"
    echo "Metadata:" >> "$output_file"
    exiftool "$file" >> "$output_file"  # Assuming exiftool is installed for extracting metadata
    echo "Hash: $(md5sum "$file" | awk '{print $1}')" >> "$output_file"
    echo >> "$output_file"
}

# Loop through PNG files in the crawl folder
for file in crawl/*.png; do
    extract_metadata_and_hash "$file"
done

# Loop through SVG files in the crawl folder
for file in crawl/*.svg; do
    extract_metadata_and_hash "$file"
done

echo "Extraction complete. The metadata and hashes have been saved in $output_file."

