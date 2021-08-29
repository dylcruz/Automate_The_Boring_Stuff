import pyinputplus as pyip

bread = {'wheat': 2, 'white': 1, 'sourdough': 1.50}
protein = {'chicken': 5, 'turkey': 5, 'ham': 6, 'tofu': 3}
cheese = {'cheddar': 1, 'swiss': 1.50, 'mozzarella': 1.50}
totalPrice = 0

breadChoice = pyip.inputMenu(list(bread), prompt = 'Please choose a type of bread:\n', numbered = True)
totalPrice += bread[breadChoice]

proteinChoice = pyip.inputMenu(list(protein), prompt = 'Please choose a type of meat:\n', numbered = True)
totalPrice += protein[proteinChoice]

cheeseYesOrNo = pyip.inputYesNo(prompt = 'Would you like cheese?\n')
if cheeseYesOrNo == 'yes':
    cheeseChoice = pyip.inputMenu(list(cheese), prompt = 'Please choose a type of meat:\n', numbered = True)
    totalPrice += cheese[cheeseChoice]
else:
    cheeseChoice = 'no'

toppingsYesOrNo = pyip.inputYesNo(prompt = 'Would you like mayo, mustard, lettuce, or tomato?\n')

numSandwiches = pyip.inputInt(prompt = 'How many sandwiches would you like?\n', min = 1)
totalPrice = totalPrice * numSandwiches

if numSandwiches == 1:
    print(f'{numSandwiches} {proteinChoice} sandwich with {cheeseChoice} cheese will cost ${totalPrice}.')
else:
    print(f'{numSandwiches} {proteinChoice} sandwiches with {cheeseChoice} cheese will cost ${totalPrice}.')