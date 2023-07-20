#!/usr/bin/env bash

# Set the chunk size in bytes
chunk_size=1000000

# Check if the required tools are installed
if ! command -v base64 > /dev/null; then
  echo "Error: base64 is not installed." >&2
  exit 1
fi

if ! command -v qrencode > /dev/null; then
  echo "Error: qrencode is not installed." >&2
  exit 1
fi

# Check if the input file exists
if [ ! -f image.png ]; then
  echo "Error: image.png does not exist." >&2
  exit 1
fi

# Get the size of the input file in bytes
file_size=$(wc -c < image.png)

# Calculate the number of chunks
num_chunks=$(( (file_size + chunk_size - 1) / chunk_size ))

# Process the input file in chunks
for i in $(seq 1 $num_chunks); do
  # Read the chunk of the input file into a base64-encoded string
  base64_data=$(dd if=image.png bs=$chunk_size count=1 skip=$((i-1)) 2> /dev/null | base64)

  # Check if the base64 encoding was successful
  if [ $? -ne 0 ]; then
    echo "Error: Failed to encode image.png as base64." >&2
    exit 1
  fi

  # Create a QR code image from the base64-encoded data
  qrencode -o qr-code-$i.png "data:image/png;base64,${base64_data}"

  # Check if the QR code generation was successful
  if [ $? -ne 0 ]; then
    echo "Error: Failed to generate QR code image." >&2
    exit 1
  fi
done

echo "QR code images generated successfully: qr-code-*.png"

