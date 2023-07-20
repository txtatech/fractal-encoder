import json

def update_ledger_with_hashes(ledger_file_path, hash_file_path, output_file_path):
    # Load the ledger
    with open(ledger_file_path, 'r') as f:
        ledger = json.load(f)

    # Load the hashes
    with open(hash_file_path, 'r') as f:
        lines = f.readlines()

    # Iterate over each entry in the ledger
    for entry in ledger:
        # Retrieve the filenames from the entry
        png_filename = entry['png_file']
        svg_filename = entry['svg_file']

        # Retrieve the corresponding hashes from the hash file
        png_hash = get_hash_from_hash_file(lines, png_filename)
        svg_hash = get_hash_from_hash_file(lines, svg_filename)

        # Update the entry with the hashes
        entry['png_hash'] = png_hash
        entry['svg_hash'] = svg_hash

    # Save the updated ledger to a new file
    with open(output_file_path, 'w') as f:
        json.dump(ledger, f, indent=4)

def get_hash_from_hash_file(lines, filename):
    found_filename = False
    for line in lines:
        if f"File: crawl/{filename}" in line:
            found_filename = True
        elif "Hash: " in line and found_filename:
            return line.split(": ")[1].strip()  # Get the hash

    return None  # Return None if the file is not found in the hash file

def main():
    # Call the function with the appropriate file paths
    update_ledger_with_hashes('outputs/ledgers/aledger.json', 'outputs/integrity/metahashes.txt', 'outputs/ledgers/bledger.json')

    print("Hashes in outputs/integrity/metahashes.txt copied! outputs/ledgers/aledger.json parsed! outputs/ledger/bledger.json created with hashes!")

if __name__ == "__main__":
    main()
