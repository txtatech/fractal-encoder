import qrcode
import json
import os

def generate_qr_with_info(coordinates, neighbors):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    # Add header with coordinates
    header = f"Coordinates: {coordinates}"
    qr.add_data(header)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Add footer with neighbors
    footer = f"Neighbors: {', '.join(neighbors)}"
    qr.add_data(footer)

    # Save QR code as ASCII text
    ascii_qr = qr.get_matrix()
    text_filename = f"qr_{coordinates}.txt"
    text_filepath = os.path.join('outputs/grid', text_filename)
    with open(text_filepath, "w") as file:
        for row in ascii_qr:
            file.write("".join(["##" if module else "  " for module in row]) + "\n")

    return qr_img, text_filepath

def generate_grid(size):
    grid = []
    qr_info = []
    qr_codes_directory = "outputs/qrs"
    qr_code_filenames = [filename for filename in os.listdir(qr_codes_directory) if filename.endswith(".png")]

    for i, filename in enumerate(qr_code_filenames):
        coordinates = f"({i % size}, {i // size})"
        neighbors = get_neighbors(i % size, i // size, size)
        qr_img, text_filepath = generate_qr_with_info(coordinates, neighbors)
        grid.append(qr_img)
        qr_info.append({
            "text_filename": os.path.basename(text_filepath),
            "coordinates": coordinates,
            "neighbors": neighbors,
            "image_filename": os.path.join(qr_codes_directory, filename)
        })

    return grid, qr_info

def get_neighbors(i, j, size):
    neighbors = []
    if i > 0:
        neighbors.append(f"({i-1}, {j})")  # North
    if i < size - 1:
        neighbors.append(f"({i+1}, {j})")  # South
    if j > 0:
        neighbors.append(f"({i}, {j-1})")  # West
    if j < size - 1:
        neighbors.append(f"({i}, {j+1})")  # East
    return neighbors

def save_grid_images(grid, size, qr_info):
    os.makedirs('outputs/grid', exist_ok=True)

    for i, qr_img in enumerate(grid):
        qr_filename = f"qr_{i}.png"
        qr_img.save(os.path.join('outputs/grid', qr_filename))
        qr_info[i]['image_filename'] = qr_filename

        text_filename = qr_info[i]['text_filename']
        text_filepath = os.path.join('outputs/grid', text_filename)
        os.replace(text_filepath, os.path.join('outputs/grid', text_filename))

def save_qr_info(qr_info):
    with open(os.path.join('outputs/grid', "qr_info.json"), "w") as file:
        json.dump(qr_info, file, indent=4)

def generate_x3dom_page(qr_info, grid_size, output_file="index.html"):
    with open(os.path.join('outputs/grid', output_file), 'w') as file:
        file.write("""
<!DOCTYPE html>
<html>
<head>
    <title>3D Grid</title>
    <script src="https://www.x3dom.org/download/x3dom.js"></script>
    <link rel="stylesheet" href="https://www.x3dom.org/download/x3dom.css">
</head>
<body>
    <x3d width='100%' height='800px'>
        <scene>
            <viewpoint position='0 5 10'></viewpoint>
        """)

        # Calculate the center position of the grid
        grid_center = grid_size / 2.0

        for i, info in enumerate(qr_info):
            x = i % grid_size
            y = i // grid_size

            # Calculate the translation position relative to the center
            x_translation = (x - grid_center) * 2
            z_translation = (y - grid_center) * 2

            file.write(f"""
            <transform translation='{x_translation} 0 {z_translation}'>
                <shape>
                    <appearance>
                        <material diffuseColor='1 1 1'></material>
                        <ImageTexture url='{info['image_filename']}'/>
                    </appearance>
                    <box></box>
                </shape>
            </transform>
            """)

        file.write("""
        </scene>
    </x3d>
</body>
</html>
        """)


if __name__ == "__main__":
    grid_size = 4
    grid, qr_info = generate_grid(grid_size)

    save_grid_images(grid, grid_size, qr_info)
    save_qr_info(qr_info)
    generate_x3dom_page(qr_info, grid_size)
