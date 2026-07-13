"""
The class records the timer and training iteration in the game
"""
import pygame

# Colours
BLACK = (0,0,0)
ORANGE = (255, 172, 28)
BLUE = (173, 216, 230)

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
        # Initialize font 
        scoreboard_font = pygame.font.SysFont(
            name = self.font,
            size = self.font_size,
            bold = False
        )
        # Write current iteration
        iteration_text = scoreboard_font.render(
            "Current iteration: " + str(self.iteration),
            True,
            BLACK
        )
        screen.blit(iteration_text, (230, 215) )

        # Write number of orange wins 
        owins_text = scoreboard_font.render(
            "Orange wins: " + str(self.o_wins),
            True,
            ORANGE
        )
        screen.blit(owins_text, (230, 243))
        # Write number of blue wins 
        bwins_text = scoreboard_font.render(
            "Blue wins: " + str(self.b_wins),
            True,
            BLUE
        )
        screen.blit(bwins_text, (230, 271))