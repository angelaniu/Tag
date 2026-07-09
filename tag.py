import pygame
pygame.init()

# note: (x=0,y=0) is the top left corner of the screen

# Track bottom left corner of the square 
bl_square_x = 100
bl_square_y = 500

# Tracking velocity and gravity of square 
vel_square_y = 0
gravity = 0.1
ground = 500

# Determines velocity of square when jumped 
def jump(y):
    # If square is on the ground, give the square 15 velocity upwards
    if y == ground:
        return -8
    # If square is in the air, return current velocity
    return vel_square_y

# Jump location of square per frame 
def update_physics(y, velocity):
    # Gravity decreases upwards velocity
    velocity += gravity
    y += velocity

    # Don't allow square to fall under the ground 
    if y > ground:
        y = ground
        velocity = 0

    return y, velocity

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
                vel_square_y = jump(bl_square_y)

    # Check for horizontal movement 
    keys = pygame.key.get_pressed()
    # If D is held, move right
    if keys[pygame.K_d]:
        bl_square_x += 2   

    # If A is held, move left
    if keys[pygame.K_a]:
        bl_square_x -= 2    

    # Apply physics to the jump 
    bl_square_y, vel_square_y = update_physics(bl_square_y, vel_square_y)
   
    # Paint full window white, and insert a blue square
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (173, 216, 230), (bl_square_x, bl_square_y, 50, 50), 0)

    # Update screen display
    pygame.display.flip()
pygame.quit()