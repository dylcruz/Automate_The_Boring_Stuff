import re

path = '/Users/dylan/python/Automate_The_Boring_Stuff/chapter9/madlibs/testSentence'
sentenceFile = open(f'{path}.txt')
sentence = sentenceFile.read()
sentenceFile.close()

findReplacement = re.compile(r'(NOUN|VERB|ADJECTIVE)')

for match in findReplacement.findall(sentence):   
    sentence = findReplacement.sub(input(f'Please enter a(n) {match}: '), sentence, count = 1)

print(sentence)

newPath = f'{path}_complete.txt'
newSentenceFile = open(f'{path}_complete.txt', 'w')
newSentenceFile.write(sentence)
newSentenceFile.close()
