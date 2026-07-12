import pygame
pygame.init()

# note: (x=0,y=0) is the top left corner of the screen

# Track top left corner of the blue square 
tl_bsquare_x = 100
tl_bsquare_y = 500

# Track bottom left corner of blue square 
bl_bsquare_x = tl_bsquare_x
bl_bsquare_y = tl_bsquare_y + 50 

# Track top right corner of blue square 
tr_bsquare_x = tl_bsquare_x + 50 
tr_bsquare_y = tl_bsquare_y

# Track bottom right corner of blue square 
br_bsquare_x = tl_bsquare_x + 50 
br_bsquare_y = tl_bsquare_y + 50 

# Track top left corner of the orange square 
tl_osquare_x = 650
tl_osquare_y = 500

# Tracking velocity of both horizontal and vertical velocities of both squares
vel_bsquare_y = 0
vel_bsquare_x = 0

vel_osquare_y = 0 
vel_osquare_x = 0

gravity = 0.15
ground = 500
friction = 0.05
air_resistance = 0.03
left_wall = 10 
right_wall = 790

# Determines vertical velocity of square when jumped 
def vertical_jump(y):
    # If square is on the ground, give the square 15 velocity upwards
    if y == ground:
        return -8
    # If square is in the air, return current velocity
    return vel_bsquare_y # change later

# Determines horizontal velocity of the square when jumped
# ONLY takes in top left corner of square as x 
def horizontal_jump(x, direction):
        # If square has space to move 
    if direction == "right" and x < 740:
        return 5
    elif direction == "left" and x > 10:
        return -5
    else:
        return vel_bsquare_x

def horizontal_physics(x, xvelocity):
    # If cube is on the ground 
    if tl_bsquare_y == 500:
        if abs(xvelocity) < friction:
            xvelocity = 0
        # Friction decreases velocity in both directions
        elif xvelocity < 0:
            xvelocity += friction
            x += xvelocity
            # Don't allow square to go past left wall 
            if x < 10: 
                xvelocity = 0 
        elif xvelocity > 0:
            xvelocity -= friction
            x += xvelocity
            # Don't allow square to go past right wall 
            if (x+50) > 790: 
                xvelocity = 0 
    # If cube is in the air 
    else:
        if abs(xvelocity) < air_resistance:
            xvelocity = 0

        # Friction decreases velocity in both directions
        elif xvelocity < 0:
            xvelocity += air_resistance
            x += xvelocity
            # Don't allow square to go past left wall 
            if x < 10: 
                print(x)
                xvelocity = 0 

        elif xvelocity > 0:
            xvelocity -= air_resistance
            x += xvelocity
            # Don't allow square to go past right wall 
            if (x+50) > 790: 
                xvelocity = 0 
    return x, xvelocity


# Jump location of square per frame 
def vertical_physics(y, yvelocity):
    # Gravity decreases upwards velocity
    yvelocity += gravity
    y += yvelocity

    # Don't allow square to fall under the ground 
    if y > ground:
        y = ground
        yvelocity = 0

    return y, yvelocity

# Create game window 
screen = pygame.display.set_mode((800, 600))

running = True
# Displays game frame 
while running:
    # Checks for keypresses and events
    for event in pygame.event.get():
        # If user closes window, quit game
        if event.type == pygame.QUIT:
            running = False

        # If user presses a key
        if event.type == pygame.KEYDOWN:
            # If the key is W, jump upwards
            if event.key == pygame.K_w:
                vel_bsquare_y = vertical_jump(tl_bsquare_y) 
            if event.key == pygame.K_a:
                vel_bsquare_x = horizontal_jump(tl_bsquare_x, direction = "left")
            if event.key == pygame.K_d:
                vel_bsquare_x = horizontal_jump(tl_bsquare_x, direction = "right")

            if event.key == pygame.K_UP:
                vel_osquare_y = vertical_jump(tl_osquare_y)
            
                
    # Apply physics to the vertical jump 
    tl_bsquare_y, vel_bsquare_y = vertical_physics(tl_bsquare_y, vel_bsquare_y)
    tl_osquare_y, vel_osquare_y = vertical_physics(tl_osquare_y, vel_osquare_y)

    # Apply physics to horizontal jump 
    tl_bsquare_x, vel_bsquare_x = horizontal_physics(tl_bsquare_x, vel_bsquare_x)
   
    # Paint full window white, and insert a both squares
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (211, 211, 211), (0, 550, 800, 100), 0)
    pygame.draw.rect(screen, (173, 216, 230), (tl_bsquare_x, tl_bsquare_y, 50, 50), 0)
    pygame.draw.rect(screen, (255, 172, 28), (tl_osquare_x, tl_osquare_y, 50, 50), 0)

    # Update screen display
    pygame.display.flip()
    
pygame.quit()