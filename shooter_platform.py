"""
Classes and functions relating to platforms
"""
import shooter_global_variables
try:
    import simplegui
except ImportError:
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


# loading platform tilemap
PLATFORM_TILEMAP = simplegui._load_local_image("Assets/Tilemaps/Tilemap_platforms.png")


PLATFORM_INFO = shooter_global_variables.ImageInfo([shooter_global_variables.TILE_DIM // 2,
                                                    shooter_global_variables.TILE_DIM // 2],
                                                   [shooter_global_variables.TILE_DIM,
                                                    shooter_global_variables.TILE_DIM])

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
        platform_group.add(Platform([(plat[1] + 0.5) * TILE_DIM, (plat[0] + 0.5)
                                     * TILE_DIM, plat[2], plat[3]]))
    print("plat[2]:", plat[2])
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
    def __init__(self, pos_tilemap_coord):
        # pos_tilemap_coord is the centre
        self._pos_ = [pos_tilemap_coord[0], pos_tilemap_coord[1]]
        # TILE_COLS columns by 22.5 rows
        self._half_side_length_ = TILE_DIM / 2
        # four corners of the platform
        self._top_left_ = [pos_tilemap_coord[0] - self._half_side_length_, pos_tilemap_coord[1] - self._half_side_length_]
        self._top_right_ = [pos_tilemap_coord[0] + self._half_side_length_, pos_tilemap_coord[1] - self._half_side_length_]
        self._bot_right_ = [pos_tilemap_coord[0] + self._half_side_length_, pos_tilemap_coord[1] + self._half_side_length_]
        self._bot_left_ = [pos_tilemap_coord[0] - self._half_side_length_, pos_tilemap_coord[1] + self._half_side_length_]
        # tilemap coordinates
        self._tilemap_coord = [pos_tilemap_coord[2], pos_tilemap_coord[3]]

    def draw(self, canvas):
        """
        draws platform object, call in draw handler
        :param canvas:
        :return:
        canvas.draw_image(PLATFORM_TILEMAP, BACKGROUND_INFO.get_center(), BACKGROUND_INFO.get_size(), [WIDTH / 2, HEIGHT / 2],
                  [WIDTH, HEIGHT])
        """
        canvas.draw_polygon([self._top_left_, self._top_right_, self._bot_right_, self._bot_left_],
                            3, "red")
        # draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation=0)
        print("self._tilemap_coord[0]", self._tilemap_coord[0])
        print("self._tilemap_coord[1]", self._tilemap_coord[1])
        canvas.draw_image(
            # image
            PLATFORM_TILEMAP,
            # center_source
            [(self._tilemap_coord[0] + 0.5) * shooter_global_variables.TILE_DIM,
             (self._tilemap_coord[1] + 0.5) * shooter_global_variables.TILE_DIM],
            # width_height_source
            [shooter_global_variables.TILE_DIM, shooter_global_variables.TILE_DIM],
            # center_dest
            self._pos_,
            # width_height_dest
            PLATFORM_INFO.get_size())
        canvas.draw_text(str(round(self._pos_[1] / TILE_DIM - 1)) + ", "
                         + str(round(self._pos_[0] / TILE_DIM - 1)),
                         [self._top_left_[0] + TILE_DIM / 3, self._pos_[1]], 20, "white")
        # draw tilemap here

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
