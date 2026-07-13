"""
This class holds a timer that counts down
"""
import pygame

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
        # Create rectangle to put text on top of 
        rect = pygame.Rect(self.x_coord, self.y_coord, self.width, self.length)
        pygame.draw.rect (
            surface = screen,
            color = self.color,
            rect = rect,
            width = 0 
        )
        # Initialize font
        timer_font = pygame.font.SysFont (
            name = self.font,
            size = self.font_size,
            bold = True
        )
        # Create text
        text = timer_font.render (
            str(self.current_time),
            True, # adds some text smoothing
            BLACK
        )
        # Center the text on top of the previous rectangle
        text_box = text.get_rect()
        text_box.center = rect.center

        # Display text
        screen.blit(text, text_box)

    
    
    