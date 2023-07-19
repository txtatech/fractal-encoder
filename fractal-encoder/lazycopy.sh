#!/bin/bash

# Source and destination directories
source_dir="outputs/crawl"
destination_dir="outputs/fractals"

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Copy PNG files from source to destination
find "$source_dir" -type f -iname "*.png" -exec cp {} "$destination_dir" \;

echo "PNG files copied successfully from $source_dir to $destination_dir."

