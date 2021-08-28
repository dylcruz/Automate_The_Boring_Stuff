import re

def checkPassword(password):
    
    # Copied from StackOverflow, this is how to do it in one line
    """
    checkAllInOne = re.compile(r'''
        ^(?=.*[A-Z])                # Positive lookahaed to search for A - Z
        (?=.*[0-9])                 # Positive lookahead to search for 0 - 9
        (?=.*[a-z])                 # Positive lookahead to search for a - z
        .{8,}$''', re.VERBOSE)      # Match 8 or more of any character
    
    if checkAllInOne.search(password) == None:
        print("Not secure.")
        return
    else:
        print("Secure.")
        return
    """

    if len(password) >= 8:
        
        checkLowerLetters = re.compile(r'[a-z]')
        checkUpperLetters = re.compile(r'[A-Z]')
        checkDigits = re.compile(r'[0-9]')

        if checkLowerLetters.search(password) == None:
            print(password + ' is not a secure password! It must contain at least 1 lower case letter!')
            return
        if checkUpperLetters.search(password) == None:
            print(password + ' is not a secure password! It must contain at least 1 upper case letter!')
            return
        if checkDigits.search(password) == None:
            print(password + ' is not a secure password! It must contain at least 1 number!')
            return
        
        print(password + ' is a secure password!')

    else:
        print(password + ' is not a secure password! It is not at least 8 characters!')
        return

shortPass = 'pass'
lowerPass = 'password'
upperPass = 'PASSWORD'
noDigitsPass = 'Password'
fullPass = 'Password1'

checkPassword(shortPass)
checkPassword(lowerPass)
checkPassword(upperPass)
checkPassword(noDigitsPass)
checkPassword(fullPass)
