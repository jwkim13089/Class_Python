# 카드 숫자의 합이 21에 가까운 수를 만드는 사람이 이기며 21이 초과하면 지는 게임
# K, Q, J 는 10으로 계산

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
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
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
score = 0

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if in_play :
            if pos == [100,200] :
                 canvas.draw_image(card_back,CARD_BACK_CENTER , CARD_BACK_SIZE ,
                                   [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            else :
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else :
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        new_card_list = ''
        for c in self.card_list :
            #new_card_list += c.get_suit() + c.get_rank() + ' '
            new_card_list += str(c) + ' '
        return 'Hand contains' + new_card_list

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        total_values = 0
        A_check = []
        for i in self.card_list :
            number = i.get_rank()
            A_check.append(number)
            card_values = VALUES[number]
            total_values = total_values + int(card_values)
            
        if  'A' not in A_check :
            return total_values
        else:
            if total_values + 10 <= 21:
                return total_values + 10
            else:
                return total_values
   
    def draw(self, canvas, pos):
        for j in self.card_list :
            j.draw(canvas, pos)
            pos[0] = pos[0] + 100
    
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.card = []
        for i in SUITS :
            for j in RANKS :
                c =  Card(i,j)
                self.card.append(c)

    def shuffle(self):
        random.shuffle(self.card)

    def deal_card(self):
        pop = self.card.pop()
        return pop
    
    def __str__(self):
        new_card = ''
        for k in self.card :
            new_card += str(k) + ' '
        return new_card



#define event handlers for buttons
def deal():
    global outcome, in_play, plus_outcome, score
    global deck, player, dealer

    if in_play :
        plus_outcome = 'Player lost the round.'
        score = score - 1
        
    if True :
        
        deck = Deck()
        deck.shuffle()
    
        dealer = Hand()
        player = Hand()
        
        outcome = ''
        plus_outcome = 'Hit or stand?'
    
        for i in range(0,4) :
            if i <= 1 :
                d = deck.deal_card()
                dealer.add_card(d)
            elif i >= 2 :
                p = deck.deal_card()
                player.add_card(p)
            i = i+1
        in_play = True
        

def hit():
    global in_play, outcome, plus_outcome ,score
    if in_play :
        add_player = deck.deal_card()
        player.add_card(add_player)
        player_value = player.get_value()
        if player_value > 21 :
            outcome = "You have busted"
            plus_outcome = 'New deal?'
            score = score - 1
            in_play = False
    
       
def stand():
    global in_play, outcome, plus_outcome ,score
    if in_play :
        player_value = player.get_value()
        if player_value > 21 :
            outcome = "You have busted"
            plus_outcome = 'New deal?'
            score = score - 1
            in_play = False
        elif player_value <= 21 :
            
            dealer_value = dealer.get_value()
            while dealer_value < 17 :
                add_dealer = deck.deal_card()
                dealer.add_card(add_dealer)
                dealer_value = dealer.get_value()
                
            if dealer_value > 21 :
                outcome = "Dealer have busted"
                plus_outcome = 'New deal?'
                score = score + 1
                in_play = False
            elif dealer_value <= 21 :
                if player_value <= dealer_value :
                    outcome = "dealer win"
                    plus_outcome = 'New deal?'
                    score = score - 1
                    in_play = False
                elif player_value > dealer_value :
                    outcome = "player win"
                    plus_outcome = 'New deal?'
                    score = score + 1
                    in_play = False
        

# draw handler    
def draw(canvas):
    #draw card
    dealer.draw(canvas,[100,200])
    player.draw(canvas,[100,400])
    #draw text
    canvas.draw_text('Blackjack', [100,100], 50, 'Black')
    canvas.draw_text(outcome, [300,150], 30, 'Black')
    canvas.draw_text(plus_outcome, [300,350], 30, 'Black')
    canvas.draw_text('Dealer', [100,150], 30, 'Black')
    canvas.draw_text('Player', [100,350], 30, 'Black')
    canvas.draw_text('Score : '+str(score), [400,100], 30, 'Black')
    
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
    
