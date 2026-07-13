"""
The class records the timer and training iteration in the game
"""
class Scoreboard:
    def __init__(
            self,
            x_coord,
            y_coord,
            length,
            width,
            color,
            timer,
        ):
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
        self.timer = timer
        self.iteration = 0
        self.p1_wins = 0
        self.p2_wins = 0 