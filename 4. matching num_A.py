## Project Templete (Pong)

# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# helper function to initialize globals
def new_game():
    global card_deck, exposed, unexposed_list
    number_list = [0,1,2,3,4,5,6,7,8,9]
    card_deck = number_list * 2
    random.shuffle(card_deck)
    #exposed에 포함된 리스트는 초록카드가 없어 숫자가 노출된 상태
    exposed = [False]*20
    unexposed_list = []
    for i in range(20,800,40) :
        unexposed_list.append([[i,3],[i,97]])

# define event handlers
def mouseclick(pos):
    # add game state logic here
    print(card_deck[pos[0]//40])
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    #draw number
    num_loc = 5
    for num in card_deck :
        canvas.draw_text(str(num), (num_loc,70), 70, 'White')
        num_loc += 40
        
    #draw card
    for card in unexposed_list:
        canvas.draw_line(card[0],card[1], 35, "green")

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