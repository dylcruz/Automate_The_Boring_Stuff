import re

def stripRegex(word, charToStrip = ' '):   
    stripper = re.compile(r'%s*' % charToStrip)
    print(stripper.sub('', word))

stripRegex('    HELLO     ')
stripRegex('----HELLO-----', '-')
stripRegex('ABCDEFzzzzzzzzzzzzzz', 'z')
stripRegex('zzzzzzzzzzzzzzABCDEF', 'z')