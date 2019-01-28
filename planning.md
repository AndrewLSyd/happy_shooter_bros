# Planning file Happy Shooter Brothers!
Tian, Clem and Ondu

# Ideas
* 2D shooter
* One screen per level
* "Teletubbies"

# Canvas
* SCREEN SIZE = 1200 x 675 px
* GRID SIZE = 30 x 30px (40cols x 23rows //NOTE: 23rd row will be truncated by half, due to screen size)

# Object sizes
* PLAYER = 40x60px (20 x 30px photoshop)


# Plan
* Create game engine (use coloured boxes to represent graphics and sprites for now)


# Game file
* shooter_main.py - area where everything comes together
* shooter_player.py
* shooter_enemy.py - enemy classes
* shooter_GUI - GUI is created, called and GUI.draw etc is defined
* shooter_level.py - each level will be an object of "level" class with attributes like map of whgere all the platforms are, enemeies, sprites

# General code structure
(only if applicable)
1. Global
2. Helper
3. Classes
4. Event handlers
5. Create a frame
6. Register event handlers
7. Start frame and timers