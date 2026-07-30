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
DARK_ORANGE = (255, 86, 0)
DARK_BLUE = (0, 161, 255)


# Initialize objects in this program 
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

# Create blue cube to be tagged
blue_cube = Cube (
    tl_square_x_init = 150, 
    tl_square_y_init = 500,
    tl_square_x = 150,
    tl_square_y = 500,
    color = BLUE,
    dead_color = DARK_BLUE,
    size = 50,
    is_tagger = False
)

# Create orange tagger cube
orange_cube = Cube (
    tl_square_x_init = 600, 
    tl_square_y_init = 500,
    tl_square_x = 600,
    tl_square_y = 500,
    color = ORANGE,
    dead_color = DARK_ORANGE,
    size = 50,
    is_tagger = True
)

# Create timer 
timer = Timer (
    x_coord = 250,
    y_coord = 120,
    length = 80,
    width = 300,
    seconds = 20,  #Change to 20 seconds later
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

# Initialize pygame 
pygame.init()
screen = pygame.display.set_mode((game_settings.width, game_settings.height))

# Run iterations of the game 
training = True
while training:
    # Reset positions of cubes, reset timer, and increment scoreboard properly before each iteration 
    orange_cube.reset_cube()
    blue_cube.reset_cube()
    timer.reset_timer()
    scoreboard.iteration += 1

    # Begin each individual game 
    running = True
    iteration_start_tick = pygame.time.get_ticks()
    # Actions per frame of the game when a game starts
    while running:
        for event in pygame.event.get():
            # If user closes window, quit game
            if event.type == pygame.QUIT:
                running = False
                training = False
                break

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

        # If collision occurred during previous jump, adjust scoreboard 
        if blue_cube.is_dead:
            scoreboard.o_wins += 1

        # Display time
        current_tick = pygame.time.get_ticks()
        current_sec = (current_tick - iteration_start_tick) // 1000 
        timer.current_time = max(0, timer.seconds - current_sec)

        # If the timer reaches 0, tagger cube dies and game is over
        if timer.current_time == 0:
            orange_cube.is_dead = True
            scoreboard.b_wins += 1

        # Paint screen and ground 
        screen.fill(WHITE)
        pygame.draw.rect(screen, LIGHT_GRAY, (0, 550, 800, 100), 0)

        # Paint objects 
        scoreboard.display_scoreboard(screen)
        timer.display_timer(screen)
        orange_cube.display_cube(screen)
        blue_cube.display_cube(screen)

        # If either cube is dead, end game
        if blue_cube.is_dead or orange_cube.is_dead:
            Cube.display_game_over(screen)
            # Update display and then freeze game for 1 second
            pygame.display.flip()
            pygame.time.wait(1000) 
            running = False
            
        # If no death, can update screen immediately 
        else: 
            pygame.display.flip()
pygame.quit()

