import re
import shutil
from pathlib import Path

# Matches: (Group 1: Prefix)(Group 2: Number)(Group 3: Extension)
# Example: "spam001.txt" -> "spam", "001", ".txt"
MATCH_PATTERN = re.compile(r'^(.*?)(\d+)(\.[^.]*)?$')
# Default path for testing, but allow override
DEFAULT_PATH = './test'

while True:
    user_input = input(f"Enter the file path (default: {DEFAULT_PATH}): ")
    if not user_input:
        folder = Path(DEFAULT_PATH)
    else:
        folder = Path(user_input)

    if folder.exists() and folder.is_dir():
        break
    else:
        print("Invalid path. Please enter the path of a directory.")

# Find only files that match our pattern
matched_files = []
for file_path in folder.iterdir():
    match = MATCH_PATTERN.search(file_path.name)
    if match:
        matched_files.append((file_path, match))

# Sort by the integer value of the number part (Group 2)
# This handles "file2.txt" vs "file10.txt" correctly
matched_files.sort(key=lambda x: int(x[1].group(2)))

print(f"Found {len(matched_files)} matching files in the directory.")

if not matched_files:
    print("No files found matching the pattern.")
    exit()

while True:
    try:
        # User enters 1-based index to create a gap at
        insert_num = int(input(f"Enter where to insert gap (1 - {len(matched_files)}): "))
        if insert_num < 1 or insert_num > len(matched_files):
            raise ValueError
        break
    except ValueError:
        print(f"Please enter a number between 1 and {len(matched_files)}.")

# We process from the insertion point to the end.
# We must process in REVERSE order to avoid overwriting files.
# e.g. Rename 003 -> 004 before renaming 002 -> 003.
files_to_move = matched_files[insert_num-1:]
files_to_move.sort(key=lambda x: int(x[1].group(2)), reverse=True)

for file_path, match in files_to_move:
    prefix = match.group(1)
    number_str = match.group(2)
    extension = match.group(3) if match.group(3) else ''

    # Calculate new number
    new_number = int(number_str) + 1
    
    # Preserve original padding (e.g., if original was "001", length is 3)
    padding = len(number_str)
    new_number_str = str(new_number).zfill(padding)

    new_filename = f"{prefix}{new_number_str}{extension}"
    new_file_path = folder / new_filename

    print(f"Moving {file_path.name} to {new_filename}")
    shutil.move(file_path, new_file_path)
