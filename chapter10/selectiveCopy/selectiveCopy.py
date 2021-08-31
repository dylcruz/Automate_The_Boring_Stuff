from genericpath import exists
import os
import shutil
import re

findFiles = re.compile(r'.*(\.pdf|\.jpg)$')
folder = os.path.abspath('files')
newFolder = os.path.abspath('copiedFiles')

if not os.path.exists(newFolder):
    os.mkdir(newFolder)

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if findFiles.search(filename) == None:
            continue
        else:
            shutil.copy(os.path.join(foldername, filename), newFolder)
