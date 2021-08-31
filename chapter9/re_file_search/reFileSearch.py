import re
from pathlib import Path

regexInput = input('Please enter a regular-expression: ')
regex = re.compile(rf'{regexInput}')

p = Path(Path.cwd())
textFiles = list(p.glob('*.txt'))

for file in textFiles:
    openFile = file.open()
    fileContent = openFile.read()
    regexFinds = regex.findall(fileContent)
    print(f'We found the following matches in the file "{file}":')
    for match in regexFinds:
        print(match)
    openFile.close()
