"""
The class records the timer and training iteration in the game
"""
import pygame
from settings import Graphic_Helper

# Colours
BLACK = (0,0,0)
ORANGE = (255, 172, 28)
BLUE = (173, 216, 230)
RED = (227, 65, 65)

class Scoreboard:
    def __init__(self, x_coord, y_coord, length, width, color, font, font_size):
        """
        Constructs the scoreboard at the back of the game display 
        x_coord: the x-coordinate of the top left corner of the board 
        y_coord: the y-coordinate of the top left corner of the board 
        seconds: the number of seconds to countdown from before the tagger automatically loses 
        iteration: number of iterations trained 
        p1_wins: total number of wins by the tagger
        p2_wins: total number of wins by the cube being tagged
        """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.width = width
        self.color = color
        self.font = font
        self.font_size = font_size
        self.iteration = 0
        self.o_wins = 0
        self.b_wins = 0 
    
    def display_scoreboard(self, screen):
        """
        This method draws the scoreoard onto the game screen
        """
        # Draw background of scoreboard
        pygame.draw.rect(
            surface = screen,
            color = self.color,
            rect = (self.x_coord, self.y_coord, self.width, self.length),
            width = 0
        )
        Graphic_Helper.insert_medium_txt(
            str_msg = "Current iteration: " + str(self.iteration),
            x = 230, 
            y = 215,
            screen = screen,
            font = self.font,
            font_size = 28,
            text_color = BLACK
        )
        Graphic_Helper.insert_medium_txt(
            str_msg = "Orange wins: " + str(self.o_wins),
            x = 230, 
            y = 243,
            screen = screen,
            font = self.font,
            font_size = 28,
            text_color = ORANGE
        )
        Graphic_Helper.insert_medium_txt(
            str_msg = "Blue wins: " + str(self.b_wins),
            x = 230, 
            y = 271,
            screen = screen,
            font = self.font,
            font_size = 28,
            text_color = BLUE
        )
  


        