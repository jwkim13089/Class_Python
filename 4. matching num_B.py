## Project Templete (Pong)

# implementation of card game - Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# helper function to initialize globals
def new_game() :
    global card_deck, exposed, exposed_list, unexposed_list, state, turn, card_list
    number_list = [0,1,2,3,4,5,6,7,8,9]
    card_deck = number_list * 2
    random.shuffle(card_deck)
    print(card_deck)
    #exposed에 포함된 리스트는 초록카드가 없어 숫자가 노출된 상태
    exposed = [False]*20
    exposed_list = []
    unexposed_list = []
    for i in range(20,800,40) :
        unexposed_list.append([[i,3],[i,97]])
    card_list = unexposed_list[:]
    state = 0
    turn = 0

# define event handlers
def mouseclick(pos) :
    global exposed, unexposed_list, state, turn, exposed_list
    # add game state logic here
    if state == 2 :
        if exposed[pos[0]//40] != True :
            first = exposed_list[0][0][0]//40
            second = exposed_list[1][0][0]//40
            if card_deck[first] != card_deck[second] :
                unexposed_list.extend(exposed_list)
                k = exposed_list[0][0][0]//40
                t = exposed_list[1][0][0]//40
                exposed[k] = False
                exposed[t] = False
                exposed_list = []
                unexposed_list.remove(card_list[pos[0]//40])
                exposed_list.append(card_list[pos[0]//40])
                exposed[pos[0]//40] = True
            elif card_deck[first] == card_deck[second] : 
                exposed_list = []
                unexposed_list.remove(card_list[pos[0]//40])
                exposed_list.append(card_list[pos[0]//40])
            state = 1


    elif state == 0 or state == 1 :
        if exposed[pos[0]//40] != True :
            unexposed_list.remove(card_list[pos[0]//40])
            exposed_list.append(card_list[pos[0]//40])
            exposed[pos[0]//40] = True
            if state == 0 :
                state = 1
            elif state == 1 :
                state = 2
                turn = turn + 1
                
# cards are logically 50x100 pixels in size    
def draw(canvas) :
    
    #draw number
    num_loc = 5
    for num in card_deck :
        canvas.draw_text(str(num), (num_loc,70), 70, 'White')
        num_loc += 40
        
    #draw card
    for card in unexposed_list :
        canvas.draw_line(card[0],card[1], 35, "green")
        
    label.set_text("Turns =" + str(turn)) 

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