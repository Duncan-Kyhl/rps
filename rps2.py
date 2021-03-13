
# Rock Paper Scissors

r = 'Rock'
p = 'Paper'
s = 'Scissors'

# computer select move
myList = [r, p, s]

import random

cpMove = random.randint(0,2)

# user input move

userMove = input('Rock, Paper, or Scissors?: ')

if userMove == 'Rock':
    userMove = 0
elif userMove == 'Paper':
    userMove = 1
elif userMove == 'Scissors':
    userMove = 2
else:
    print('Please enter a valid move.')

# compare and print moves to find winner
print(myList[cpMove])
print(myList[userMove])


if cpMove == userMove:
    print('tie! Play again?')
elif cpMove == 0:
    if userMove == 1:
        print('User wins!')
    if userMove == 2:
        print('Computer wins!')
elif cpMove == 1:
    if userMove == 0:
        print('Computer Wins!')
    if userMove == 2:
        print('User Wins')
elif cpMove == 2:
    if userMove == 1:
        print('Computer Wins!')
    if userMove == 0:
        print('User Wins')

# play again

#play = input('Would you like to play again?')
