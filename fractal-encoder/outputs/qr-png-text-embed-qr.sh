#!/usr/bin/env bash

# Set the chunk size in characters 1000 works for large qrs 250 for small
chunk_size=1000

# Set the counter to 0
counter=0

# Create the "converted2" folder if it doesn't exist
mkdir -p converted2

# Read all PNG files in the current directory
for file in crawl/*.png; do
  # Check if the file is a PNG image
  if ! file -b "$file" | grep -q "PNG image data"; then
    continue
  fi

  # Read the image file into a string
  text=$(base64 -w0 "$file")

  # Check if the file reading was successful
  if [ $? -ne 0 ]; then
    echo "Error: Failed to read $file." >&2
    exit 1
  fi

  # Calculate the number of chunks
  num_chunks=$(( (${#text} + chunk_size - 1) / chunk_size ))

  # Split the input data into chunks
  for i in $(seq 1 $num_chunks); do
    # Extract a chunk of the input data
    chunk=${text:((i-1)*chunk_size):chunk_size}

    # Create a QR code ASCII art from the chunk of data
    output_file="converted2/qr-code-$(basename "$file")-$i.txt"
    qrencode -t ANSIUTF8 -l L -s 1 -m 0 "$chunk" > "$output_file"

    # Check if the QR code ASCII art generation was successful
    if [ $? -ne 0 ]; then
      echo "Error: Failed to generate QR code ASCII art for $file." >&2
      exit 1
    fi
  done

  # Increment the counter
  counter=$((counter + 1))

  # If the counter is divisible by 3, pause the script and reset the counter
  if [ $((counter % 3)) -eq 0 ]; then
    sleep 12
    counter=0
  fi
done

echo "QR code ASCII art embeds generated to outputs/converted2 for all PNG files in the outputs/crawl folder."
