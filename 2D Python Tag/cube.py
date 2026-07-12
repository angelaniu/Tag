"""
This class creates a cube and handles cube movements in the tag game. 
"""

class Cube:
    def __init__(self, tl_square_x, tl_square_y, color, size, is_tagger):
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

        self.tl_square_x = tl_square_x
        self.tl_square_y = tl_square_y
        self.color = color
        self.size = size 
        self.is_tagger = is_tagger

    def vertical_jump(self, display, otherCube):
        """
        Determines vertical velocity of square when jumped 
        """
        # If square is on the ground or on top of another cube
        if (self.tl_square_y + self.size == display.ground
            or self.tl_square_y + self.size == otherCube.tl_square_y
        ):
            # give upwards velocity
            self.y_velocity = -8
    
    def horizontal_jump(self, direction, display):
        """
        Determines the horizontal velocity of the square when jumped
        """
        # Check if the cube has space to move horizontally 
        if direction == "right" and self.tl_square_x < display.right_wall - self.size:
            self.x_velocity = 5
        elif direction == "left" and self.tl_square_x > display.left_wall:
            self.x_velocity = -5
    
    def vertical_physics(self, display, otherCube):
        """
        Adjusts y-coordinate of cube after vertical jump
        """
        # Gravity decreases upwards velocity
        self.y_velocity += display.gravity
        self.tl_square_y += self.y_velocity

        # Don't allow square to fall beneath ground
        if self.tl_square_y + self.size > display.ground:
            self.tl_square_y = display.ground - self.size
            self.y_velocity = 0 
        
        # Don't allow cube to fall beneath another cube
        if (self.tl_square_y + self.size > otherCube.tl_square_y and self.tl_square_y < otherCube.tl_square_y
            and (
                (self.tl_square_x <= otherCube.tl_square_x and otherCube.tl_square_x <= self.tl_square_x + self.size)
                or (otherCube.tl_square_x <= self.tl_square_x and self.tl_square_x <= otherCube.tl_square_x + otherCube.size)
                )
        ):
            # Make the cubes stack 
            self.tl_square_y = otherCube.tl_square_y - self.size
            self.y_velocity = 0
            

    def horizontal_physics(self, display):
        """
        Adjusts x-coordinate of cube after horizontal jump
        """
        # If cube is on the ground, use ground friction
        if self.tl_square_y + self.size == display.ground:
            # Allow velocity to reach 0 and not bounce back and forth 
            if abs(self.x_velocity) < display.friction:
                self.x_velocity = 0 

            # If velocity is moving left
            elif self.x_velocity < 0:
                self.x_velocity += display.friction
                self.tl_square_x += self.x_velocity
                # Don't allow square to move past left wall
                if self.tl_square_x < display.left_wall:
                    self.tl_square_x = display.left_wall
                    self.x_velocity = 0

            # If velocity is moving right 
            elif self.x_velocity > 0:
                self.x_velocity -= display.friction 
                self.tl_square_x += self.x_velocity
                # Don't allow square to move past right wall
                if (self.tl_square_x + self.size) > display.right_wall:
                    self.tl_square_x = display.right_wall - self.size
                    self.x_velocity = 0

        # If cube is in air, use air resistance
        else:
            # Allow velocity to reach 0 and not bounce back and forth 
            if abs(self.x_velocity) < display.air_resistance:
                self.x_velocity = 0 

            # If velocity is moving left
            elif self.x_velocity < 0:
                self.x_velocity += display.air_resistance
                self.tl_square_x += self.x_velocity
                # Don't allow square to move past left wall
                if self.tl_square_x < display.left_wall:
                    self.tl_square_x = display.left_wall
                    self.x_velocity = 0

            # If velocity is moving right 
            elif self.x_velocity > 0:
                self.x_velocity -= display.air_resistance
                self.tl_square_x += self.x_velocity
                # Don't allow square to move past right wall
                if (self.tl_square_x + self.size) > display.right_wall:
                    self.tl_square_x = display.right_wall - self.size
                    self.x_velocity = 0

