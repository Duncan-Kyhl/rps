# import libraries
from random import randint

# create play options
moves = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors',
}

# simulate JavaScript swtich case
def switch(argument):
    moves [= {
        0: 'Rock',
        1: 'Paper',
        2: 'Scissors',
    }]
    print switch.get(argument, "Invalid input")

# if [x] - 1 = x, then player wins, else cp wins

# function to return key for any value
def get_key(val):
    for key, value in moves.items():
         if val == value:
             return key
 
    return "key doesn't exist"



# create play options
o = ['Rock', 'Paper', 'Scissors']

# initialize players 
move = randint(0,2)
cp = moves[move]    # computer
player = ''     # human

# get player's move
player = input('Rock, Paper, or Scissors?')

# evaluate winner
if player == computer:
    print('Tie!')
else if player == 'Rock' 
    if cp == 'Paper'

    if cp == 'Scissors'

else if player == 'Paper' 


else if player == 'Scissors' 



----
Using if/else statemenets:
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]