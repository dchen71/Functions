# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

num_Range = 100
num_Guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_Guesses
    secret_number = random.randrange(0, num_Range)
    if num_Range == 100:
        num_Guesses = 7
    elif num_Range == 1000:
        num_Guesses = 10

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_Range
    num_Range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_Range
    num_Range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    global num_Guesses
    if num_Guesses > 0:
        num_Guesses -= 1
        if guess == secret_number:
            print "Correct!"
            new_game()
        elif guess > secret_number:
              print "Lower!"
        else:
             print "Higher!"
    else:
        print "You ran out of guesses.  The number was " + str(secret_number)
        new_game()
    
# create frame
f = simplegui.create_frame('Guess', 300,300)

# register event handlers for control elements and start frame
f.add_input('Guess', input_guess,50)
button1 = f.add_button('New game', new_game)
button2 = f.add_button('Range 0-100', range100)
button3 = f.add_button('Range 0-1000', range1000)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
