# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math
import shooter_global_variables

# initialize globals - pos and vel encode vertical info for paddles
LEFT_WALL = 0
TOP_WALL = 0

gravity = [0, 3]
line = [0, 0]
 

WIDTH = shooter_global_variables.WIDTH
HEIGHT = shooter_global_variables.HEIGHT

# number of rows and columns in the tile map
TILE_ROWS = shooter_global_variables.TILE_ROWS
TILE_COLS = shooter_global_variables.TILE_COLS
TILE_DIM = shooter_global_variables.TILE_DIM

class enemy:

    # initialize enemy
    def __init__(self, start_pos, colour, radius):

    # random starting position that is on the edge of the screen, assuming start position is left side of screen
        if random.randrange(0, 100) > 50:
            start_pos[0] = start_pos[0] + 50
            start_pos[1] = start_pos[1] - 50
        else:
            start_pos[0] = start_pos[0] - WIDTH - 50
            start_pos[1] = start_pos[1] - 50

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
                self._offset_[0] = 0.5*speed[0]
        elif goal[0] < self._position_[0]:
            if random.randrange(0,100) > 50:
                self._offset_[0] = -speed[0]
            else:
                self._offset_[0] = -0.5*speed[0]
        
        # vertical
        # if they are on the ground or on a platform then randomly jump
        if (goal[1] < self._position_[1] and self._position_[1] == HEIGHT - 1.25 * TILE_DIM) or self._on_platform_ is True:
            if random.randrange(0, 100) > 90:
                self._offset_[1] = -0.02*speed[1]
                self._on_platform_ = False
            else:
                self._offset_[1] = 0
        elif (self._offset_[1]) < 0 and self._offset_[1] > -0.4*speed[1]:
            self._offset_[1] = self._offset_[1] - 0.25 * speed[1] + gravity[1]

        else:
            self._offset_[1] = gravity[1]

        if self._offset_[1] == 0:
            self._position_[0] = self._position_[0] + self._offset_[0]
        else:
            self._position_[0] = self._position_[0] + 0.25*self._offset_[0]

        self._position_[1] += self._offset_[1]
          
        if self._position_[1] > HEIGHT - 1.25 * TILE_DIM:
            self._position_[1] = HEIGHT - 1.25 * TILE_DIM

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
            # print("enemy collided with platform")
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
        

