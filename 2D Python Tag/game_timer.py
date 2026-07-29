"""
This class holds a timer that counts down
"""
import pygame
from settings import Graphic_Helper

# Colours
BLACK = (0,0,0)

class Timer:
    """
    Initalizes a timer that counts down given number of seconds
    """
    def __init__ (self, x_coord, y_coord, width, length, seconds, color, font, font_size):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.length = length
        self.seconds = seconds
        self.color = color
        self.font = font
        self.current_time = seconds
        self.font_size = font_size

    def display_timer (self, screen):
        """
        This method draws the timer onto the game screen
        """
        Graphic_Helper.rect_with_msg(
            str_msg = str(self.current_time),
            x = self.x_coord,
            y = self.y_coord,
            width = self.width,
            length = self.length,
            screen = screen,
            bg_color = self.color,
            font = self.font,
            font_size = self.font_size,
            text_color = BLACK
        )
    def reset_timer (self):
        """
        This method resets the timer to its original settings
        """
        self.current_time = self.seconds
        
    
    
    