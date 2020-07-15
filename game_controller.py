import random


class GameController:
    def __init__(self, BOARD_LEN, SQUARE_LEN, DIAMETER, tiles, playground):
        self.white_wins = False
        self.black_wins = False
        self.tie = False
        self.SQUARE_LEN = SQUARE_LEN
        self.BOARD_LEN = BOARD_LEN
        self.tiles = tiles
        self.pg = playground
        self.time_counter = 0
        self.save_score = True
        self.enter_name = True

    def display(self):
        """Display tiles and playboard."""
        self.tiles.display()
        self.pg.display()

    def player_move(self, x, y):
        col = x // self.SQUARE_LEN
        row = y // self.SQUARE_LEN
        if self.tiles.black_turn:
            self.tiles.add_tile(row, col)

    def AI_move(self):
        flip_count = []
        for (row, col) in self.tiles.valid_lst:
            flip_count.append(self.tiles.valid_or_flip(row, col))
        for (row, col) in self.tiles.valid_lst:
            if self.tiles.valid_or_flip(row, col) == max(flip_count):
                self.tiles.add_tile(row, col)
                break

    def update(self):
        REFRESH_TIMES = 60
        ONE_REFRESH = 1
        AI_DELAY = 1
        if self.tiles.valid_lst == set():
            self.tie = self.tiles.white_count == self.tiles.black_count
            self.black_wins = self.tiles.black_count > self.tiles.white_count
            self.white_wins = self.tiles.black_count < self.tiles.white_count
            self.set_player()
            self.results()
            self.score_output()
        if not self.tiles.black_turn:
            self.time_counter += ONE_REFRESH
            if self.time_counter == AI_DELAY * REFRESH_TIMES:
                self.AI_move()
                self.time_counter = 0

    def set_player(self):
        """Prompt the player for their name."""
        if self.enter_name:
            answer = self.input('Please enter your name: ')
            if answer:
                print('hi ' + answer)
            elif answer == '':
                print('[empty string]')
            else:
                print(answer)
            self.player_name = answer
        self.enter_name = False

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def score_output(self):
        """
        Save player name and score to scores.txt,
        and keep the highest score is always the first entry in the file.
        """
        if self.save_score:
            records = []
            with open('scores.txt') as f:
                for line in f:
                    name_and_score = line.split()
                    records.append((name_and_score[0], int(name_and_score[1])))
            if records != []:
                if self.tiles.black_count > records[0][1]:
                    records.insert(0, (self.player_name, self.tiles.black_count))
                else:
                    records.append((self.player_name, self.tiles.black_count))
            elif records == []:
                records.append((self.player_name, self.tiles.black_count))
            with open('scores.txt', 'w') as f:
                for n_s in records:
                    f.write(n_s[0] + " " + str(n_s[1]) + '\n')
            self.save_score = False

    def results(self):
        """Announce the winner in the graphics window."""
        YELLOW = (232, 235, 52)
        TEXT_SIZE = 50
        WINNER_HORIZON = self.BOARD_LEN * 2 / 5
        WINNER_VER = self.BOARD_LEN * 2 / 5
        BLACK_SCORE_HOR = self.BOARD_LEN * 1 / 15
        WHITE_SCORE_HOR = self.BOARD_LEN * 3 / 5
        SCORE_VER = self.BOARD_LEN * 3 / 5

        fill(*YELLOW)
        textSize(TEXT_SIZE)
        if self.white_wins:
            text("AI WINS", WINNER_HORIZON, WINNER_VER)
        elif self.black_wins:
            text(str(self.player_name)+" WINS", WINNER_HORIZON, WINNER_VER)
        else:
            text("TIE", WINNER_HORIZON, WINNER_VER)
        text("Black has " + str(self.tiles.black_count) + " tiles",
             BLACK_SCORE_HOR, SCORE_VER)
        text("White has " + str(self.tiles.white_count) + " tiles",
             WHITE_SCORE_HOR, SCORE_VER)






