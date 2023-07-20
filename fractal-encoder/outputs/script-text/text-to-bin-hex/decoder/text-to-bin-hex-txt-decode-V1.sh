#!/bin/bash

# Decode the hexadecimal representation back to binary data
sed 's/\\x//g' output.txt | xxd -r -p > output.bin

# Decompress the binary data using gzip
gzip -d output.bin

# Rename the decompressed file
mv output.bin.gz input.bin

# Extract the original text file
gzip -d input.bin

# Rename the extracted file
mv input.bin.txt output.txt

