import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

#bring the card images
CARD_SIZE = (72,95)
CARD_CENTER = (36,48)
CARD_IMAGES = simplegui.load_image("C:\\Users\\jwkim\\Desktop\\uni_class\\Source\\t.png")

CARD_BACK_SIZE  = (72,95)
CARD_BACK_CENTER = (36,48)
CARD_BACK_IMAGES = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

CARD_COLLECTION = simplegui.load_image("C:\\Users\\jwkim\\Desktop\\uni_class\\Source\\all.png")

music = simplegui.load_sound("C:\\Users\\jwkim\\Desktop\\uni_class\\Source\\pro.ogg")

SUITS = ('C', 'S', 'H', 'D', 'JOKER')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')

delay = 0
outcome = ''
outcome_2 = ''

in_play = False
opponent_play = False
me_play = False

class Card :
    def __init__(self,suit,rank) :
        if (suit in SUITS) and (rank in RANKS) :
            self.suit = suit
            self.rank = rank
        else :
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)
    
    def __str__(self) :
        return self.suit + self.rank
    
    def get_suit(self) :
        return self.suit
    
    def get_rank(self) :
        return self.rank
    
    def draw(self, canvas, pos) :
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if SUITS.index(self.suit) == 4 :
            card_loc = (CARD_CENTER[0], CARD_CENTER[1]+ CARD_SIZE[1] * 4)
        canvas.draw_image(CARD_IMAGES, card_loc, CARD_SIZE, [pos[0]+CARD_CENTER[0], pos[1]+CARD_CENTER[1]], CARD_SIZE)
        
        if in_play :
            if pos[1] < 404 :
                canvas.draw_image(CARD_BACK_IMAGES,CARD_BACK_CENTER , CARD_BACK_SIZE ,
                                  [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        

class Hand :
    def __init__(self) :
        self.card_list = []
        
    def __str__(self) :
        new_card_list = ''
        for i in self.card_list :
            new_card_list += str(i) + ' '
        return  new_card_list
     
    def add_card(self, card) :
        self.card_list.append(card)
      
    def lose_card(self,card) :
        if card in self.card_list :
            self.card_list.remove(card)

    def loc(self,loc1):
        list_loc = ''
        loc = int(loc1)
        if len(self.card_list) > loc :
            list_loc = self.card_list[loc]
        return list_loc
    
    def card_len(self) :
        t = len(self.card_list)
        return t
    
    def check(self) :
        card_rank_list = []
        for n in self.card_list :
            number = n.get_rank()
            if n.get_suit() == 'JOKER':
                number = 'JOKER'
            card_rank_list.append(number)
        L = list(set(card_rank_list))
    
        from collections import Counter
        C1 = Counter(card_rank_list)
        C2 = Counter(L)
        diff = C1 - C2
        D = list(diff.elements())
        F = list(set(D))
    
        L = []
    
        for n in F :
            m = card_rank_list.index(n)
            L.append(m)

            o = card_rank_list.index(n,m+1)
            L.append(o)
            
        list_1 = []
        for p in L :
            q = self.card_list[p]
            list_1.append(q)
        for r in list_1 :
            self.card_list.remove(r)

            
        return self.card_list

    def mini_shuffle(self) :
        random.shuffle(self.card_list)
    
    def draw(self, canvas, pos) :
        j = 1
        for k in self.card_list :
            if j == 15 :
                pos[0] = 3
                pos[1] = pos[1] + 100
            k.draw(canvas, pos)
            pos[0] = pos[0] + 75
            j += 1
       
        
class Deck :
    def __init__(self) :
        self.card = []
        for d in SUITS :
            for e in RANKS :
                if d != 'JOKER' :
                    f = Card(d,e)
                    self.card.append(f)
                elif d == 'JOKER' :
                    if e == 'A' :
                        f = Card(d,e)
                        self.card.append(f)

        
    def shuffle(self) :
        random.shuffle(self.card)
        
    def deal_card(self) :
        pop = self.card.pop()
        return pop
        
    def __str__(self) :
        new_card = ''
        for g in self.card :
            new_card += str(g) + ' '
        return new_card
    
        
def deal() :
    global in_play, me_play, opponent_play
    global deck, opponent, me, delay, outcome, outcome_2
    
    
    if in_play == False :
        deck = Deck()
        deck.shuffle()
        
        opponent = Hand()
        me = Hand()
    
        
        for h in range(0,53) :
            if h < 26 :
                o = deck.deal_card()
                opponent.add_card(o)
            elif h >= 26 :
                m = deck.deal_card()
                me.add_card(m)
   
        me.check()
        opponent.check()
        
        me.mini_shuffle()
        opponent.mini_shuffle()
        
        in_play = True
        me_play = True
        opponent_play = False
        outcome = 'my turn'
        outcome_2 =  "Choose a card among the opponent's"

        
    
    
def choose_me(click_pos) : 
    global in_play, me_play, opponent_play
    global opponent, me, choose_loc, outcome, outcome_2
    choose_loc = ''
    if in_play :
        if me_play==True and opponent_play==False :
            if click_pos[0] <= opponent.card_len()*75 and click_pos[1] <= 100:
                if 3 < click_pos[0]%75 < 75 :
                    if 4 < click_pos[1] < 96 :
                        choose_loc = click_pos[0]//75
                        me.add_card(opponent.loc(choose_loc))
                        opponent.lose_card(opponent.loc(choose_loc))
                        me.check()
                        me_play = False
                        opponent_play = True
                        outcome = 'opponent turn'
                        outcome_2 =  "Click the 'opponent's turn' button"
                    elif 104 < click_pos[1] < 200 :
                        choose_loc = (click_pos[0]//75) + 13
                        me.add_card(opponent.loc(choose_loc))
                        opponent.lose_card(opponent.loc(choose_loc))
                        me.check()
                        me.mini_shuffle()
                        opponent.mini_shuffle()
                        me_play = False
                        opponent_play = True
                        outcome = 'opponent turn'
                        outcome_2 =  "Click the 'opponent's turn' button"
                    else : pass
            elif click_pos[0] >= opponent.card_len()*100 :
                pass
        if me.card_len() == 0 or opponent.card_len() == 0 :
            in_play = False
    if in_play == False :
        if me.card_len() > opponent.card_len() :
            outcome = 'Opponent win'
            outcome_2 = 'Please restart the frame'
        elif me.card_len() < opponent.card_len() :
            outcome = 'I win'
            outcome_2 = 'Please restart the frame'
            
    
def choose_opponent() :
    global in_play, me_play, opponent_play
    global opponent, me, choose_random, outcome, outcome_2
    choose_random = ''
    if in_play :
        if opponent_play==True and me_play == False :
            me_card = me.card_len()
            choose_random = random.randint(0,me_card-1)
            opponent.add_card(me.loc(choose_random))
            me.lose_card(me.loc(choose_random))
            opponent.check()
            me.mini_shuffle()
            opponent.mini_shuffle()
            me_play = True
            opponent_play = False
            outcome = "my turn"
            outcome_2 =  "Choose a card among the opponent's"
        if me.card_len() == 0 or opponent.card_len() == 0 :
            in_play = False
    if in_play == False :
        if me.card_len() > opponent.card_len() :
            outcome = 'Opponent win'
            outcome_2 = 'Please restart the frame'
        elif me.card_len() < opponent.card_len() :
            outcome = 'I win'
            outcome_2 = 'Please restart the frame'
        
        

        
def draw(canvas) :
    opponent.draw(canvas, [3,4])
    me.draw(canvas, [3,404])
    canvas.draw_image(CARD_COLLECTION, [291,200], [583,399], [490,280],[291,200])

    canvas.draw_text(outcome, [700,255], 40, 'Black')
    canvas.draw_text(outcome_2, [700,285], 20, 'Black')
    canvas.draw_text('↑ OPPONENT', [15,220], 25, 'Black')
    canvas.draw_text('↓ MINE', [15,380], 25, 'Black')    

# initialization frame
frame = simplegui.create_frame("TRUMP", 1052, 604)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("opponent's turn",choose_opponent, 200)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(choose_me)


# get things rolling
music.play()
deal()

frame.start()