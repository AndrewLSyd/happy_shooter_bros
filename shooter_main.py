"""
shooter game frame.
"""

import shooter_player
import shooter_platform
import shooter_gui
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


# initialize player
PLAYER = shooter_player.Player([WIDTH // 3, HEIGHT // 5], 100)

# initialise platforms
PLAT_MAP_POS1 = [
    [7, 12], [7, 13]
    ,[8, 7], [8, 8], [8, 9], [8, 10]]

PLAT_TILE_MAP2 = [
    [0, 14], [0, 14]
    ,[0, 14], [0, 0], [0, 0], [0, 0]]


PLATFORM_GROUP = shooter_platform.create_platforms(PLAT_MAP_POS1)

# initialise GUI with player and platform_group object
GUI = shooter_gui.GUI(PLAYER, PLATFORM_GROUP)
