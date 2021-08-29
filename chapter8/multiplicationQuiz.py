import pyinputplus as pyip
from random import randint
from time import sleep

numerOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numerOfQuestions):
    num1 = randint(0,9)
    num2 = randint(0,9)

    prompt = f'#{questionNumber + 1}: {num1} x {num2} = '
    
    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'], blockRegexes=[('.*', 'Incorrect!')], timeout = 8, limit = 3)

    except pyip.TimeoutException:
        print('Out of time!')

    except pyip.RetryLimitException:
        print('Out of tries!')

    else:
        # This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1
    
    sleep(1)

print(f'Score: {correctAnswers} / {numerOfQuestions}')
