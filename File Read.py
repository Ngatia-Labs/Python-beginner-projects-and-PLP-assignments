# File Read & Write Challenge 🖋️

# Open original file for reading
with open("list.py", "r") as infile:
    content = infile.read()

# Modify the content (example: make it uppercase)
modified_content = content.upper()

# Write modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been read, modified, and written to output.txt")