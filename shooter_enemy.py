# Implementation of classic arcade game Pong
import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       

LEFT_WALL = 0
TOP_WALL = 0
BOTTOM_WALL = 400
RIGHT_WALL = 600

gravity = [0, 3]
speed = [10, 20]
offset = [0, 0]
line = [0,0]
 

class enemy:
    
    #initialize enemy 
    def __init__(self, start_pos, colour, power_flag, radius):
        self.position = start_pos
        self.colour = colour
        self._radius_ = 10
        
        if random.randrange(0,100)> 80:
            self.power_flag = 1
        else:
            self.power_flag = 0
    
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
            if random.randrange(0,100) > 20:
                offset[1] = -speed[1]
            else: offset[1]= 0
        else:
            offset[1] = gravity[1]

         
        self.position[0] =self.position[0] + offset[0]
        self.position[1] += offset[1]
          
        if self.position[1] > BOTTOM_WALL:
            self.position[1]  = BOTTOM_WALL
            
    def collide_platform(self, platform):
        """
        checks collisions with platforms
        :param platform:
        :return: True if player is on platform
        """
        plat_left = platform.get_top_left()
        plat_right = platform.get_top_right()
        # y collision to a tolerance of 3 pixels
        collide_y_down = self.position[1] + self._radius_ > (plat_left[1] - 3)
        collide_y_up = self.position[1] + self._radius_ < (plat_left[1] + 3)
        collide_y = collide_y_up and collide_y_down
        # x collision
        collide_x_left = self.position[0] >= plat_left[0]
        collide_x_right = self.position[0] <= plat_right[0]
        collide_x = collide_x_left and collide_x_right

        moving_down = self.offset[1] > 0

        # if player is at the top of the platform, between the left and right corners and \
        # moving down
        if collide_x and collide_y and moving_down:
            print("enemy collided with platform")
            self._on_platform_ = True
            # set vertical vel to 0 and set vertical pos to top of tile
            self.offset[1] = 0
            self.position[1] = plat_left[1] - self._radius_
     
    def draw2(self, canvas):
        
        if self.power_flag == 1:
            ang = math.pi * random.random()
            line_end = [50*math.cos(ang), 50*math.sin(ang)]
            line[0] = self.position[0]+line_end[0]
            line[1] = self.position[1]-line_end[1]
            canvas.draw_line([self.position[0], self.position[1]], [line[0], line[1]], 2, "white")

        canvas.draw_circle(self.position, self._radius_, 1, self.colour)
        
        
colour_list = COLOR_LIST = ["Red", "Green", "Yellow", "Purple"]
enemy_list = []
for i in range(10):
    e = enemy([RIGHT_WALL, BOTTOM_WALL], random.choice(colour_list), 50, 10)
    enemy_list.append(e)
        

def draw(canvas):
    # draw enemy
    for e in enemy_list:
        e.move(player._pos_, speed)
    for e in enemy_list:
        e.draw2(canvas)
