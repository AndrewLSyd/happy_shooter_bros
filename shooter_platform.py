"""
Classes and functions relating to platforms
"""
#  __      _____ _       _           _
# /_ |    / ____| |     | |         | |
#  | |   | |  __| | ___ | |__   __ _| |___
#  | |   | | |_ | |/ _ \| '_ \ / _` | / __|
#  | |_  | |__| | | (_) | |_) | (_| | \__ \
#  |_(_)  \_____|_|\___/|_.__/ \__,_|_|___/

WIDTH = 1200
HEIGHT = 675
# number of rows and columns in the tile map
TILE_ROWS = 12
TILE_COLS = 20

#  ___      _    _      _                    __                  _   _
# |__ \    | |  | |    | |                  / _|                | | (_)
#    ) |   | |__| | ___| |_ __   ___ _ __  | |_ _   _ _ __   ___| |_ _  ___  _ __  ___
#   / /    |  __  |/ _ \ | '_ \ / _ \ '__| |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  / /_ _  | |  | |  __/ | |_) |  __/ |    | | | |_| | | | | (__| |_| | (_) | | | \__ \
# |____(_) |_|  |_|\___|_| .__/ \___|_|    |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                        | |
#
def create_platforms(plat_map):
    """
    takes in list of platforms and generates platform objects for them all
    :param plat_map: list of platform coordinates
    :return: set of platforms
    """
    platform_group = set()
    for plat in plat_map:
        platform_group.add(Platform([(plat[1] + 1) * HEIGHT // TILE_ROWS, (plat[0] + 1)
                                     * WIDTH // TILE_COLS]))
    return platform_group


#  ____      _____ _
# |___ \    / ____| |
#   __) |  | |    | | __ _ ___ ___  ___  ___
#  |__ <   | |    | |/ _` / __/ __|/ _ \/ __|
#  ___) |  | |____| | (_| \__ \__ \  __/\__ \
# |____(_)  \_____|_|\__,_|___/___/\___||___/
class Platform:
    """
    Platform class.
    pos is the CENTRE of the platform
    TILE_COLS columns by 22.5 rows
    tiled
    """
    def __init__(self, pos):
        # pos is the centre
        self._pos_ = [pos[0], pos[1]]
        # TILE_COLS columns by 22.5 rows
        self._half_side_length_ = WIDTH / TILE_COLS / 2
        # four corners of the platform
        self._top_left_ = [pos[0] - self._half_side_length_, pos[1] - self._half_side_length_]
        self._top_right_ = [pos[0] + self._half_side_length_, pos[1] - self._half_side_length_]
        self._bot_right_ = [pos[0] + self._half_side_length_, pos[1] + self._half_side_length_]
        self._bot_left_ = [pos[0] - self._half_side_length_, pos[1] + self._half_side_length_]

    def draw(self, canvas):
        """
        draws platform object, call in draw handler
        :param canvas:
        :return:
        """
        canvas.draw_polygon([self._top_left_, self._top_right_, self._bot_right_, self._bot_left_],
                            5, "red")
        canvas.draw_text(str(round(self._pos_[1] / HEIGHT * TILE_ROWS - 1)) + ", "
                         + str(round(self._pos_[0] / WIDTH * TILE_COLS - 1)),
                         [self._top_left_[0], self._pos_[1]], 20, "white")

    def get_top_left(self):
        """
        :return: top left coordinates of platform
        """
        return self._top_left_

    def get_top_right(self):
        """
        :return: top left coordinates of platform
        :return:
        """
        return self._top_right_
