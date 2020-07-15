from tiles import Tiles


class Playground:
    """The game board"""
    def __init__(self, BOARD_LEN, SQUARE_NUM, SQUARE_LEN, STROKE_WEIGHT):
        self.BOARD_LEN = BOARD_LEN
        self.SQUARE_LEN = SQUARE_LEN
        self.SQUARE_NUM = SQUARE_NUM
        self.STROKE_WEIGHT = STROKE_WEIGHT

    def display(self):
        """Draw lines"""
        strokeWeight(self.STROKE_WEIGHT)
        for col in range(1, self.SQUARE_NUM):
            line(self.SQUARE_LEN * col, 0,
                 self.SQUARE_LEN * col, self.BOARD_LEN)
        for row in range(1, self.SQUARE_NUM):
            line(0, self.SQUARE_LEN * row,
                 self.BOARD_LEN, self.SQUARE_LEN * row)
