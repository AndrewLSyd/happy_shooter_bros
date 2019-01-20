"""
shooter game engine.
Has "Player" class with movement methods, shoot methods
"""
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

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
        self._on_ground_ = False
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

    def jump(self):
        if self._on_ground_:
            print("player jumped")
            self._vel_[1] -= self._canvas_height_ / 500

    def stop(self, direction):
        if direction == "left" and self._vel_[0] < 0:
            self._vel_[0] = 0
        elif direction == "right" and self._vel_[0] > 0:
            self._vel_[0] = 0

    def draw(self, canvas):
        canvas.draw_circle([self._pos_[0], self._pos_[1]], self._radius_, 2, "red")

    def update(self):
        # gravity
        self._vel_[1] += self._canvas_height_ / 25000
        # terminal velocity for gravity
        if self._vel_[1] >= self._canvas_height_ / 100:
            self._vel_[1] = self._canvas_height_ / 100

        # update position based on velocity
        self._pos_[0] += self._vel_[0]
        self._pos_[1] += self._vel_[1]

        # check if on ground and update _on_ground_flag
        if self._pos_[1] >= self._canvas_height_ - self._radius_:
            self._on_ground_ = True
        elif self._pos_[1] < self._canvas_height_ - self._radius_:
            self._on_ground_ = False

        # if on ground, then set vertical vel to zero and set position to the floor
        if self._on_ground_:
            self._pos_[1] = self._canvas_height_ - self._radius_
            self._vel_[1] = 0



