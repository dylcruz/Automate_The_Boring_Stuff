import os
from pathlib import Path

while True:
    searchPath = Path(input('Please enter a valid folder path to search through (Ex. /Users/Dylan): '))
    if os.path.exists(searchPath):
        break
    print(f'{searchPath} does not exist.')

print(f'Searching through {searchPath} for files > 100MB...')

filesFound = 0
filesError = 0
largestFileSize = 0
largestFilePath = ''
for foldername, subfolders, filenames in os.walk(searchPath):
    for filename in filenames:
        filePath = os.path.join(foldername, filename)
        absFilePath = os.path.abspath(os.path.join(foldername, filename))

        try:
            if os.path.getsize(absFilePath) > 100000000:
                print(f'The file {filePath} is > 100MB ({os.path.getsize(absFilePath) / 1000000} MB.)')
                filesFound += 1
                if os.path.getsize(absFilePath) > largestFileSize:
                    largestFileSize = os.path.getsize(absFilePath)
                    largestFilePath = absFilePath

        except FileNotFoundError:
            print(f'ERROR! Unable to get the size of {absFilePath}. Skipping.')
            filesError += 1

print(f'Search done. We found {filesFound} file(s) larger than 100MB.')
print(f'{filesError} file(s) were not included in the search due to errors.')
print(f'The largest file is {largestFilePath} at {largestFileSize / 1000000} MB.')