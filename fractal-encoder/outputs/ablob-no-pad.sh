#!/usr/bin/env bash

# Show the options for the output folder
echo "Choose an output folder:"
echo "1. converted1"
echo "2. converted2"

# Read the user's choice
read -rp "Enter the number corresponding to your choice: " choice

# Set the input and output folders based on the user's choice
case "$choice" in
  1)
    input_folder="converted1"
    ;;
  2)
    input_folder="converted2"
    ;;
  *)
    echo "Invalid choice. Exiting..."
    exit 1
    ;;
esac

# Directory path to search for text files
input_directory="$input_folder"
output_directory="blob"

# Create the blob.txt file
output_file="blob1.txt"
touch "$output_directory/$output_file"

# Find all text files in the input directory and sort them based on the coordinates in the file names
files=$(find "$input_directory" -type f -name "*.txt" | sort -t '_' -k2,2n -k3,3n)

# Append the contents of each file to the blob.txt file
for file in $files; do
  # Read the contents of the file
  contents=$(cat "$file")

  # Append the contents to the blob.txt file in the output directory
  echo "$contents" >> "$output_directory/$output_file"
done

echo "Text files from $input_directory appended to $output_directory/$output_file"

