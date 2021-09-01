import os
import re
from pathlib import Path
import shutil

fileSearch = re.compile(r'^(.*)(\d\d\d)\.(.*)$')

filesFound = []

while True:
    searchPath = Path(input('Please enter a valid folder path to search through (Ex. /Users/Dylan): '))
    if os.path.exists(searchPath):
        break
    print(f'{searchPath} does not exist.')

for fileName in os.listdir(searchPath):
    if fileSearch.search(fileName) == None:
        continue
    filesFound.append(fileName)

filesFound.sort()

lastFileNum = 1

for fileName in filesFound:
    fileReg = fileSearch.search(fileName)
    if int(fileReg.group(2)) == lastFileNum:
        lastFileNum += 1
        continue
    else:
        newFileNum = int(fileReg.group(2)) - 1
        print(os.path.abspath(searchPath / fileName))
    