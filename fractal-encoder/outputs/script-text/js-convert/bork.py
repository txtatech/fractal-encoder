import re
import json
import base64

# Open the JavaScript file and read its contents
with open('worker.js', 'r') as file:
    js_content = file.read()

# Use a regular expression to find lines starting with 'const', 'let', or 'function'
pattern = re.compile(r'^(.*(?:const|let|function).*)$', re.MULTILINE)
matches = pattern.findall(js_content)

# Initialize an empty list for the JSON objects
json_objects = []

# Iterate over the matched lines
for line in matches:
    # Encode the line in Base64
    base64_line = base64.b64encode(line.encode()).decode()

    # Add a new JSON object to the list
    json_objects.append({"command": base64_line})

# Write the JSON objects to a file
with open('commands.json', 'w') as file:
    json.dump(json_objects, file)
