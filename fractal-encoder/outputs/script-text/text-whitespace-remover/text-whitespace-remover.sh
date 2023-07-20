# Find all text files in the current directory
files=$(find . -type f -name "*.txt")

# Iterate over the list of text files
for file in $files; do
  # Remove all whitespace from each line
  awk '{$1=$1};1' "$file" | tr -d ' ' | > output.txt
done

