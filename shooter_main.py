"""
shooter game frame.
"""

import shooter_global_variables
import shooter_player
import shooter_platform
import shooter_gui
import shooter_enemy
import random

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
BOTTOM_WALL = 400
RIGHT_WALL = 600

# initialize player
PLAYER = shooter_player.Player([WIDTH // 3, HEIGHT // 5], 100)
# initialise platforms
# position uses "matrix notation of rows/cols"
# [tile pos rows, tile pos cols, tile map x coord, tile map y coord (computing one)]

PLAT_MAP1 = [
    [7, 12, 0, 0], [7, 13, 4, 0]
    , [8, 7, 1, 1], [8, 8, 1, 1], [8, 9, 1, 1], [8, 10, 1, 1]
    , [5, 7, 1, 1], [5, 5, 1, 1], [5, 9, 1, 1], [5, 10, 1, 1]] +\
            [[10, index, 6, 0] for index in range(TILE_COLS)] +\
            [[11, index, 1, 1] for index in range(TILE_COLS)]



PLATFORM_GROUP = shooter_platform.create_platforms(PLAT_MAP1)

# initialize enemy
colour_list = COLOR_LIST = ["Red", "Green", "Yellow", "Purple"]
enemy_speed = [10, 20]
enemy_list = []
for i in range(10):
    e = shooter_enemy.enemy([200, 200], random.choice(colour_list), 10)
    enemy_list.append(e)



# initialise GUI with player and platform_group object
# GUI takes PLAT_TILE_MAP as another argument
GUI = shooter_gui.GUI(PLAYER, PLATFORM_GROUP, enemy_list, enemy_speed)
