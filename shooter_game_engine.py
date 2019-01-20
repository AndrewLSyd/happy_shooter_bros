"""
shooter game engine.

Contains:
"Player" class with movement methods, shoot methods
"Platform" class
"""
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math


#  ___      _    _      _                    __                  _   _
# |__ \    | |  | |    | |                  / _|                | | (_)
#    ) |   | |__| | ___| |_ __   ___ _ __  | |_ _   _ _ __   ___| |_ _  ___  _ __  ___
#   / /    |  __  |/ _ \ | '_ \ / _ \ '__| |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  / /_ _  | |  | |  __/ | |_) |  __/ |    | | | |_| | | | | (__| |_| | (_) | | | \__ \
# |____(_) |_|  |_|\___|_| .__/ \___|_|    |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                        | |
#                        |_|
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


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
    def __init__(self, canvas_width, canvas_height, pos, health):
        self._canvas_width_ = canvas_width
        self._canvas_height_ = canvas_height
        self._pos_ = [pos[0], pos[1]]
        self._vel_ = [0, 0]
        self._health_ = health
        self._on_platform_ = False
        self._radius_ = canvas_width / 100
        self._move_speed_ = self._canvas_width_ / 500

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
        if self._on_platform_:
            print("player jumped")
            self._pos_[1] -= 3
            self._vel_[1] -= self._canvas_height_ / 500
            self._on_platform_ = False

    def stop(self, direction):
        if direction == "left" and self._vel_[0] < 0:
            self._vel_[0] = 0
        elif direction == "right" and self._vel_[0] > 0:
            self._vel_[0] = 0

    # drawing and updating
    def draw(self, canvas):
        canvas.draw_circle([self._pos_[0], self._pos_[1]], self._radius_, 2, "red")

    def update(self):
        # gravity
        self._vel_[1] += self._canvas_height_ / 25000
        # terminal velocity for gravity
        if self._vel_[1] >= self._move_speed_ * 5:
            self._vel_[1] = self._move_speed_ * 5

        # update position based on velocity
        self._pos_[0] += self._vel_[0]
        self._pos_[1] += self._vel_[1]

    def collide_platform(self, platform):
        plat_left = platform.get_top_left()
        plat_right = platform.get_top_right()
        # print("checking collision")
        # if player is at the top of the platform, between the left and right corners with a tolerance of 2.5 pixels
        if (self._pos_[1] + self._radius_ > (plat_left[1] - 1.5) and self._pos_[1] + self._radius_ < (plat_left[1] + 1.5)) and self._pos_[0] >= plat_left[0] and self._pos_[0] <= plat_right[0]:
            print("player collided with platform")
            self._on_platform_ = True
            # set vertical vel to 0 and set vertical pos to top of tile
            self._vel_[1] = 0
            self._pos_[1] = plat_left[1] - self._radius_


class Platform:
    """
    Platform class.
    pos is the CENTRE of the platform
    40 columns by 22.5 rows
    tiled
    """
    def __init__(self, canvas_width, canvas_height, pos):
        self._canvas_width_ = canvas_width
        self._canvas_height_ = canvas_height
        # pos is the centre
        self._pos_ = [pos[0], pos[1]]
        # 40 columns by 22.5 rows
        self._half_side_length_ = canvas_width / 40 / 2
        # four corners of the platform
        self._top_left_ = [pos[0] - self._half_side_length_, pos[1] - self._half_side_length_]
        self._top_right_ = [pos[0] + self._half_side_length_, pos[1] - self._half_side_length_]
        self._bot_right_ = [pos[0] + self._half_side_length_, pos[1] + self._half_side_length_]
        self._bot_left_ = [pos[0] - self._half_side_length_, pos[1] + self._half_side_length_]

    def draw(self, canvas):
        canvas.draw_polygon([self._top_left_, self._top_right_, self._bot_right_, self._bot_left_],
                            5, "red")

    def get_top_left(self):
        return self._top_left_

    def get_top_right(self):
        return self._top_right_

