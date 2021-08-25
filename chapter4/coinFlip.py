import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    for i in range(0,100):
        coinFlips.append(random.randint(0,1))
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(0,len(coinFlips) - 6):
        if coinFlips[i] == coinFlips[i + 1] and coinFlips[i] == coinFlips[i + 2] and coinFlips[i] == coinFlips[i + 3] and coinFlips[i] == coinFlips[i + 4] and coinFlips[i] == coinFlips[i + 5]:
            numberOfStreaks += 1
            break
    
print('Chance of streak: %s%%' % (numberOfStreaks / (100 * 10000)))