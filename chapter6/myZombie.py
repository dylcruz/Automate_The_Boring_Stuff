import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class MyZombieRandAfterFirstRoll:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            if random.randint(0,1) == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break 

class MyZombieTwoShotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break 

class MyZombieRoll14StopTwoShot:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        numRolls = 0
        randRolls = random.randint(1,4)
        shotguns = 0

        diceRollResults = zombiedice.roll() # first roll
        numRolls += 1    

        while diceRollResults is not None:            
            if numRolls == randRolls:
                break

            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
                numRolls += 1
            else:
                break 

class MyZombieMoreShotThanBrain:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        brains = 0
        
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            
            if brains > shotguns and shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
            

zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='Stop after 2 or more brains'),
    #MyZombieRandAfterFirstRoll(name='Random After First Roll'),
    MyZombieTwoShotguns(name='Stop after 2 shotguns'),
    #MyZombieRoll14StopTwoShot(name='Random roll 1 - 4, stop if 2 shotguns'),
    MyZombieMoreShotThanBrain(name='Stop More Shot than Brain')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=10000)
