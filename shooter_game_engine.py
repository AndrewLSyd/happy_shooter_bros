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

    def move(self, direction):
        """
        move left/right
        :return:
        """
        if direction == "left":
            print("player move_left")
            self._vel_[0] = -self._canvas_width_ / 500
        elif direction == "right":
            print("player move_right")
            self._vel_[0] = self._canvas_width_ / 500

    def stop(self):
        self._vel_[0] = 0

    def draw(self, canvas):
        canvas.draw_circle([self._pos_[0], self._pos_[1]], 12, 20, "red")

    def update(self):
        # gravity with terminal velocity
        self._vel_[1] += self._canvas_height_ / 50000
        if self._vel_[1] >= self._canvas_height_ / 100:
            self._vel_[1] = self._canvas_height_ / 100

        self._pos_[0] += self._vel_[0]
        self._pos_[1] += self._vel_[1]

        # floor
        if self._pos_[1] >= self._canvas_height_:
            self._pos_[1] = self._canvas_height_



