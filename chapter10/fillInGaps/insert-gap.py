import re
import shutil
from pathlib import Path

MATCH_PATTERN = r'([a-zA-Z]*)(\d*)(\..*)'
FILE_PATH = './test'
while True:
    folder = Path(input("Enter the file path: "))
    folder = Path(FILE_PATH)
    if folder.exists() and folder.is_dir():
        break
    else:
        print("Invalid path. Please enter the path of a directory.")

files = sorted([file for file in folder.iterdir()])
print(f"Found {len(files)} files in the directory.")

while True:
    try:
        insert_num = int(input(f"Enter number to insert (1 - {len(files)}): "))
        if insert_num < 1 or insert_num > len(files):
            raise ValueError
        break
    except ValueError:
        print("Enter a whole, positive number that's inside the file found range.")

sliced_files = sorted(files[insert_num-1:], reverse=True)
for file in sliced_files:
    file_match = re.match(MATCH_PATTERN, file.name)
    file_name, file_num, file_ext = file_match.groups()
    new_file_num = int(file_num) + 1

    if new_file_num < 10:
        new_file_num_str = f"00{new_file_num}"
    elif new_file_num < 100:
        new_file_num_str = f"0{new_file_num}"
    else:
        new_file_num_str = str(new_file_num)

    new_file_str = file_name + new_file_num_str + file_ext
    new_file = Path(f"{FILE_PATH}/{new_file_str}")
    print(f"Moving {file} to {new_file}")
    shutil.move(file, new_file)
