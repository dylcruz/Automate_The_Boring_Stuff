import random
import sys

wins = 0
ties = 0
losses = 0
playerMove = ''
computerMove = ''
computerMoveInt = 0
playerChoice = ''
computerChoice = ''

print("ROCK, PAPER, SCISSORS")

while True:

    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    playerChoice = input()
    playerChoice = playerChoice.lower()

    if playerChoice != 'r' and playerChoice != 'p' and playerChoice != 's' and playerChoice != 'q':
        print("INVALID CHOICE. CHOOSE AGAIN.")
        continue

    if playerChoice == 'q':
        print("Your final stats were: " + str(wins) + " wins. " + str(losses) + " losses. " + str(ties) + " ties.")
        sys.exit()

    if playerChoice == 'r':
        playerMove = 'ROCK'
    if playerChoice == 'p':
        playerMove = 'PAPER'
    if playerChoice == 's':
        playerMove = 'SCISSORS'

    computerMoveInt = random.randint(1, 3)
    if computerMoveInt == 1:
        computerMove = 'ROCK'
        computerChoice = 'r'
    if computerMoveInt == 2:
        computerMove = 'PAPER'
        computerChoice = 'p'
    if computerMoveInt == 3:
        computerMove = 'SCISSORS'
        computerChoice = 's'

    print(playerMove + " versus...")
    print(computerMove)

    if playerChoice == computerChoice:
        print("It is a tie!")
        ties = ties + 1
    elif playerChoice == 'r' and computerChoice == 'p':
        print("You lose!")
        losses = losses + 1
    elif playerChoice == 'r' and computerChoice == 's':
        print("You win!")
        wins = wins + 1
    elif playerChoice == 'p' and computerChoice == 's':
        print("You lose!")
        losses = losses + 1
    elif playerChoice == 'p' and computerChoice == 'r':
        print("You win!")
        wins = wins + 1
    elif playerChoice == 's' and computerChoice == 'r':
        print("You lose!")
        losses = losses + 1
    elif playerChoice == 's' and computerChoice == 'p':
        print("You win!")
        wins = wins + 1
