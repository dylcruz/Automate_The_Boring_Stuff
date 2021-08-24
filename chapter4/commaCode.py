def listCombine(myList):
    if len(myList) == 0:
        print("This list is empty!")
        return

    for i in range(len(myList)):
        if i == len(myList) - 1:
            print('and ' + myList[i] + '.')
        else:
            print(myList[i] + ', ', end='')


spam = ['apples', 'bananas', 'tofu', 'cats', 'apples', 'bananas', 'tofu', 'cats']
listCombine(spam)
spam2 = []
listCombine(spam2)
