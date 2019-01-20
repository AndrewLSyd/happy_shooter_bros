"""
shooter game frame.
Creates a Player class and starts the frame
"""

import shooter_game_engine
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

WIDTH = 1200
HEIGHT = 675


# initialize player
player = shooter_game_engine.Player(WIDTH, HEIGHT, [WIDTH // 2, HEIGHT // 5], 100)

#  _  _     _____        __   ______               _     _    _                 _ _
# | || |   |  __ \      / _| |  ____|             | |   | |  | |               | | |
# | || |_  | |  | | ___| |_  | |____   _____ _ __ | |_  | |__| | __ _ _ __   __| | | ___ _ __ ___
# |__   _| | |  | |/ _ \  _| |  __\ \ / / _ \ '_ \| __| |  __  |/ _` | '_ \ / _` | |/ _ \ '__/ __|
#    | |_  | |__| |  __/ |   | |___\ V /  __/ | | | |_  | |  | | (_| | | | | (_| | |  __/ |  \__ \
#    |_(_) |_____/ \___|_|   |______\_/ \___|_| |_|\__| |_|  |_|\__,_|_| |_|\__,_|_|\___|_|  |___/


def draw(canvas):
    player.draw(canvas)
    player.update()


def move_left():
    player.move("left")


def move_right():
    player.move("right")


def stop_left():
    player.stop("left")


def stop_right():
    player.stop("right")


def jump():
    player.jump()


# keyboard handler
keydown_inputs = {"left": move_left, "right": move_right, "up": jump}
keyup_inputs = {"left": stop_left, "right": stop_right}


def keydown_handler(key):
    for i in keydown_inputs:
        if key == simplegui.KEY_MAP[i]:
            keydown_inputs[i]()


def keyup_handler(key):
    for i in keyup_inputs:
        if key == simplegui.KEY_MAP[i]:
            keyup_inputs[i]()


#  _____    _____       _ _   _       _ _            ______
# | ____|  |_   _|     (_) | (_)     | (_)          |  ____|
# | |__      | |  _ __  _| |_ _  __ _| |_ ___  ___  | |__ _ __ __ _ _ __ ___   ___
# |___ \     | | | '_ \| | __| |/ _` | | / __|/ _ \ |  __| '__/ _` | '_ ` _ \ / _ \
#  ___) |   _| |_| | | | | |_| | (_| | | \__ \  __/ | |  | | | (_| | | | | | |  __/
# |____(_) |_____|_| |_|_|\__|_|\__,_|_|_|___/\___| |_|  |_|  \__,_|_| |_| |_|\___|
frame = simplegui.create_frame("Happy Shooter Bros - Engine", WIDTH, HEIGHT)
frame.add_label("Welcome to Happy Shooter Bros!!")

#    __     _____            _     _              ______               _
#   / /    |  __ \          (_)   | |            |  ____|             | |
#  / /_    | |__) |___  __ _ _ ___| |_ ___ _ __  | |____   _____ _ __ | |_
# | '_ \   |  _  // _ \/ _` | / __| __/ _ \ '__| |  __\ \ / / _ \ '_ \| __|
# | (_) |  | | \ \  __/ (_| | \__ \ ||  __/ |    | |___\ V /  __/ | | | |_
#  \___(_) |_|  \_\___|\__, |_|___/\__\___|_|    |______\_/ \___|_| |_|\__|
#          | |  | |     __/ |     | | |
#          | |__| | __ |___/_   __| | | ___ _ __ ___
#          |  __  |/ _` | '_ \ / _` | |/ _ \ '__/ __|
#          | |  | | (_| | | | | (_| | |  __/ |  \__ \
#          |_|  |_|\__,_|_| |_|\__,_|_|\___|_|  |___/

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)


#  ______    _____ _             _      __
# |____  |  / ____| |           | |    / _|
#     / /  | (___ | |_ __ _ _ __| |_  | |_ _ __ __ _ _ __ ___   ___
#    / /    \___ \| __/ _` | '__| __| |  _| '__/ _` | '_ ` _ \ / _ \
#   / /     ____) | || (_| | |  | |_  | | | | | (_| | | | | | |  __/
#  /_(_)   |_____/ \__\__,_|_|  _\__| |_| |_|  \__,_|_| |_| |_|\___|
#                          | | | | (_)
#            __ _ _ __   __| | | |_ _ _ __ ___   ___ _ __ ___
#           / _` | '_ \ / _` | | __| | '_ ` _ \ / _ \ '__/ __|
#          | (_| | | | | (_| | | |_| | | | | | |  __/ |  \__ \
#           \__,_|_| |_|\__,_|  \__|_|_| |_| |_|\___|_|  |___/

frame.start()
