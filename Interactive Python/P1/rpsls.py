# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if(name == 'rock'):
        answer = 0
    elif(name == 'Spock'):
        answer = 1
    elif(name == 'paper'):
        answer = 2
    elif(name == 'lizard'):
        answer = 3
    elif(name == 'scissors'):
        answer = 4
    else: #default rock
        answer = 0
    return answer


def number_to_name(number):
    if(number == 0):
        answer = 'rock'
    elif(number == 1):
        answer = 'Spock'
    elif(number == 2):
        answer = 'paper'
    elif(number == 3):
        answer = 'lizard'
    elif(number == 4):
        answer = 'scissors'
    else: #default rock
        answer = 'rock'
    return answer
    

def rpsls(player_choice): 
    print( "Player chooses " + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5,1)
    comp_choice = number_to_name(comp_number)
    print( "Computer chooses " + comp_choice)
    result = (comp_number - player_number)%5
    if(result == 0):
        print( 'Draw')
    elif(result == 1):
        print( 'Computer wins!')
    elif(result == 2):
        print( 'Computer wins!')
    elif(result == 3):
        print( 'Player wins!')
    else:
        print( 'Player wins!')
    print( "")
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


