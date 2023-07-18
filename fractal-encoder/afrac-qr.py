import json
import segno
import os

# Maximum amount of data to put in a single QR code
MAX_DATA_PER_QR = 760

# Load the ledger.json file
with open('outputs/ledgers/aledger.json', 'r') as file:
    ledger = json.load(file)

# Create the outputs/qrs directory if it doesn't exist
os.makedirs('outputs/qrs', exist_ok=True)

# Loop through each entry in the ledger
for entry in ledger:
    # Combine the information you want to store in the QR code
    qr_data = json.dumps({
        'identifier': entry['identifier'],
        'png_file': entry['png_file'],
        'svg_file': entry['svg_file'],
        'text_file': entry['text_file'],
        'fractal_text': entry['fractal_text'],
        'coordinates': entry['coordinates']
    })

    # Split the data into chunks that fit into a QR code
    qr_data_chunks = [qr_data[i:i+MAX_DATA_PER_QR] for i in range(0, len(qr_data), MAX_DATA_PER_QR)]

    # Generate a QR code for each chunk
    for i, data_chunk in enumerate(qr_data_chunks):
        qr = segno.make(data_chunk)

        # Save the QR code as a PNG file, adding an up-down axis indicator and a sequence number if there are multiple QR codes for this entry
        filename = f"outputs/qrs/{entry['identifier']}_qr{'U' if len(qr_data_chunks) > 1 else ''}{i}.png"
        qr.save(filename, scale=10)
