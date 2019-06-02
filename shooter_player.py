"""
Classes and functions related to the player
"""
import math
import shooter_global_variables
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#  __      _____ _       _           _
# /_ |    / ____| |     | |         | |
#  | |   | |  __| | ___ | |__   __ _| |___
#  | |   | | |_ | |/ _ \| '_ \ / _` | / __|
#  | |_  | |__| | | (_) | |_) | (_| | \__ \
#  |_(_)  \_____|_|\___/|_.__/ \__,_|_|___/
#
WIDTH = shooter_global_variables.WIDTH
HEIGHT = shooter_global_variables.HEIGHT
# number of rows and columns in the tile map
TILE_ROWS = shooter_global_variables.TILE_ROWS
TILE_COLS = shooter_global_variables.TILE_COLS
TILE_DIM = shooter_global_variables.TILE_DIM

PLAYER_TILEMAP = simplegui._load_local_image("Assets/Tilemaps/Tilemap_player_70x70.png")

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
    def __init__(self, pos, health):
        self._pos_ = [pos[0], pos[1]]
        self._vel_ = [0, 0]
        self._health_ = health
        self._on_platform_ = False
        self._radius_ = 35
        self._move_speed_ = TILE_DIM / 25
        self._jump_vel_ = TILE_DIM / 8.5
        self._tilemap_coord_ = [1, 1]

    def move(self, direction):
        """
        move left/right
        :return:
        """
        if direction == "left":
            print("player move_left")
            self._vel_[0] = -self._move_speed_

        elif direction == "right":
            print("player move_right")
            self._vel_[0] = self._move_speed_

    # movement
    def jump(self):
        """
        player jumps
        :return: None
        """
        if self._on_platform_:
            print("player jumped")
            self._pos_[1] -= 3
            self._vel_[1] -= self._jump_vel_
            self._on_platform_ = False
            self._tilemap_coord_ = [0, 1]

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
            # center_source
            [(self._tilemap_coord_[0] + 0.5) * 70, (self._tilemap_coord_[1] + 0.5) * 70],
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
        self._vel_[1] += TILE_DIM / 300
        # terminal velocity for gravity
        if self._vel_[1] >= self._move_speed_ * 5:
            self._vel_[1] = self._move_speed_ * 5

        # update position based on velocity
        self._pos_[0] += self._vel_[0]
        self._pos_[1] += self._vel_[1]

        # if self._tilemap_coord_[0] == 1:
        #     self._tilemap_coord_[0] = 0
        # elif self._tilemap_coord_[0] == 0:
        #     self._tilemap_coord_[0] = 1

    def collide_platform(self, platform):
        """
        checks collisions with platforms
        :param platform:
        :return: True if player is on platform
        """
        plat_left = platform.get_top_left()
        plat_right = platform.get_top_right()
        # y collision to a tolerance of 3 pixels
        collide_y_down = self._pos_[1] + self._radius_ > (plat_left[1] - 7.5)
        collide_y_up = self._pos_[1] + self._radius_ < (plat_left[1] + 7.5)
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
