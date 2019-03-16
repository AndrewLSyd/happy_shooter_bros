# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math

# initialize globals - pos and vel encode vertical info for paddles
LEFT_WALL = 0
TOP_WALL = 0

gravity = [0, 3]
line = [0, 0]
 

WIDTH = 1200
HEIGHT = 675

class enemy:

    # initialize enemy
    def __init__(self, start_pos, colour, radius):
        self._position_ = start_pos
        self.colour = colour
        self._radius_ = radius
        self._on_platform_ = False
        self._offset_ = [0, 0]
        self._on_platform_ = False
        
        if random.randrange(0, 100) > 80:
            self.power_flag = 1
        else:
            self.power_flag = 0
       
    # movement
    def move(self, goal, speed):
        
        # horizontal
        if goal[0] > self._position_[0]:
            if random.randrange(0,100) > 50:
                self._offset_[0] = speed[0]
            else:
                self._offset_[0] = -0.5*speed[0]
        elif goal[0] < self._position_[0]:
            if random.randrange(0,100) > 50:
                self._offset_[0] = -speed[0]
            else:
                self._offset_[0] = 0.5*speed[0]
        
        # vertical
        #if they are on the ground or on a platform then randomly jump
        if (goal[1] < self._position_[1] and self._position_[1] == HEIGHT) or self._on_platform_ is True:
            if random.randrange(0, 100) > 20:
                self._offset_[1] = -speed[1]
            else:
                self._offset_[1] = 0
        else:
            self._offset_[1] = gravity[1]

        self._position_[0] = self._position_[0] + self._offset_[0]
        self._position_[1] += self._offset_[1]
          
        if self._position_[1] > HEIGHT:
            self._position_[1] = HEIGHT

    def collide_platform(self, platform):
        """
        checks collisions with platforms
        :param platform:
        :return: True if player is on platform
        """
        plat_left = platform.get_top_left()
        plat_right = platform.get_top_right()
        # y collision to a tolerance of 3 pixels
        collide_y_down = self._position_[1] + self._radius_ > (plat_left[1] - 3)
        collide_y_up = self._position_[1] + self._radius_ < (plat_left[1] + 3)
        collide_y = collide_y_up and collide_y_down
        # x collision
        collide_x_left = self._position_[0] >= plat_left[0]
        collide_x_right = self._position_[0] <= plat_right[0]
        collide_x = collide_x_left and collide_x_right

        moving_down = self._offset_[1] > 0

        # if player is at the top of the platform, between the left and right corners and \
        # moving down
        if collide_x and collide_y and moving_down:
            print("enemy collided with platform")
            self._on_platform_ = True
            # set vertical vel to 0 and set vertical pos to top of tile
            self._offset_[1] = 0
            self._position_[1] = plat_left[1] - self._radius_
     
    def draw2(self, canvas):
        
        if self.power_flag == 1:
            ang = math.pi * random.random()
            line_end = [50*math.cos(ang), 50*math.sin(ang)]
            line[0] = self._position_[0] + line_end[0]
            line[1] = self._position_[1] - line_end[1]
            canvas.draw_line([self._position_[0], self._position_[1]], [line[0], line[1]], 2, "white")

        canvas.draw_circle(self._position_, self._radius_, 1, self.colour)
        

