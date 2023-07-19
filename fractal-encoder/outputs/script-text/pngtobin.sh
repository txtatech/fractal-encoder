# Encode the image data as a base64 string
base64 image.png > image.base64

# Write the base64-encoded data to a .bin file
echo "$(cat image.base64)" > image.bin

# Remove the temporary base64 file
rm image.base64

