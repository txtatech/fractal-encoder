#!/bin/bash

# Define a function to serialize the JSON object
serialize() {
  # Read the JSON object from the input file
  json_object=$(cat input.json)

  # Serialize the JSON object into a binary representation using jq
  binary=$(echo "$json_object" | jq --raw-output --compact-output '.')

  # Write the binary data to the output file
  echo "$binary" > output.bin
}

# Define a function to deserialize the binary data
deserialize() {
  # Read the binary data from the output file
  binary=$(cat output.bin)

  # Parse the binary data and convert it back into a JSON object using jq
  json_object=$(echo "$binary" | jq --raw-input '.')

  # Write the JSON object to the input file
  echo "$json_object" > input.json
}

# Display the main menu
while true; do
  clear
  echo "JSON Serialization Tool"
  echo "-------------------------------"
  echo "1. Serialize"
  echo "2. Deserialize"
  echo "3. Quit"
  read -p "Enter your choice: " choice

  case $choice in
    1) serialize;;
    2) deserialize;;
    3) exit;;
    *) echo "Invalid choice";;
  esac
done

