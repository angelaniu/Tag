"""
Run this file to start the tag game
"""

import pygame
from cube import Cube
from settings import Settings
from scoreboard import Scoreboard
from game_timer import Timer

# Colours 
LIGHT_GRAY = (211, 211, 211)
WHITE = (255, 255, 255)
LIGHT_PURPLE = (250, 231, 255)
DARK_PURPLE = (202, 126, 224)
ORANGE = (255, 172, 28)
BLUE = (173, 216, 230)

# Create game display 
game_settings = Settings (
    display_width = 800,
    display_height = 600,
    ground = 550,
    left_wall = 10,
    right_wall = 790,
    gravity = 0.15,
    air_resistance = 0.03,
    friction = 0.1
)

# Create cube to be tagged
blue_cube = Cube (
    tl_square_x = 150,
    tl_square_y = 500,
    color = (173, 216, 230),
    size = 50,
    is_tagger = False
)

# Create tagger cube
orange_cube = Cube (
    tl_square_x = 600,
    tl_square_y = 500,
    color = ORANGE,
    size = 50,
    is_tagger = True
)

# Create timer 
timer = Timer (
    x_coord = 250,
    y_coord = 120,
    length = 80,
    width = 300,
    seconds = 20, 
    color = DARK_PURPLE,
    font = "freesansbold.ttf",
    font_size = 70
)
# Create scoreboard 
scoreboard = Scoreboard (
    x_coord = 200,
    y_coord = 100,
    length = 200,
    width = 400,
    color = LIGHT_PURPLE,
    font = "freesansbold.ttf", 
    font_size = 28
)

pygame.init()
screen = pygame.display.set_mode((game_settings.width, game_settings.height))
running = True

# Actions per frame of the game when activated 
while running:
    for event in pygame.event.get():
        # If user closes window, quit game
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            # Movement for blue cube
            if event.key == pygame.K_w:
                blue_cube.vertical_jump(game_settings, orange_cube)
            if event.key == pygame.K_a:
                blue_cube.horizontal_jump("left", game_settings)
            if event.key == pygame.K_d:
                blue_cube.horizontal_jump("right", game_settings)
            # Movement for orange cube 
            if event.key == pygame.K_UP:
                orange_cube.vertical_jump(game_settings, blue_cube)
            if event.key == pygame.K_LEFT:
                orange_cube.horizontal_jump("left", game_settings)
            if event.key == pygame.K_RIGHT:
                orange_cube.horizontal_jump("right", game_settings)
            
    # Apply vertical physics 
    blue_cube.vertical_physics(game_settings, orange_cube)
    orange_cube.vertical_physics(game_settings, blue_cube)

    # Apply physics to horizontal jump 
    blue_cube.horizontal_physics(game_settings, orange_cube)
    orange_cube.horizontal_physics(game_settings, blue_cube)

    # Paint screen and ground 
    screen.fill(WHITE)
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 550, 800, 100), 0)

    # Paint objects 
    scoreboard.display_scoreboard(screen)
    timer.display_timer(screen)
    orange_cube.display_cube(screen)
    blue_cube.display_cube(screen)

    # Update screen display
    pygame.display.flip()

pygame.quit()