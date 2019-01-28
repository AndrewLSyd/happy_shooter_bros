"""
shooter game frame.
"""

import shooter_player
import shooter_platform
import shooter_gui

WIDTH = 1200
HEIGHT = 675

# initialize player
PLAYER = shooter_player.Player([WIDTH // 3, HEIGHT // 5], 100)
# initialise platforms
PLAT_MAP1 = [[8, 6], [8, 7], [8, 8], [8, 9], [8, 10]]
PLATFORM_GROUP = shooter_platform.create_platforms(PLAT_MAP1)

# initialise GUI with player and platform_group object
GUI = shooter_gui.GUI(PLAYER, PLATFORM_GROUP)
