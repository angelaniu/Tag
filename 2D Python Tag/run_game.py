"""
Run this file to start the tag game
"""

import pygame
from cube import Cube
from display import Display
from scoreboard import Scoreboard
from timer import Timer


# Create game display 
game = Display (
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
orange_cube = Cube(
    tl_square_x = 600,
    tl_square_y = 500,
    color = (255, 172, 28),
    size = 50,
    is_tagger = True
)

# Create timer 
timer = Timer (
    x_coord = 250,
    y_coord = 120,
    length = 150,
    width = 300,
    seconds = 20, 
    color = (240, 240, 240)
)
# Create scoreboard 
scoreboard = Scoreboard(
    x_coord = 200,
    y_coord = 100,
    length = 200,
    width = 400,
    color = (250, 231, 255),
    timer = timer
)

pygame.init()
screen = pygame.display.set_mode((game.width, game.height))
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
                blue_cube.vertical_jump(game, orange_cube)
            if event.key == pygame.K_a:
                blue_cube.horizontal_jump("left", game)
            if event.key == pygame.K_d:
                blue_cube.horizontal_jump("right", game)
            # Movement for orange cube 
            if event.key == pygame.K_UP:
                orange_cube.vertical_jump(game, blue_cube)
            if event.key == pygame.K_LEFT:
                orange_cube.horizontal_jump("left", game)
            if event.key == pygame.K_RIGHT:
                orange_cube.horizontal_jump("right", game)
            
    # Apply vertical physics 
    blue_cube.vertical_physics(game, orange_cube)
    orange_cube.vertical_physics(game, blue_cube)

    # Apply physics to horizontal jump 
    blue_cube.horizontal_physics(game, orange_cube)
    orange_cube.horizontal_physics(game, blue_cube)

    # Paint display
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (211, 211, 211), (0, 550, 800, 100), 0)
    pygame.draw.rect(
        surface = screen,
        color = scoreboard.color,
        rect = (scoreboard.x_coord, scoreboard.y_coord, scoreboard.width, scoreboard.length),
        width = 0
    )
    pygame.draw.rect(
        surface = screen, 
        color = timer.color,
        rect = (timer.x_coord, timer.y_coord, timer.width, timer.length),
        width = 0
    )

    # Paint cubes
    pygame.draw.rect(
        surface = screen,
        color = orange_cube.color,
        rect = (orange_cube.tl_square_x, orange_cube.tl_square_y, orange_cube.size, orange_cube.size),
        width = 0
    )
    pygame.draw.rect(
        surface = screen,
        color = blue_cube.color,
        rect = (blue_cube.tl_square_x, blue_cube.tl_square_y, blue_cube.size, blue_cube.size),
        width = 0
    )

    # Update screen display
    pygame.display.flip()

pygame.quit()