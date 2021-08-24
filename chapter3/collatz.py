def collatz(number):
    if number == 1:
        print(number)
        return number
    elif number % 2 == 0:
        print(int(number / 2))
        return number / 2
    else:
        print(int(3 * number + 1))
        return int(3 * number + 1)


userNumber = 0

print("Enter number:")

while True:
    try:
        userNumber = int(input())
        if userNumber < 0:
            print('Please enter a positive number.')
            continue
        break
    except ValueError:
        print("Please enter an integer.")

while userNumber != 1 and userNumber != 0:
    userNumber = collatz(userNumber)
