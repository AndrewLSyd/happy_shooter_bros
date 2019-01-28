"""
shooter GUI and input handlers
"""
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import shooter_global_variables

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


# load art assets
BACKGROUND_INFO = shooter_global_variables.ImageInfo([WIDTH // 2, HEIGHT // 2], [WIDTH, HEIGHT])
BACKGROUND_IMAGE = simplegui._load_local_image("Assets/Backgrounds/background-test.png")


class GUI:
    """
    Class to run game GUI.
    """

    def __init__(self, player, platform_group):
        self._frame_ = simplegui.create_frame("Happy Shooter Bros - Engine", WIDTH, HEIGHT)
        self._player_ = player
        self._platform_group_ = platform_group
        self._keydown_inputs_ = {"left": self.move_left, "right": self.move_right, "up": self.jump}
        self._keyup_inputs_ = {"left": self.stop_left, "right": self.stop_right}
        # self._frame_.add_button('New Game', self.start)
        self._frame_.set_draw_handler(self.draw)
        self._frame_.set_keydown_handler(self.keydown_handler)
        self._frame_.set_keyup_handler(self.keyup_handler)
        # self._frame_.set_canvas_background("#BCADA1")
        self._frame_.start()

    # 4. DEFINE EVENT HANDLERS
    # keyboard handlers
    def move_left(self):
        """
        moves player object left
        :return: None
        """
        self._player_.move("left")

    def move_right(self):
        """
        moves player object right
        :return: None
        """
        self._player_.move("right")

    def stop_left(self):
        """
        stops player object left
        :return: None
        """
        self._player_.stop("left")

    def stop_right(self):
        """
        stops player object right
        :return: None
        """
        self._player_.stop("right")

    def jump(self):
        """
        jumps player object
        :return: None
        """
        self._player_.jump()

    def keydown_handler(self, key):
        """

        :param key:
        :return:
        """
        for i in self._keydown_inputs_:
            if key == simplegui.KEY_MAP[i]:
                self._keydown_inputs_[i]()

    def keyup_handler(self, key):
        """

        :param key:
        :return:
        """
        for i in self._keyup_inputs_:
            if key == simplegui.KEY_MAP[i]:
                self._keyup_inputs_[i]()

    def draw(self, canvas):
        """

        :param canvas:
        :return:
        """
        canvas.draw_image(BACKGROUND_IMAGE, BACKGROUND_INFO.get_center(), BACKGROUND_INFO.get_size(), [WIDTH / 2, HEIGHT / 2],
                          [WIDTH, HEIGHT])
        # player
        self._player_.update()
        self._player_.draw(canvas)

        # platforms
        for plat in self._platform_group_:
            self._player_.collide_platform(plat)
            plat.draw(canvas)

    # need change level function
