# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

LEFT_WALL = 0
TOP_WALL = 0
BOTTOM_WALL = 400
RIGHT_WALL = 600

gravity = [0, 3]
speed = [10, 20]
offset = [0, 0]



class enemy:
    
    #initialize enemy 
    def __init__(self, start_pos, colour):
        self.position = start_pos
        self.colour = colour
    
    #movement
    def move(self, goal, speed):
        
        #horizontal
        if goal[0] > self.position[0]:
            if random.randrange(0,100) > 50:
                offset[0] = speed[0]
            else:
                offset[0] = -0.5*speed[0]
        elif goal[0] < self.position[0]:
            if random.randrange(0,100) > 50:
                offset[0] = -speed[0]
            else:
                offset[0] = 0.5*speed[0]
        
        #vertical
        
        if goal[1] < self.position[1] and self.position[1] == BOTTOM_WALL:
            if random.randrange(0,100) > 40:
                offset[1] = -speed[1]
            elif random.randrange(0, 100) > 20:
                offset[1] = -2*speed[1]
            else: offset[1]= 0
        else:
            offset[1] = gravity[1]

         
        self.position[0] =self.position[0] + offset[0]
        self.position[1] += offset[1]
          
        if self.position[1] > BOTTOM_WALL:
            self.position[1]  = BOTTOM_WALL
   

    def draw2(self, canvas):
        canvas.draw_circle(self.position, 10, 1, self.colour)
        
colour_list = COLOR_LIST = ["Red", "Green", "Blue", "Purple"]
enemy_list = []
for i in range(10):
    e = enemy([RIGHT_WALL, BOTTOM_WALL], random.choice(colour_list))
    enemy_list.append(e)
        
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos =[WIDTH // 2,HEIGHT //2 ]
ball_vel =[0,0]

paddle1_pos = [PAD_WIDTH+20 , HEIGHT//2]
paddle2_pos = [WIDTH - PAD_WIDTH - 20 , HEIGHT//2]

paddle1_vel =[0,0]
paddle2_vel =[0,0]

score1= 0
score2= 0

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH // 2, HEIGHT //2]
    
    if random.randrange(1, 50) < 25:
        direction ="RIGHT"
    else:
        direction = "LEFT"
    
    
    #Initial spawn
    if direction == "RIGHT" :
        x_vel = random.randrange(120, 240) / 60
        y_vel = -random.randrange(60,180) / 60
        ball_vel=[x_vel, y_vel]
    elif direction== "LEFT" :
        x_vel = -random.randrange(120, 240) / 60
        y_vel = -random.randrange(60,180) / 60
        ball_vel=[x_vel, y_vel]
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global ball_pos, ball_vel
    
    score1=0
    score2=0
    paddle1_pos = [PAD_WIDTH+20 , HEIGHT//2]
    paddle2_pos = [WIDTH - PAD_WIDTH - 20 , HEIGHT//2]
    paddle1_vel =[0,0]
    paddle2_vel =[0,0]
    ball_pos =[WIDTH // 2,HEIGHT //2 ]
    ball_vel =[0,0]

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    canvas.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] +PAD_HEIGHT], 1, "White")
    canvas.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] +PAD_HEIGHT], 1, "White")
    
    #score
    canvas.draw_text(str(score1), [WIDTH // 2 - 100, 50], 24, "White")
    canvas.draw_text(str(score2), [WIDTH // 2 + 100, 50], 24, "White")
    
    #Rebounds
    #vertical walls
    if ball_pos[0] < LEFT_WALL + BALL_RADIUS or ball_pos[0] + BALL_RADIUS > RIGHT_WALL:
        ball_vel[0] = -ball_vel[0]
    #horizontal walls
    if ball_pos[1] < TOP_WALL + + BALL_RADIUS or ball_pos[1] + BALL_RADIUS > BOTTOM_WALL:
        ball_vel[1] = -ball_vel[1]
    
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "white")
    
    # update paddle's vertical position, keep paddle on the screen
    #top wall
    
    paddle1_pos[1] = paddle1_pos[1]+paddle1_vel[1]
    
#    if paddle1_pos[1] > TOP_WALL or paddle1_pos[1]>BOTTOM_WALL:
  #      paddle1_pos[1] = paddle1_pos[1]
   
    paddle2_pos[1] = paddle2_pos[1]+paddle2_vel[1]

#    if paddle2_pos[1] < TOP_WALL and paddlew_pos[1]>BOTTOM_WALL:
 #       paddle2_pos[1] = paddle2_pos[1]                                    
         
    
    
    # determine whether paddle and ball collide    
#left paddle
    if (paddle1_pos[0] -5  <= ball_pos[0] and ball_pos[0] <= paddle1_pos[0] +5) and (ball_pos[1] > paddle1_pos[1] and ball_pos[1] < paddle1_pos[1] +PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]
    
#right paddle
    if (paddle2_pos[0] -5 <= ball_pos[0] and ball_pos[0] <= paddle2_pos[0] +5) and (ball_pos[1] > paddle2_pos[1] and ball_pos[1] < paddle2_pos[1] +PAD_HEIGHT):
        ball_vel[0] = -ball_vel[0]



    # draw scores
    if (ball_pos[0] < BALL_RADIUS):
        score1 = score1+1
    elif (ball_pos[0] > WIDTH - BALL_RADIUS):
        score2 = score2+1
        
        
    # draw enemy

    for e in enemy_list:
        e.move(ball_pos, speed)
    
    for e in enemy_list:
        e.draw2(canvas)


        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] -= 3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] += 3
      
    
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] -=  3
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] +=  3    


def keyup(key):
    global paddle1_vel, paddle2_vel

    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] +=  3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] -=  3
      
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] +=  3
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] -=  3

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1= frame.add_button("Spawn Ball", spawn_ball, 100)
button2= frame.add_button("New Game", new_game, 100)


# start frame
new_game()
frame.start()
