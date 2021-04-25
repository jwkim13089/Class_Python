# 'Run' 실행 후 frame의 input_field에 1000보다 작은 숫자를 입력한다. 
# 컴퓨터의 Guessin_number를 보고 higher과 lower중에 버튼을 클릭한다. 
# 다시 새로운 게임을 시작하고 싶을 시에는 new_game 버튼을 누른다.
# 숫자를 입력하면 100보다 작은 숫자인지 100이상, 1000미만인 숫자인지 컴퓨터가 알아서 판단하여 게임을 시작한다.
# smart 버튼은 한번만 사용할 수 있다.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

inp = ''
print('Choose the number')
first = 0
i = 1
j = 1
k = 1

def start100() :
    global Guessing_number,last, i, j
    Guessing_number = random.randint(0,99)
    last = 99
    print(Guessing_number)   
    i = i+1
    j = j+1

    
def start1000() :
    global Guessing_number,last, i, j
    Guessing_number = random.randint(0,999)
    last = 999
    print(Guessing_number)
    i = i+1
    j = j+1


def higher() :
    global Min, Max, i, j, predict
    if i == 2 or j == 2:
        Min = Guessing_number
        Max = last
    Min = Min + 1
    Min = int(Min)
    Max = int(Max)
    predict = random.randint(Min,Max)
    if Mine < predict :
        Max = predict
    elif Mine > predict :
        Min = predict
    print(predict)
    if Mine < 100 :
        if i >= 7 :
            if predict != Mine:
                print('Fail. Try again.')
    elif 100 <= Mine and Mine < 1000 :       
        if j >= 10 : 
            if predict != Mine:
                print('Fail. Try again.')
    if predict == Mine :
        print('Correct!')
    i = i+1
    j = j+1



def lower() :
    global Min, Max, i, j, predict
    if i == 2 or j == 2 :
        Min = first
        Max = Guessing_number
    Max = Max - 1
    Max = int(Max)
    Min = int(Min)
    predict = random.randint(Min,Max)
    if Mine < predict :
        Max = predict
    elif Mine > predict :
        Min = predict
    print(predict)
    if Mine < 100 :
        if i >= 7 :
            if predict != Mine:
                print('Fail. Try again.')
    elif 100 <= Mine and Mine < 1000 :       
        if j >= 10 : 
            if predict != Mine:
                print('Fail. Try again.')
    if predict == Mine :
        print('Correct!')
    i = i+1
    j = j+1

    
def new_game() :
    global i, j, k, first
    print(' ')
    print('Choose the number')
    first = 0
    i = 1
    j = 1
    k = 1
    

def enter(inp) :
    global Mine
    Mine = int(inp)
    choose()
    
    
def choose() :
    global Mine
    if Mine >= 0 and Mine < 100 :
        start100()
    elif Mine >= 100 and Mine <1000 : 
        start1000()
    elif Mine >= 1000 or Mine < 0:
        print('Choose number is less than 1000 among positive integers')
        print('')
        new_game()


def smart() :
    global Max, Min, predict, i, j, Guessing_number,Mine,k
    if k == 1 :
        if i == 2 or j == 2:
            if Guessing_number < Mine :
                Min = Guessing_number
                Max = last
            if Guessing_number > Mine :
                Min = first
                Max = Guessing_number
        if i > 2 :
            if predict < Mine :
                Min = predict
                Min = Min + 1
            elif predict > Mine :
                Max = predict
                Max = Max - 1
        n = Max - Min +1   #n = 숫자 개수
        m = n/2
        predict = Min + m
        print(int(predict))
        if int(predict) == Mine :
            print('Correct!')
        elif Mine < 100 :
            if i >= 7 :
                if predict != Mine:
                    print('Fail. Try again.')
        elif 100 <= Mine and Mine < 1000 :       
            if j >= 10 : 
                if predict != Mine:
                    print('Fail. Try again.')
        if predict < Mine :
            Min = predict
        elif predict > Mine :
            Max = predict
        i = i+1
        j = j+1
        k = k+1
    else : 
        print('You already used it')

    
frame = simplegui.create_frame('Guessing number',300,300)

frame.add_button('new_game',new_game,100)
frame.add_button('higher',higher,100)
frame.add_button('lower',lower,100)
frame.add_button('smart',smart,100)
frame.add_input('Enter number',enter,100)

frame.start()
