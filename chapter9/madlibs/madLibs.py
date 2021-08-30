from pathlib import Path

path = '/Users/dylan/python/Automate_The_Boring_Stuff/chapter9/madlibs/testSentence'

sentenceFile = open(f'{path}.txt')
sentenceSplit = sentenceFile.read().split()

for i in range(len(sentenceSplit)):
    if sentenceSplit[i] == 'ADJECTIVE':
        print('Please enter an adjective: ', end = '')
        sentenceSplit[i] = input()
    elif sentenceSplit[i] == 'NOUN':
        print('Please enter a noun: ', end = '')
        sentenceSplit[i] = input()
    elif sentenceSplit[i] == 'VERB':
        print('Please enter an verb: ', end = '')
        sentenceSplit[i] = input()
    else:
        continue

sentence = ' '.join(sentenceSplit)
print(sentence)

newPath = f'{path}_complete.txt'
completeFile = open(newPath, 'w')
completeFile.write(sentence)
