import cairo
import math
import uuid
import os
from PIL import PngImagePlugin
from PIL import Image
import re
import json


class Fractal:
    def generate_fractal(self, text, num_chars):
        # Calculate the dimensions of the fractal based on the number of characters
        side_length = math.ceil(math.sqrt(num_chars))
        fractal_size = side_length * side_length

        # Pad the text with spaces to match the fractal size
        padded_text = text.ljust(fractal_size)

        # Generate the fractal data by converting the characters to ASCII values
        fractal_data = [ord(char) for char in padded_text]

        return fractal_data

    def draw_fractal_png(
        self, fractal_data, width, height, filename, fractal_identifier
    ):
        # Set up the fractal properties
        fractal_size = len(fractal_data)
        side_length = int(math.sqrt(fractal_size))
        cell_size = min(width // side_length, height // side_length)

        # Create a new Cairo image surface
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        ctx = cairo.Context(surface)

        # Clear the background
        ctx.set_source_rgb(1, 1, 1)  # Set background color to white
        ctx.rectangle(0, 0, width, height)
        ctx.fill()

        # Draw the fractal cells
        for i in range(side_length):
            for j in range(side_length):
                index = i * side_length + j
                if index < fractal_size:
                    # Calculate the cell position
                    x = j * cell_size
                    y = i * cell_size

                    # Calculate the cell color based on the ASCII value
                    value = fractal_data[index]
                    red = value / 255
                    green = value / 255
                    blue = value / 255

                    # Set the cell color and draw a rectangle
                    ctx.set_source_rgb(red, green, blue)
                    ctx.rectangle(x, y, cell_size, cell_size)
                    ctx.fill()

        # Set the fractal metadata as MIME data
        metadata = f"fractal-identifier={fractal_identifier}"
        surface.set_mime_data("text/plain", metadata.encode())

        # Save the surface as a PNG image
        output_path = os.path.join("outputs", "crawl", filename)
        surface.write_to_png(output_path)

    def draw_fractal_svg(
        self, fractal_data, width, height, filename, fractal_identifier
    ):
        # Set up the fractal properties
        fractal_size = len(fractal_data)
        side_length = int(math.sqrt(fractal_size))
        cell_size = min(width // side_length, height // side_length)

        # Create a new Cairo SVG surface
        output_path = os.path.join("outputs", "crawl", filename)
        surface = cairo.SVGSurface(output_path, width, height)
        ctx = cairo.Context(surface)

        # Clear the background
        ctx.set_source_rgb(1, 1, 1)  # Set background color to white
        ctx.rectangle(0, 0, width, height)
        ctx.fill()

        # Draw the fractal cells
        for i in range(side_length):
            for j in range(side_length):
                index = i * side_length + j
                if index < fractal_size:
                    # Calculate the cell position
                    x = j * cell_size
                    y = i * cell_size

                    # Calculate the cell color based on the ASCII value
                    value = fractal_data[index]
                    red = value / 255
                    green = value / 255
                    blue = value / 255

                    # Set the cell color and draw a rectangle
                    ctx.set_source_rgb(red, green, blue)
                    ctx.rectangle(x, y, cell_size, cell_size)
                    ctx.fill()

        # Clean up and close the surface
        ctx.show_page()
        surface.finish()

        # Embed metadata in SVG XML
        with open(output_path, "a") as svg_file:
            svg_file.write(f"<!-- Fractal Metadata: {fractal_identifier} -->\n")

        # Set the fractal identifier as metadata in SVG XML
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("fractal-identifier", fractal_identifier)

    def decode_fractal(self, fractal_data):
        # Convert the ASCII values back to characters
        text = "".join(chr(value) for value in fractal_data)

        # Remove trailing spaces
        text = text.rstrip()

        return text


def spiral():
    x = y = 0
    dx = 0
    dy = -1
    while True:
        yield (x, y)
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def main():
    # Read the text from a file
    file_path = os.path.join("outputs", "input", "afractest.txt")
    with open(file_path, "r") as file:
        text = file.read()

    # Specify the chunk size and number of characters per fractal
    chunk_size = 13200
    num_chars = 2300

    # Calculate the number of iterations required
    num_iterations = math.ceil(len(text) / chunk_size)

    # Generate a unique identifier for the fractals
    fractal_identifier = str(uuid.uuid4())

    # Set up the dimensions of the fractal images
    width = 1990
    height = 1990

    # Set the filenames for the fractal images and the decoded text files
    fractal_png_base_filename = f"{fractal_identifier}_fractal"
    fractal_svg_base_filename = f"{fractal_identifier}_fractal"
    decoded_base_filename = f"{fractal_identifier}_decoded"
    central_ledger_filename = os.path.join("outputs", "ledgers", "acentral_ledger.txt")

    # Iterate over the text in chunks and generate fractals
    for i in range(num_iterations):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size

        # Extract the chunk of text
        chunk_text = text[start_index:end_index]

        # Generate the fractal from the chunk of text
        fractal_obj = Fractal()
        fractal_data = fractal_obj.generate_fractal(chunk_text, num_chars)

        # Generate a unique identifier for the current fractal
        current_fractal_identifier = str(uuid.uuid4())

        # Set the filenames for the current fractal
        fractal_png_filename = f"{fractal_png_base_filename}_{i}.png"
        fractal_svg_filename = f"{fractal_svg_base_filename}_{i}.svg"
        decoded_filename = f"{decoded_base_filename}_{i}.txt"

        # Draw and save the fractal as a PNG image
        fractal_obj.draw_fractal_png(
            fractal_data,
            width,
            height,
            fractal_png_filename,
            current_fractal_identifier,
        )

        print(f"Fractal PNG {i} saved as {fractal_png_filename}")

        # Draw and save the fractal as an SVG image
        fractal_obj.draw_fractal_svg(
            fractal_data,
            width,
            height,
            fractal_svg_filename,
            current_fractal_identifier,
        )

        print(f"Fractal SVG {i} saved as {fractal_svg_filename}")

        # Decode the fractal back to text
        decoded_text = fractal_obj.decode_fractal(fractal_data)

        # Save the decoded text to a file
        decoded_output_path = os.path.join("outputs", "crawl", decoded_filename)
        with open(decoded_output_path, "w") as file:
            file.write(decoded_text)

        print(f"Decoded text {i} saved as {decoded_filename}")

        # Append the relevant information to the central ledger file
        with open(central_ledger_filename, "a") as ledger_file:
            ledger_file.write(f"Fractal Identifier: {current_fractal_identifier}\n")
            ledger_file.write(f"Fractal PNG: {fractal_png_filename}\n")
            ledger_file.write(f"Fractal SVG: {fractal_svg_filename}\n")
            ledger_file.write(f"Decoded Text: {decoded_filename}\n")
            ledger_file.write(
                f"BEGIN '{current_fractal_identifier}' fractal of the text\n"
            )
            ledger_file.write(decoded_text)
            ledger_file.write(
                f"\nEND '{current_fractal_identifier}' fractal of the text\n"
            )
            ledger_file.write("\n")

        print(
            f"Information {i} appended to the central ledger: {central_ledger_filename}"
        )

    # After all fractals are generated and ledger is updated, add metadata to PNG images

    # Iterate over all PNG images in the directory
    for filename in os.listdir(os.path.join("outputs", "crawl")):
        if filename.endswith(".png"):
            # Full path to the image file
            image_path = os.path.join("outputs", "crawl", filename)

            # Open the image using PIL
            image = Image.open(image_path)

            # Check if the image has PNGInfo (metadata)
            if "pnginfo" in image.info:
                # Get the PNGInfo object
                pnginfo = image.info["pnginfo"]

                # Check if the fractal-identifier metadata is present
                if "fractal-identifier" in pnginfo:
                    # Get the fractal identifier value
                    fractal_identifier = pnginfo["fractal-identifier"]

                    print(f"Fractal Identifier: {fractal_identifier}")
                else:
                    print(f"No fractal-identifier metadata found in {filename}")
            else:
                print(f"No metadata found in {filename}")


def generate_ledger_json(text, num_iterations):
    # Get the ledger data from the main script
    ledger_data = []

    # Specify the chunk size and number of characters per fractal
    chunk_size = 13200
    num_chars = 2300

    # Generate a unique identifier for the fractals
    fractal_identifier = str(uuid.uuid4())

    # Set up the dimensions of the fractal images
    width = 1990
    height = 1990

    # Set the filenames for the fractal images and the decoded text files
    fractal_png_base_filename = f"{fractal_identifier}_fractal"
    fractal_svg_base_filename = f"{fractal_identifier}_fractal"
    decoded_base_filename = f"{fractal_identifier}_decoded"

    # Iterate over the text in chunks and generate fractals
    for i in range(num_iterations):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size

        # Extract the chunk of text
        chunk_text = text[start_index:end_index]

        # Generate the fractal from the chunk of text
        fractal_obj = Fractal()
        fractal_data = fractal_obj.generate_fractal(chunk_text, num_chars)

        # Generate a unique identifier for the current fractal
        current_fractal_identifier = str(uuid.uuid4())

        # Set the filenames for the current fractal
        fractal_png_filename = f"{fractal_png_base_filename}_{i}.png"
        fractal_svg_filename = f"{fractal_svg_base_filename}_{i}.svg"
        decoded_filename = f"{decoded_base_filename}_{i}.txt"

        # Draw and save the fractal as a PNG image
        fractal_obj.draw_fractal_png(
            fractal_data,
            width,
            height,
            fractal_png_filename,
            current_fractal_identifier,
        )

        print(f"Fractal PNG {i} saved as {fractal_png_filename}")

        # Draw and save the fractal as an SVG image
        fractal_obj.draw_fractal_svg(
            fractal_data,
            width,
            height,
            fractal_svg_filename,
            current_fractal_identifier,
        )

        print(f"Fractal SVG {i} saved as {fractal_svg_filename}")

        # Decode the fractal back to text
        decoded_text = fractal_obj.decode_fractal(fractal_data)

        # Save the decoded text to a file
        decoded_output_path = os.path.join("outputs", "crawl", decoded_filename)
        with open(decoded_output_path, "w") as file:
            file.write(decoded_text)

        print(f"Decoded text {i} saved as {decoded_filename}")

        # Create an entry dictionary for the ledger data
        entry_dict = {
            "identifier": current_fractal_identifier,
            "png_file": fractal_png_filename,
            "svg_file": fractal_svg_filename,
            "text_file": decoded_filename,
            "fractal_text": decoded_text,
        }

        # Append the entry dictionary to the ledger data list
        ledger_data.append(entry_dict)

    # Assign coordinates to each ledger entry
    spiral_generator = spiral()
    for entry in ledger_data:
        entry["coordinates"] = next(spiral_generator)

    # Convert the ledger data to JSON
    ledger_json = json.dumps(ledger_data, indent=4)

    # Write the JSON data to a file
    output_path = os.path.join("outputs", "ledgers", "aledger.json")
    with open(output_path, "w") as file:
        file.write(ledger_json)


if __name__ == "__main__":
    # Read the text from a file
    file_path = os.path.join("outputs", "input", "afractest.txt")
    with open(file_path, "r") as file:
        text = file.read()

    # Specify the chunk size and number of characters per fractal
    chunk_size = 13200
    num_chars = 2300

    # Calculate the number of iterations required
    num_iterations = math.ceil(len(text) / chunk_size)

    main()
    generate_ledger_json(text, num_iterations)
