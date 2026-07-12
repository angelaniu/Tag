"""
This class describes the forces and setting of the game 
"""
class Display:
    def __init__(self, display_width, display_height, ground, left_wall, right_wall, gravity, air_resistance, friction):
        """
        Constructs the setting of the game
        display_width: the pixel width of the screen
        display_height: the pixel height of the screen
        display_ground: the y-pixel of the ground
        left_wall: the x-pixel of the left wall
        right_wall: the x-pixel of the right wall
        gravity: force pulling the cube's y-velocity downward 
        air_resistance: force affecting the cube's x-velocity in the air
        friction: force affecting the cube's x-velocity on the ground
        """
        self.width = display_width
        self.height = display_height 
        self.ground = ground
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.gravity = gravity 
        self.air_resistance = air_resistance
        self.friction = friction


