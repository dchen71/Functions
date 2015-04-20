# implementation of card game - Memory

import simplegui
import random



# helper function to initialize globals
def new_game():
    global deck, exposed, num_pos, card_pos,space, flipped, ex_card, turns
    exposed = []
    deck = range(0,8)
    deck2 = range(0,8)
    deck.extend(deck2)
    random.shuffle(deck)
    for i in range(len(deck)):
        exposed.append(False)
    num_pos = [10,80]
    card_pos = [5,10,50,90]
    space=50
    ex_card = [0,0]
    flipped = [False,False]
    turns = 0
    label.set_text("Turns = " + str(turns))
                            
    
# define event handlers
def mouseclick(pos):
    global exposed,card_pos,space, ex_card, flipped, turns,deck
    # add game state logic here
    if(pos[1] < card_pos[3] and pos[1] > card_pos[1]):
        for i in range(0,16):
            if(pos[0] >= card_pos[0] + space*i and pos[0] <= card_pos[0] + space * (i+1)):
                if(flipped[0] == False):
                    if(exposed[i] == False):
                        exposed[i] = True
                        ex_card[0] = i
                        flipped[0] = True
                else:
                    if(flipped[1] == False):
                        if(exposed[i] == False):
                            exposed[i] = True
                            ex_card[1] = i
                            flipped[1] = True
                    else:
                        if(exposed[i] == False):
                            if(deck[ex_card[0]] == deck[ex_card[1]]):
                                exposed[i] = True
                                ex_card[0] = i
                                flipped[1] = False
                                turns += 1
                                label.set_text("Turns = " + str(turns))
                            else:
                                exposed[ex_card[0]] = False
                                exposed[ex_card[1]] = False
                                exposed[i] = True
                                ex_card[0] = i
                                flipped[1] = False
                                turns += 1
                                label.set_text("Turns = " + str(turns))

                                # cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed, num_pos, card_pos, space
    for card in range(len(deck)):
        if(exposed[card] == True):
            canvas.draw_text(str(deck[card]), (num_pos[0]+ card*space,num_pos[1]), 75, "white")
        else:
            canvas.draw_polygon([[card_pos[0]+card*space, card_pos[1]], [card_pos[0]+card*space, card_pos[3]], [card_pos[2]+card*space, card_pos[3]], [card_pos[2]+card*space, card_pos[1]]], 5, 'White','Green')
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric