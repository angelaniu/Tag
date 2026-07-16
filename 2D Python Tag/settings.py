"""
This class describes the forces and setting of the game 
"""
BLACK = (0, 0, 0)
import pygame
class Settings:
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
    
class Graphic_Helper:
    @staticmethod
    def insert_medium_txt(str_msg, x, y, screen, font, font_size, text_color):
        # Initialize font 
        font = pygame.font.SysFont(
            name = font,
            size = font_size,
            bold = False
        )
        # Write message 
        text = font.render(
            str_msg,
            True,
            text_color
        )
        # Display message
        screen.blit(text, (x,y))

    @staticmethod
    def rect_with_msg(str_msg, x, y, width, length, screen, bg_color, font, font_size, text_color):
        # Create rectangle to put text on top of 
        rect = pygame.Rect(x, y, width, length)
        pygame.draw.rect (
            surface = screen,
            color = bg_color,
            rect = rect,
            width = 0 
        )
        # Initialize font 
        font = pygame.font.SysFont(
            name = font,
            size = font_size,
            bold = True
        )
        # Create text message 
        text = font.render (
            str_msg,
            True,
            text_color
        )
        # Center the text on top of the previous rectangle
        text_box = text.get_rect()
        text_box.center = rect.center

        #Display text
        screen.blit(text, text_box)
