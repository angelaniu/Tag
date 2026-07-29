"""
This class creates a cube and handles cube movements in the tag game. 
"""
import pygame
from settings import Graphic_Helper

# Colours
RED = (227, 65, 65)
WHITE = (255, 255, 255)
DARK_ORANGE = (255, 116, 0)
DARK_BLUE = (38, 185, 235)

class Cube:
    def __init__(self, tl_square_x_init, tl_square_y_init, tl_square_x, tl_square_y, color, dead_color, size, is_tagger):
        """
        Initializes a cube 
        tl_square_x: x coordinate of top left corner of cube 
        tl_square y: y coordinate of top left corner of cube 
        color: color of the cube 
        size: the pixel width of a cube 
        is_tagger: indicates whether the cube is a tagger, or to be tagged 
        """

        self.x_velocity = 0
        self.y_velocity = 0
        self.is_dead = False
        # Track initial coordinates for the cube for reset
        self.tl_square_x_init = tl_square_x_init
        self.tl_square_y_init = tl_square_y_init
        # Track the dynamic coordinates of the cube 
        self.tl_square_x = tl_square_x
        self.tl_square_y = tl_square_y
        self.color = color
        self.dead_color = dead_color
        self.size = size 
        self.is_tagger = is_tagger

    def vertical_jump(self, settings, otherCube):
        """
        Determines vertical velocity of square when jumped 
        """
        # If square is on the ground or on top of another cube
        if (self.tl_square_y + self.size == settings.ground
            or self.tl_square_y + self.size == otherCube.tl_square_y
        ):
            # give upwards velocity
            self.y_velocity = -8
    
    def horizontal_jump(self, direction, settings):
        """
        Determines the horizontal velocity of the square when jumped
        """
        # Check if the cube has space to move horizontally 
        if direction == "right" and self.tl_square_x < settings.right_wall - self.size:
            self.x_velocity = 5
        elif direction == "left" and self.tl_square_x > settings.left_wall:
            self.x_velocity = -5
    
    def vertical_physics(self, settings, otherCube):
        """
        Adjusts y-coordinate of cube after vertical jump
        """
        # Gravity decreases upwards velocity
        self.y_velocity += settings.gravity
        self.tl_square_y += self.y_velocity

        # Don't allow square to fall beneath ground
        if self.tl_square_y + self.size > settings.ground:
            self.tl_square_y = settings.ground - self.size
            self.y_velocity = 0 
        
        # Don't allow cube to fall beneath another cube
        if (self.tl_square_y + self.size >= otherCube.tl_square_y and self.tl_square_y <= otherCube.tl_square_y
            and (
                (self.tl_square_x <= otherCube.tl_square_x and otherCube.tl_square_x <= self.tl_square_x + self.size)
                or (otherCube.tl_square_x <= self.tl_square_x and self.tl_square_x <= otherCube.tl_square_x + otherCube.size)
            )
            # Prevent this cube from being placed above the other cube when this cube is jumping from below
            and (
                self.y_velocity > 0
            )
        ):
            # If one cube falls below the other, make the cubes stack 
            # Leave a single pixel difference between both cubes to prevent edge cases on corners
            self.tl_square_y = otherCube.tl_square_y - self.size - 1
            self.y_velocity = 0
            # During collision one cube dies
            self.cube_collision(otherCube)

    def horizontal_movement(self, force, settings, otherCube):
        """
        Helper function of horizontal_physics 
        Adjusts x-coordinate of cube depending on type of force (air resistance, or ground friction)
        """
        # Allow velocity to reach 0 and not bounce back and forth 
        if abs(self.x_velocity) < force:
            self.x_velocity = 0 

        # If velocity is moving left
        elif self.x_velocity < 0:
            self.x_velocity += force
            self.tl_square_x += self.x_velocity
            # Don't allow square to move past left wall
            if self.tl_square_x < settings.left_wall:
                self.tl_square_x = settings.left_wall
                self.x_velocity = 0
            # Don't allow this cube to move left into another cube
            if (
                otherCube.tl_square_x + otherCube.size >= self.tl_square_x and otherCube.tl_square_x <= self.tl_square_x
                and (
                    (otherCube.tl_square_y <= self.tl_square_y + self.size <= otherCube.tl_square_y + otherCube.size)
                    or 
                    (otherCube.tl_square_y <= self.tl_square_y <= otherCube.tl_square_y + otherCube.size)
                )
            ):
                self.x_velocity = 0 
                # Leave a single pixel difference between both cubes to prevent edge cases on corners
                self.tl_square_x = otherCube.tl_square_x + otherCube.size + 1
                # During collision one cube dies
                self.cube_collision(otherCube)

        # If velocity is moving right 
        elif self.x_velocity > 0:
            self.x_velocity -= force
            self.tl_square_x += self.x_velocity
            # Don't allow square to move past right wall
            if (self.tl_square_x + self.size) > settings.right_wall:
                self.tl_square_x = settings.right_wall - self.size
                self.x_velocity = 0
            
            # During collision don't allow square to move right into another cube 
            if (
                self.tl_square_x + self.size >= otherCube.tl_square_x and self.tl_square_x <= otherCube.tl_square_x
                and (
                    (self.tl_square_y <= otherCube.tl_square_y <= self.tl_square_y + self.size)
                    or
                    (otherCube.tl_square_y <= self.tl_square_y <= otherCube.tl_square_y + otherCube.size)
                )
            ):
                self.x_velocity = 0 
                self.tl_square_x = otherCube.tl_square_x - self.size - 1
                # During collision one cube dies
                self.cube_collision(otherCube)

    def horizontal_physics(self, settings, otherCube):
        """
        Adjusts x-coordinate of cube after horizontal jump
        """
        # If cube is on the ground, use ground friction
        if self.tl_square_y + self.size == settings.ground:
            self.horizontal_movement(settings.friction, settings, otherCube)

        # If cube is in air, use air resistance
        else:
            self.horizontal_movement(settings.air_resistance, settings, otherCube)
    
    def cube_collision(self, otherCube):
        """
        This method sets a cube to dead state when a collision occurs
        """
        # If this cube is not a tagger, this cube is dead
        if self.is_tagger == False: 
            self.is_dead = True
        # If this cube is a tagger, the other cube is dead
        else:
            otherCube.is_dead = True
    
    @staticmethod
    def display_game_over (screen):
        """
        This method displays a game over banner at the top of the screen
        """
        Graphic_Helper.rect_with_msg(
            str_msg = "Game over",
            x = 200,
            y = 40,
            width = 400,
            length = 50,
            screen = screen,
            bg_color = RED,
            font = "freesansbold.ttf",
            font_size = 40, 
            text_color = WHITE
        )

    def reset_cube(self):
        """
        This method resets a cube to its original starting state at the start of each iteration
        """
        self.x_velocity = 0
        self.y_velocity = 0
        self.is_dead = False
        self.tl_square_x = self.tl_square_x_init
        self.tl_square_y = self.tl_square_y_init
 

    def display_cube(self, screen):
        """
        This method draws a cube on the game screen
        """
        # If the cube is dead, color the cube with their dead color 
        if self.is_dead == True: 
            pygame.draw.rect(
                surface = screen, 
                color = self.dead_color, 
                rect = (self.tl_square_x, self.tl_square_y, self.size, self.size),
                width = 0
                )  
        # If cube is alive, color normally 
        else:
            pygame.draw.rect(
                surface = screen, 
                color = self.color, 
                rect = (self.tl_square_x, self.tl_square_y, self.size, self.size),
                width = 0
            )

        


