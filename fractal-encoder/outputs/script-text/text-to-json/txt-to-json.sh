# Iterate over all files in the current directory
for file in *
do
  # Read the contents of the file into a variable
  data=$(cat "$file")

  # Convert the data to JSON using the jq command
  json=$(echo "$data" | jq -Rs 'split("\n") | map({key: .})')

  # Save the JSON data to a file
  echo "$json" > "${file%.*}.json"
done

