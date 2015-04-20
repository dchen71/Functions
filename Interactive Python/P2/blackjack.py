# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or stand"
score = [0,0]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        card = ""
        for this_card in self.hand:
            card = card +  str(this_card)+ " " 
        return "Hand Contains: " + card	# return a string representation of a hand
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        self.score = 0
        self.ace = 0
        
        for card in self.hand:
            if card.get_rank() == "A":
                if self.score <= 10:
                    self.score += 11
                    self.ace += 1
                else:
                    self.score += 1
            elif card.get_rank() == "J":
                self.score += 10
            elif card.get_rank() == "Q":
                self.score += 10
            elif card.get_rank() == "K":
                self.score += 10
            elif card.get_rank() == "T":
                self.score+=10
            else:
                self.score += int(card.get_rank())

            if self.score > 10 and self.ace > 0:
                self.score -= 10
                self.ace = 0

        return self.score

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        length = len(self.hand)
        for i in range(length):
            self.hand[i].draw(canvas,(pos[0] + (i * 100), pos[1]))

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit in range(4):
            for card in range(13):
                self.deck.append(Card(SUITS[suit],RANKS[card]))
            
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card	# deal a card object from the deck
    
    def __str__(self):
        cards = ""
        for card in self.deck:
            cards = cards + str(card) + " "
        return "Deck contains: " + cards	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, player1, player2, deck

    # your code goes here
    if in_play == True:
        outcome = "You restarted. Auto lose"
    else:
        outcome = "Hit or stand"
    
    deck = Deck()
    deck.shuffle()
    player1 = Hand()
    player2 = Hand()  
    player1.add_card(deck.deal_card())
    player2.add_card(deck.deal_card())
    player1.add_card(deck.deal_card())
    player2.add_card(deck.deal_card())    
    print "Player's " + str(player1)
    print "Deal's " + str(player2)
    
    in_play = True

def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global in_play, outcome, score
    if in_play:
        if player1.get_value() <= 21:
            player1.add_card(deck.deal_card())
        if player1.get_value() > 21:
            outcome = "Player has bust, New deal?"
            print outcome
            score[1] += 1
            in_play = False
    
def stand():
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global in_play, outcome
    if in_play:
        while player2.get_value() <= 17:
            player2.add_card(deck.deal_card())
        if player2.get_value() > 21:
            outcome = "Dealer has bust, New deal?"
            print outcome
            in_play = False
            score[0] += 1
        elif player2.get_value() >= player1.get_value():
            outcome = "Dealer wins"
            print outcome
            in_play = False
            score[1] += 1
        elif player2.get_value() < player1.get_value():
            outcome = "Player wins"
            print outcome
            in_play = False
            score[0] += 1
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    player1.draw(canvas, [50,400])
    player2.draw(canvas, [50,50])
    canvas.draw_text(outcome,(200,250),20,'white')
    canvas.draw_text("BLACKJACK", (10,30),20,'white')
    canvas.draw_text("Player: " + str(score[0]),(10,520),20,"white")
    canvas.draw_text("Dealer: " + str(score[1]),(10,540),20,"white")

    if in_play == True:
        canvas.draw_image(card_back, [CARD_CENTER[0],CARD_CENTER[1]], CARD_SIZE, [86,98], CARD_SIZE)
    
    #86,98
        
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric