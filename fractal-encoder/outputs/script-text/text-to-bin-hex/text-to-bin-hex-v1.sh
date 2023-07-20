#!/bin/bash

# Compress the input file with gzip
gzip -c input.txt > input.bin.gz

# Encode the binary data as a period character
xxd -p input.bin.gz | tr -d '\n' | sed 's/../\\\x&/g' > output.txt

mv input.bin.gz output.bin
