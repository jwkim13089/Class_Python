# Start 버튼을 누르면 스톱워치가 실행된다.
# Stop 버튼을 누르면 스톱워치가 멈춘다.
# milli second 단위가 0에서 멈추면 score가 올라간다.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width = 800
height = 500
unit = 100
watch = '00:00.0'
size = 100
t = ''
x = 0
y = 0
total = str(x) + '/' + str(y)
integer = int(0)
stopwatch = 0
millisecond = 0

def format(t):
    global minute, second, millisecond, watch, size
    if minute < 10 :
        minute = str(minute)
        minute = '0' + minute
    elif minute >= 10 : 
        timer.stop()
        size = 75
        watch = 'Time over'
    else :
        minute = str(minute)
    if second < 10 :
        second = str(second)
        second = '0' + second
    else :
        second = str(second)
    millisecond = str(millisecond)
    minute = minute + ':'
    second = second + '.'
    watch = minute + second + millisecond
       
def start() : 
    global stopwatch
    stopwatch = 0
    timer.start()
    
def stop() :
    global total, x, y, stopwatch
    if stopwatch == 0 :
        y = y + 1
        if int(millisecond) == 0 :
            x = x + 1
        total = str(x) + '/' + str(y)
        timer.stop()
    stopwatch = stopwatch + 1
    
def reset() :
    global size, integer, watch, x, y, stopwatch,total, millisecond
    timer.stop()
    size = 100
    integer = 0
    watch = '00:00.0'
    x = 0
    y = 0
    stopwatch = 0
    millisecond = 0
    total = str(x) + '/' + str(y)
    
def create_timer() :
    global minute, second, millisecond, integer
    integer = int(integer)
    if integer < 10 :
        minute = 0
        second = 0
        millisecond = integer
    elif integer >= 10 and integer < 60 :
        minute = 0
        second = integer//10
        millisecond = integer%10
    elif integer >= 60 :
        minute = integer//600
        second = (integer%600)//10
        millisecond = (integer%600)%10
    integer = integer + 1
    format(t)
    
def draw_timer(canvas) : 
    canvas.draw_text(watch, (250, 280), size, 'White')
    canvas.draw_text(total, (650,100), 50, 'Red')

frame = simplegui.create_frame("Stopwatch: The Game", width, height)

frame.set_draw_handler(draw_timer)
timer = simplegui.create_timer(unit, create_timer)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.start()