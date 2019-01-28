"""
shooter game frame.
"""

import shooter_player
import shooter_platform
import shooter_gui
import shooter_enemy
import random

WIDTH = 1200
HEIGHT = 675

# initialize player
PLAYER = shooter_player.Player([WIDTH // 3, HEIGHT // 5], 100)
# initialise platforms
PLAT_MAP1 = [
    [7, 12], [7, 13]
    ,[8, 7], [8, 8], [8, 9], [8, 10]]


PLATFORM_GROUP = shooter_platform.create_platforms(PLAT_MAP1)

# initialize enemy
COLOUR_LIST = ["Red", "Green", "Yellow", "Purple"]
ENEMY_SPEED = [10, 20]
ENEMY_LIST = []
for i in range(10):
    e = shooter_enemy.enemy([WIDTH, HEIGHT], random.choice(COLOUR_LIST), 10)
    ENEMY_LIST.append(e)

# initialise GUI with player and platform_group object
GUI = shooter_gui.GUI(PLAYER, PLATFORM_GROUP, ENEMY_LIST, ENEMY_SPEED)
