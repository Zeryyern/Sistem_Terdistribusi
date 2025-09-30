import os

sizes = {
    "10kb.txt": 10 * 1024,
    "100kb.txt": 100 * 1024,
    "1mb.txt": 1 * 1024 * 1024,
    "5mb.txt": 5 * 1024 * 1024,
    "10mb.txt": 10 * 1024 * 1024,
}

content = b"Trying to work with Docker, solving distribution system task\n"

# Make sure the folder exists
os.makedirs("files", exist_ok=True)

for filename, size in sizes.items():
    with open(f"files/{filename}", "wb") as f:
        # Write the content repeatedly until we reach (or exceed) the target size
        written = 0
        while written + len(content) <= size:
            f.write(content)
            written += len(content)

        # If not yet exact size, pad the rest with zeros
        if written < size:
            f.write(b"\0" * (size - written))

print("Files generated successfully with exact sizes!")
