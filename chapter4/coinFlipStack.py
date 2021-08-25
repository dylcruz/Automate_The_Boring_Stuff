import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlips = []
    streak = 0

    for i in range(0,100):
        coinFlips.append(random.randint(0,1))
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(1,len(coinFlips)):
        if coinFlips[i] == coinFlips[i - 1]:
            streak += 1
        else:
            streak = 0
        
        if streak >= 6:
            numberOfStreaks += 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / (100 * 10000)))
