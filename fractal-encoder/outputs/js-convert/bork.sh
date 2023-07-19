# Extract commands and functions from the .js file
commands=$(grep -E '^\s*(function|let|const)\b' *.js)

# Initialize an empty string for the JSON objects
json_objects=""

# Iterate over each command or function
while read -r line; do
  # Encode the command or function as Base64
  base64_command=$(echo "$line" | base64)

  # Add a new JSON object to the string
  json_objects="$json_objects {\"command\": \"$base64_command\"},"
done <<< "$commands"

# Remove the trailing comma from the last JSON object
json_objects=$(echo "$json_objects" | sed 's/,$//')

# Write the JSON objects to a file
echo "[$json_objects]" > commands.json
