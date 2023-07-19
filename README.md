# fractal-encoder
A fork of frac-crawl with a more complete tool-set for fractal encoding, lattice structuring, ASCII art qr code generation, 3D QR code grid generation and mapping for programmable terrain.

# Fractal Encoder Project

## Overview

Fractal-Encoder is a project which involves transforming text data into visual fractals, encoding those fractals into QR codes, and converting those QR codes into ASCII art. This process demonstrates concepts in data representation, data compression, data encryption, and data visualization.

## Dependencies

To run this project, you'll need:

- Python 3.x
- Bash shell
- Python libraries:
  - numpy
  - matplotlib
  - svgwrite
  - svglib
  - reportlab
  - json
  - segno
  - x3dom
- Bash utilities:
  - base64
  - file
  - qrencode
  - exiftool

## Project Structure

The project is structured as follows:

1. **afrac-main.py:** Generates fractals based on input text. The fractals are saved as PNG and SVG images. Decodes the fractals back to text and saves this as a text file. Records information related to each fractal in a ledger, in both text and JSON format.

2. **afrac-qr.py:** Takes the ledger data and converts it into QR codes. Each QR code contains a chunk of data from the ledger that can fit into a single QR code. The QR codes are saved as PNG images.

3. **afrac-grid.py:** Generates a 3D grid of the QR codes from the previous step and creates an HTML page using X3DOM to visualize the 3D grid of QR codes.

4. **Shell scripts:** Convert the PNG images into QR code ASCII art, and then concatenate these ASCII arts into one or two 'blob' files, one with padding and one without.

## Step-by-step Process

Here's a step-by-step breakdown of the process:

1. **Text to Fractal Transformation:** The `afrac-main.py` script ingests a large text file, and for each chunk of text, it generates a unique fractal. Each fractal is saved as both a PNG image and an SVG image. The fractal is then decoded back to text and saved as a text file. All the information about each fractal is appended to a "central ledger" text file and a JSON file.

2. **Fractal Information to QR Codes:** The `afrac-qr.py` script takes the ledger data and converts it into QR codes. It separates the information in the ledger into chunks that fit into a single QR code, generating a QR code for each chunk. These QR codes are saved as PNG images.

3. **QR Code Visualization:** The `afrac-grid.py` script generates a 3D grid of QR codes from the previous step. It generates an HTML page using X3DOM to visualize this 3D grid of QR codes.

4. **QR Codes to ASCII Art:** The shell scripts 'qr-png-ascii-convert.sh' and 'qr-png-text-embed-qr.sh' convert the PNG images of QR codes into QR code ASCII art. The outputs are stored in 'converted1' or 'converted2' directories.

5. **ASCII Art Consolidation:** The shell scripts 'ablob-no-pad.sh' and 'ablob-padding.sh' concatenate the QR code ASCII art files into a single file, with the latter adding additional line padding.

## How to Run

1. Start by running `afrac-main.py` to generate the fractals and the ledger.

2. Run `afrac-qr.py` to convert the ledger data into QR codes.

3. Run `afrac-grid.py` to generate the 3D grid of QR codes and the HTML visualization.

4. Run either `qr-png-ascii-convert.sh` or `qr-png-text-embed-qr.sh` to convert the PNG images of QR codes into QR code ASCII art.

5. Run either `ablob-no-pad.sh` or `ablob-padding.sh` to concatenate the QR code ASCII art files into a single 'blob' file.

6. To run the entire process at once, use `afrac-full.sh`.

## Note

This project involves a number of transformations between different data representations, which might be computationally intensive and time-consuming. Consider the requirements of your machine before executing the scripts.

# Version 0.0.03 Notes:

Fixed metadta function.
Added hashing function.
Added metadata, hash checks and logging.
Added png, bin, text, javascript and other processing tools to the outputs folder.

# MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
