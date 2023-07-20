#!/usr/bin/env bash
echo "$art"

# Set the output file
output_file=all-text-files.txt

# Read all text files in the current directory
for file in *.txt; do
  # Check if the file is a text file
  if ! file "$file" | grep -q "ASCII text"; then
    continue
  fi

  # Read the text file into a string
  text=$(cat "$file")

  # Check if the file reading was successful
  if [ $? -ne 0 ]; then
    echo "Error: Failed to read $file." >&2
    exit 1
  fi

  # Append the text to the output file
  echo "$text" >> "$output_file"

  # Check if the file writing was successful
  if [ $? -ne 0 ]; then
    echo "Error: Failed to write to $output_file." >&2
    exit 1
  fi
done

echo "The contents of all text files in the current directory have been appended to $output_file."

