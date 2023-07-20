import base64

# Open the JavaScript file and read its contents
with open('worker.js', 'r') as file:
    js_code = file.read()

# Add the necessary escaping
escaped_js_code = js_code.replace('\\', '\\\\').replace('\n', '\\n')

# Encode the escaped JavaScript code in Base64
encoded_script = base64.b64encode(escaped_js_code.encode()).decode()

# Write the encoded script to a file
with open('encoded_script.txt', 'w') as file:
    file.write(encoded_script)
