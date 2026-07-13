"""
This class holds a timer that counts down
"""
class Timer:
    """
    Initalizes a timer that counts down given number of seconds
    """
    def __init__ (self, x_coord, y_coord, width, length, seconds, color):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.length = length
        self.seconds = seconds
        self.color = color
