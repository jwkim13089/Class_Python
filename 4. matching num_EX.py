# Mini_Project_5:  Memory
#학번: 20181151      성명: 김지원
#### 제출기한: 2019년 5월 8일 11시 59분
#### 주의사항: 과제 A 와 과제 B 모두 완성해서 제출하여야 함.
## 완성된 프로그램 Demo - Web
## simple state example for Memory

'''
###  프로젝트 요구사항 설명서 (Memory)
매 단계마다 요구사항을 코딩한 후, 프로그램을 실행하여 요구사항이 잘 코딩 되었는지 확인하여야 한다. 

**1 단계:** <br>
[0,9] 까지의 리스트 두개를 만든 후, 이 둘을 결합하여 하나의 리스트 <span style="color:red">card_deck</span>을 만들라.

**2 단계:** <br>
<span style="color:red">for</span> loop 와 <span style="color:red">draw_text</span> 를 이용하여 <span style="color:red">card_deck </span>에 있는 숫자들을 canvas 에 일정한 간격으로 그려라.

**3 단계:**<br>
<span style="color:red">random.shuffle( )</span> 을 이용하여 <span style="color:red">deck</span> 에 있는 카드를 섞어라..

**4 단계:** <br>
녹색 사각형 이나 카드의 숫자가 그려지도록 코드를 수정하라.<br>
<span style="color:red">exposed</span> 라는 리스트를 만들어, i번째 카드의 숫자가 보이면 True, 보이지 않으면 False 가 되도록 하라.

**5 단계:** <br>
마우스로 클릭한 카드가 어떤 어떤 카드인지를 결정하는 기능을 코딩하자.<br>
마우스를 클릭할 때 마우스의 위치를 알려주는 event handler를 추가하여, 클릭한 카드를 인쇄하라.<br>

**6 단계:** <br>
마우스로 클릭한 위치에 있는 카드가 보이도록 아래와 같이 코딩하라.<br>
만일 마우스로 클릭한 위치의 카드가 i 번째 카드라면, <span style="color:red">exposed[ i ]</span> 는 <span style="color:red">False</span> 에서 <span style="color:red">True</span> 로 바꾸라.<br>
그러나, 만일 그 카드가 이미 <span style="color:red">True</span> 라면, 마우스 클릭을 무시하라.

**7 단계:** <span style="color:red">mouseclick</span><br>
mouse click handler에 게임 로직을 추가할 차례이다.<br>
앞에서 설명한 example code를 참고하여, 두 개의 카드를 선택하여 이들이 일치하는지를 체크한다.<br>
state 0은 게임의 시작 단계이다.<br>
state 0에서, 만일 unexposed 카드를 클릭하여 그 카드가 exposed 되면, state 1 이된다.
따라서, state 1 이란, 쌍을 이루지 못한 카드 하나만 노출된 상태이다.
state 1 에서, 만일 unexposed 카드를 클릭하여 그 카드가 exposed 되면, state 2 가 된다.
state 2 에서, 만일 unexposed 카드를 클릭하여 그 카드가 exposed 되면, state 1 이 된다.

**8 단계:** <br>
state 2 에서, 두 카드의 값이 일치하는지를 체크하여야 한다.<br>
만일 두 카드가 일치하지 않으면, state 1 으로 가기 전에 카드를 보이지 않도록 뒤집어야 한다.<br>
가장 최근에 exposed 된 두 카드의 index를 저장하는 두개의 global variable을 사용하라.

**9 단계:**<br>
카드를 몇 쌍 뒤집었는지를 세는 counter를 추가하라.<br>
<span style="color:red">set_text</span>를 사용하여 컨트롤 판넬에 있는 label에 있는 이 counter를 업데이트 하라.

**10 단계:** <br>
Reset 버튼을 누르면, 카드를 reshuffle 하고, counter를 reset 하고, 게임을 시작하도록, <span style="color:red">new_game</span> 을 수정하라.
'''

# simple state example for Memory

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
     
# define event handlers
def new_game():
    global state
    state = 0
    
def buttonclick():
    global state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1
                         
def draw(canvas):
    canvas.draw_text(str(state) + " card exposed", [30, 62], 24, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory states", 200, 100)
frame.add_button("Restart", new_game, 200)
frame.add_button("Simulate mouse click", buttonclick, 200)


# register event handlers
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
