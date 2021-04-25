# 좌측 유저는 'S','W' 키를 사용하고, 우측 유저는 '↑','↓' 키를 사용한다.
# 승부가 나지 않고 게임이 지속되면 공의 속도가 빨라진다.
# 게임을 처음부터 시행하려면 Reset 버튼을 누른다.

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0,0]
    ball_vel[0] = random.randrange(2,4)
    ball_vel[1] = random.randrange(1,3)  ## pixels per update (1/60 seconds)
    if direction == RIGHT :
        ball_vel[1] = -ball_vel[1]
    elif direction == LEFT :
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2 
    score1 = 0
    score2 = 0
    paddle1_pos = [PAD_WIDTH/2,HEIGHT/2]
    paddle2_pos = [WIDTH-PAD_WIDTH/2,HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(True)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, direction
 

    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
            
    canvas.draw_circle(ball_pos,BALL_RADIUS,2, 'Black', 'White')
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS :
        ball_vel[1] = -ball_vel[1]
    
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]+PAD_HEIGHT/2],[paddle1_pos[0],paddle1_pos[1]-PAD_HEIGHT/2],PAD_WIDTH,"White")
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]+PAD_HEIGHT/2],[paddle2_pos[0],paddle2_pos[1]-PAD_HEIGHT/2],PAD_WIDTH,"White")
    
    if paddle1_pos[1] < PAD_HEIGHT/2 :
        paddle1_pos[1] = paddle1_pos[1]+20
    elif paddle1_pos[1] > HEIGHT-(PAD_HEIGHT/2) :
        paddle1_pos[1] = paddle1_pos[1]-20
    if paddle2_pos[1] < PAD_HEIGHT/2 :
        paddle2_pos[1] = paddle2_pos[1]+20
    elif paddle2_pos[1] > HEIGHT-(PAD_HEIGHT/2) :
        paddle2_pos[1] = paddle2_pos[1]-20
        
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
        if ball_pos[1] < paddle1_pos[1]+PAD_HEIGHT/2 and ball_pos[1] > paddle1_pos[1]-PAD_HEIGHT/2 :
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0]*(1+1/10)
            ball_vel[1] = ball_vel[1]*(1+1/10)
        else :
            score2 = score2 + 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS) :
        if ball_pos[1] < paddle2_pos[1]+PAD_HEIGHT/2 and ball_pos[1] > paddle2_pos[1]-PAD_HEIGHT/2 :
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0]*(1+1/10)
            ball_vel[1] = ball_vel[1]*(1+1/10)
        else :
            score1 = score1 + 1
            spawn_ball(LEFT)

    
    canvas.draw_text(str(score1), (100,100), 80, 'White')
    canvas.draw_text(str(score2), (400,100), 80, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 10
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -10
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 10
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -10

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)

new_game()
frame.start()