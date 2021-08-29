from pyinputplus import inputYesNo
from sys import exit

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = inputYesNo(prompt)
    if response == 'yes':
        continue
    else:
        print('Thank you. Have a nice day.')
        exit()
