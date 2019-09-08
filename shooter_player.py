"""
Classes and functions related to the player
"""
import math
import shooter_global_variables
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from copy import deepcopy
#  __      _____ _       _           _
# /_ |    / ____| |     | |         | |
#  | |   | |  __| | ___ | |__   __ _| |___
#  | |   | | |_ | |/ _ \| '_ \ / _` | / __|
#  | |_  | |__| | | (_) | |_) | (_| | \__ \
#  |_(_)  \_____|_|\___/|_.__/ \__,_|_|___/
#
# loading global variables
WIDTH = shooter_global_variables.WIDTH
HEIGHT = shooter_global_variables.HEIGHT
# number of rows and columns in the tile map
TILE_ROWS = shooter_global_variables.TILE_ROWS
TILE_COLS = shooter_global_variables.TILE_COLS
TILE_DIM = shooter_global_variables.TILE_DIM

PLATFORM_HIST = []
# set used to hold bullet objects
bullet_group = set([])

# art assets
PLAYER_TILEMAP = simplegui._load_local_image("Assets/Tilemaps/Tilemap_player_70x70.png")
BULLET_IMG = simplegui._load_local_image("Assets/Tilemaps/bullet_1.png")
BULLET_FLIP_IMG = simplegui._load_local_image("Assets/Tilemaps/bullet_1_flipped.png")

#  ___      _    _      _                    __                  _   _
# |__ \    | |  | |    | |                  / _|                | | (_)
#    ) |   | |__| | ___| |_ __   ___ _ __  | |_ _   _ _ __   ___| |_ _  ___  _ __  ___
#   / /    |  __  |/ _ \ | '_ \ / _ \ '__| |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  / /_ _  | |  | |  __/ | |_) |  __/ |    | | | |_| | | | | (__| |_| | (_) | | | \__ \
# |____(_) |_|  |_|\___|_| .__/ \___|_|    |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                        | |
#                        |_|
def dist(coord1, coord2):
    """
    returns the pythagorean distance between two points
    """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


#  ____      _____ _
# |___ \    / ____| |
#   __) |  | |    | | __ _ ___ ___  ___  ___
#  |__ <   | |    | |/ _` / __/ __|/ _ \/ __|
#  ___) |  | |____| | (_| \__ \__ \  __/\__ \
# |____(_)  \_____|_|\__,_|___/___/\___||___/
class Player:
    """
    Player class
    """
    def __init__(self, pos, health, bullet_group):
        global PLATFORM_HIST
        self._pos_ = [pos[0], pos[1]]
        self._vel_ = [0, 0]
        self._health_ = health
        self._on_platform_ = False  # used for collision detection and to determine whether the player can jump
        self._radius_ = 35
        self._move_speed_run = TILE_DIM * 0.1
        self._move_speed_crouch = self._move_speed_run * 0.5
        self._move_speed_ = self._move_speed_run
        self._jump_vel_ = TILE_DIM * 0.2
        self._tilemap_coord_ = [1, 1]       
        self._walk_cycle_pos_ = 0  # integer value between 0 and 100 inclusive representing state in walk cycle
        # tilemap offsets
        self._direction_offset_ = 0
        self._stance_offset_ = 0
        self._crouching_ = False
        self.bullet_group = bullet_group

        PLATFORM_HIST = [deepcopy(self._pos_)]

    def move(self, direction):
        """
        input: direction: 'left' or 'right'
        moves player object left/right        
        """
        if direction == "left":
            # print("player move_left")
            self._vel_[0] = -self._move_speed_
            self._direction_offset_ = 5
            if self._on_platform_:
                self._stance_offset_ = 1


        elif direction == "right":
            # print("player move_right")
            self._vel_[0] = self._move_speed_
            self._direction_offset_ = 0
            if self._on_platform_:
                self._stance_offset_ = 1

    # player shoots a buellet
    def shoot(self):
        crouch_offset = self._crouching_ * 10

        if self._direction_offset_:
            a_bullet = Bullet(deepcopy([self.get_pos()[0] - 25, self.get_pos()[1] + 10 + crouch_offset]), 'left', 1, 1, 10)
        else:
            a_bullet = Bullet(deepcopy([self.get_pos()[0] + 25, self.get_pos()[1] + 10 + crouch_offset]), 'right', 1, 1, 10)
        self.bullet_group.add(a_bullet)

    # movement
    def jump(self):
        """
        player jumps        
        """
        if self._on_platform_:
            # print("player jumped")
            self._pos_[1] -= 3
            self._vel_[1] -= self._jump_vel_
            self._on_platform_ = False
            self._tilemap_coord_ = [0, 1]
            self._stance_offset_ = 4
            self._walk_cycle_pos_ = 0

    def stop(self, direction):
        """
        stops player horizontal movements
        :param direction:
        :return: None
        """
        if direction == "left" and self._vel_[0] < 0:
            self._vel_[0] = 0
        elif direction == "right" and self._vel_[0] > 0:
            self._vel_[0] = 0
        if self._on_platform_:
            self._stance_offset_ = 0

    def crouch(self):
        """
        crouches player
        """
        self._crouching_ = True
        self._move_speed_ = self._move_speed_crouch
        # print("player crouched")

    def stop_crouch(self):
        """
        crouches player
        """
        self._crouching_ = False
        self._move_speed_ = self._move_speed_run
        # print("player stopped crouching")

    # drawing and updating
    def draw(self, canvas):
        """
        player draw method. draw handler to call this method to draw player
        :param canvas:
        :return: None
        """
        canvas.draw_image(
            # image
            PLAYER_TILEMAP,
            # center_source, rows then columns           
            [(0.5 + self._walk_cycle_pos_ // 50) * 70, (0.5 + self._direction_offset_ + self._stance_offset_) * 70],
            # width_height_source
            [70, 70],
            # center_dest
            self._pos_,
            # width_height_dest
            [70, 70])
        canvas.draw_circle([self._pos_[0], self._pos_[1]], self._radius_, 2, "red")
        

    def update(self):
        """
        updates player position
        :return: None
        """
        # gravity
        self._vel_[1] += TILE_DIM * shooter_global_variables.GRAVITY / 100
        # terminal velocity for gravity
        if self._vel_[1] >= self._move_speed_ * 5:
            self._vel_[1] = self._move_speed_ * 5

        # update position based on velocity
        self._pos_[0] += self._vel_[0]
        self._pos_[1] += self._vel_[1]

        # when in the air
        if not self._on_platform_:
            self._stance_offset_ = 4
            self._walk_cycle_pos_ = 0
            self._move_speed_ = self._move_speed_run
            if self._vel_[0] > 0 and self._on_platform_:
                self._vel_[0] = self._move_speed_
            elif self._vel_[0] < 0 and self._on_platform_:
                self._vel_[0] = -self._move_speed_          
        
        # otherwise when on a platform
        elif self._on_platform_:
            if self._crouching_:
                self._move_speed_ = self._move_speed_crouch
                if self._vel_[0] > 0 and self._on_platform_:
                    self._vel_[0] = self._move_speed_
                elif self._vel_[0] < 0 and self._on_platform_:
                    self._vel_[0] = -self._move_speed_          
            
            if self._vel_[0] == 0:
                self._stance_offset_ = 0
            else:
                self._stance_offset_ = 1        
        
        if self._crouching_:
            self._stance_offset_ = 3
            
        # if moving update walk cycle
        if abs(self._vel_[0]) > 0:            
            self._walk_cycle_pos_ = (self._walk_cycle_pos_ + 15) % 100
            # update speed for crouched movement
            if self._vel_[0] > 0 and self._on_platform_:
                self._vel_[0] = self._move_speed_
            elif self._vel_[0] < 0 and self._on_platform_:
                self._vel_[0] = -self._move_speed_          

    def collide_platform(self, platform):
        """
        checks collisions with platforms
        :param platform:
        :return: True if player is on platform
        """
        plat_left = platform.get_top_left()
        plat_right = platform.get_top_right()
        # y collision to a tolerance of 3 pixels
        collide_y_down = self._pos_[1] + self._radius_ > (plat_left[1] - max(2.5, 0.5 * abs(self._vel_[1])))
        collide_y_up = self._pos_[1] + self._radius_ < (plat_left[1] + max(2.5, 0.5 * abs(self._vel_[1])))
        collide_y = collide_y_up and collide_y_down
        # x collision
        collide_x_left = self._pos_[0] >= plat_left[0]
        collide_x_right = self._pos_[0] <= plat_right[0]
        collide_x = collide_x_left and collide_x_right
        moving_down = self._vel_[1] > 0

        # if player is at the top of the platform, between the left and right corners and \
        # moving down
        if collide_x and collide_y and moving_down:
            # print("player collided with platform")
            self._on_platform_ = True
            # set vertical vel to 0 and set vertical pos to top of tile
            self._vel_[1] = 0
            self._pos_[1] = plat_left[1] - self._radius_
            self._tilemap_coord_ = [0, 0]

            if self._pos_[1] != PLATFORM_HIST[-1][1]:
                PLATFORM_HIST.append(deepcopy(self._pos_))
                # print("LIST APPENDED", PLATFORM_HIST)

    # getters and setters
    def set_pos(self, pos):
        """
        sets positions of player object
        """
        self._pos_ = pos

    def set_vel(self, vel):
        """
        sets velocity of player object
        :param vel:
        :return:
        """
        self._vel_[0] = vel[0]
        self._vel_[1] = vel[1]

    def get_pos(self):
        """
        gets positions of player object
        """
        return self._pos_

class Bullet:
    """
    Bullet class
    """
    def __init__(self, pos, direction, age, lifespan, radius):
        self._pos_ = pos     
        self._direction_ = direction   
        self._age_ = age
        self._life_span_ = lifespan
        self._radius_ = radius
        self._vel_ = 25

    def update(self):
        """
        updates for the bullet: decrement lifespan
        """
        self._age_ += 1

        # update position based on velocity
        if self._direction_ == "right":
            self._pos_[0] += self._vel_     
        else:
            self._pos_[0] -= self._vel_     


    def draw(self, canvas):
        """
        player draw method. draw handler to call this method to draw player
        :param canvas:
        :return: None
        """        
        if self._direction_ == "right":
            canvas.draw_image(
                # image
                BULLET_IMG,
                # center_source, rows then columns           
                [16, 8],
                # width_height_source
                [32, 16],
                # center_dest
                self._pos_,
                # width_height_dest
                [32, 16])
        else:
            canvas.draw_image(
                # image
                BULLET_FLIP_IMG,
                # center_source, rows then columns           
                [16, 8],
                # width_height_source
                [32, 16],
                # center_dest
                self._pos_,
                # width_height_dest
                [32, 16])

        canvas.draw_circle([self._pos_[0], self._pos_[1]], self._radius_, 2, "red")
        