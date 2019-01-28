"""
shooter game frame.
"""

import shooter_player
import shooter_platform
import shooter_gui
import shooter_enemy.py

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
colour_list = COLOR_LIST = ["Red", "Green", "Yellow", "Purple"]
enemy_speed = [10, 20]
enemy_list = []
for i in range(10):
    e = enemy([RIGHT_WALL, BOTTOM_WALL], random.choice(colour_list), 50, 10)
    enemy_list.append(e)



# initialise GUI with player and platform_group object
GUI = shooter_gui.GUI(PLAYER, PLATFORM_GROUP, enemy_list, enemy_speed)
