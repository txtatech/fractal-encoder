import json
import os
from PIL import Image
import base64

def generate_grid(size):
    grid = []
    qr_info = []
    qr_codes_directory = "outputs/fractals"  # Directory containing the fractal PNGs
    qr_code_filenames = [filename for filename in os.listdir(qr_codes_directory) if filename.endswith(".png")]

    for i, filename in enumerate(qr_code_filenames):
        coordinates = f"({i % size}, {i // size})"
        neighbors = get_neighbors(i % size, i // size, size)
        image_filepath = os.path.join(qr_codes_directory, filename)
        image = Image.open(image_filepath)

        # Resize the image to the desired size
        image = image.resize((128, 128))

        qr_info.append({
            "coordinates": coordinates,
            "neighbors": neighbors,
            "image": image,
            "image_filename": filename
        })

    return qr_info

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

def save_grid_images(qr_info, size):
    os.makedirs('outputs/grid2', exist_ok=True)

    for i, info in enumerate(qr_info):
        image = info['image']
        grid_filename = f"grid_{i}.png"
        grid_filepath = os.path.join('outputs/grid2', grid_filename)
        image.save(grid_filepath)

        qr_info[i]['image_filename'] = grid_filename

def save_qr_info(qr_info):
    for info in qr_info:
        image = info['image']
        # Convert the image to a base64-encoded string
        image_base64 = base64.b64encode(image.tobytes()).decode('utf-8')
        # Update the 'image' key with the base64 string
        info['image'] = image_base64

    with open(os.path.join('outputs/grid2', "qr_info.json"), "w") as file:
        json.dump(qr_info, file, indent=4)

def generate_x3dom_page(qr_info, grid_size, output_file="index.html"):
    with open(os.path.join('outputs/grid2', output_file), 'w') as file:
        file.write("""
<!DOCTYPE html>
<html>
<head>
    <title>3D Grid</title>
    <script src="https://www.x3dom.org/download/x3dom.js"></script>
    <link rel="stylesheet" href="https://www.x3dom.org/download/x3dom.css">
    <style>
        html, body {
            height: 100%;
            margin: 0;
            overflow: hidden;
        }
        #x3d-container {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <div id="x3d-container">
        <x3d width='100%' height='100%'>
            <scene>
                <viewpoint position='0 5 10'></viewpoint>
        """)

        for i, info in enumerate(qr_info):
            x = i % grid_size
            y = i // grid_size

            # Calculate the translation position
            x_translation = x - (grid_size // 2)
            z_translation = y - (grid_size // 2)

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
    </div>
</body>
</html>
        """)


if __name__ == "__main__":
    grid_size = 4
    qr_info = generate_grid(grid_size)

    save_grid_images(qr_info, grid_size)
    save_qr_info(qr_info)
    generate_x3dom_page(qr_info, grid_size)
