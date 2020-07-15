import random


class Tiles:
    """Black and white tiles"""
    def __init__(self, SQUARE_NUM, SQUARE_LEN, DIAMETER):
        self.NOTHING = -1
        self.BLACK = 0
        self.WHITE = 255
        self.black_count = 0
        self.white_count = 0
        self.DIRECTION = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
                          (-1, 1), (0, 1)]
        self.SQUARE_NUM = SQUARE_NUM
        self.SQUARE_LEN = SQUARE_LEN
        self.DIAMETER = DIAMETER
        self.tiles_lst = [[-1]*SQUARE_NUM for i in range(SQUARE_NUM)]
        self.black_turn = True
        self.first_four_digits()
        self.valid_lst = set()
        self.update_valid_lst()

    def first_four_digits(self):
        """Add the first 4 tiles to the self.tiles_lst."""
        self.tiles_lst[self.SQUARE_NUM//2-1][self.SQUARE_NUM//2] = self.BLACK
        self.tiles_lst[self.SQUARE_NUM//2][self.SQUARE_NUM//2-1] = self.BLACK
        self.tiles_lst[self.SQUARE_NUM//2-1][self.SQUARE_NUM//2-1] = self.WHITE
        self.tiles_lst[self.SQUARE_NUM//2][self.SQUARE_NUM//2] = self.WHITE
        self.black_count = 2
        self.white_count = 2

    def display(self):
        """Display tiles via processing."""
        for row in range(self.SQUARE_NUM):
            for col in range(self.SQUARE_NUM):
                if self.tiles_lst[row][col] != self.NOTHING:
                    fill(self.tiles_lst[row][col])
                    ellipse((col * self.SQUARE_LEN + 0.5 * self.SQUARE_LEN),
                            (row * self.SQUARE_LEN + 0.5 * self.SQUARE_LEN),
                            self.DIAMETER, self.DIAMETER)

    def add_tile(self, row, col):
        """Put in tiles where the user clicks or AI moves."""
        if (row, col) in self.valid_lst:
            if self.black_turn:
                self.tiles_lst[row][col] = self.BLACK
                self.black_count += 1
            else:
                self.tiles_lst[row][col] = self.WHITE
                self.white_count += 1
            self.valid_or_flip(row, col, True)
            self.switch_turn()
            self.update_valid_lst()

    def update_valid_lst(self):
        """Add valid postions into valid_lst."""
        self.turn_announce()
        self.valid_lst.clear()
        for row in range(self.SQUARE_NUM):
            for col in range(self.SQUARE_NUM):
                self.valid_or_flip(row, col)

    def valid_or_flip(self, row, col, flip=False):
        """
        Check the valid positions on each direction
        and do flip when needed.
        """
        if self.black_turn:
            current_color = self.BLACK
            opposite_color = self.WHITE
        else:
            current_color = self.WHITE
            opposite_color = self.BLACK

        possible_flip_num = 0
        for (dir_row, dir_col) in self.DIRECTION:
            distance = 1
            new_row = row + dir_row * distance
            new_col = col + dir_col * distance
            flip_lst = []
            while (self.on_board(new_row, new_col)
                    and self.tiles_lst[new_row][new_col] == opposite_color):
                flip_lst.append((new_row, new_col))
                distance += 1
                new_row = row + dir_row * distance
                new_col = col + dir_col * distance
                if (not self.on_board(new_row, new_col) or self.tiles_lst[new_row][new_col] == self.NOTHING):
                    break
                elif self.tiles_lst[new_row][new_col] == current_color:
                    possible_flip_num += len(flip_lst)
                    if flip:
                        for (r, c) in flip_lst:
                            self.tiles_lst[r][c] = current_color
                            if current_color == self.BLACK:
                                self.black_count += 1
                                self.white_count -= 1
                            elif current_color == self.WHITE:
                                self.white_count += 1
                                self.black_count -= 1
                    elif self.tiles_lst[row][col] == self.NOTHING:
                        self.valid_lst.add((row, col))
                        break
        return possible_flip_num

    def turn_announce(self):
        if self.black_turn:
            print("It's black turn!")
        else:
            print("It's white turn!")

    def on_board(self, row, col):
        """Check if the position is on board."""
        return 0 <= row < self.SQUARE_NUM and 0 <= col < self.SQUARE_NUM

    def switch_turn(self):
        """Alternate between black and white tiles"""
        self.black_turn = not self.black_turn

