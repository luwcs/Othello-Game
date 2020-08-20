from game_controller import GameController
from playground import Playground
from tiles import Tiles

BOARD_LEN = 800
SQUARE_LEN = 100
SQUARE_NUM = 8
DIAMETER = 90
STROKE_WEIGHT = 3
GREEN = (17, 115, 33)
COLOR_MAX = 255

tiles = Tiles(SQUARE_NUM, SQUARE_LEN, DIAMETER)
pg = Playground(BOARD_LEN, SQUARE_NUM, SQUARE_LEN, STROKE_WEIGHT)
gc = GameController(BOARD_LEN, SQUARE_LEN, DIAMETER, tiles, pg)


def setup():
    size(BOARD_LEN, BOARD_LEN)
    colorMode(RGB, COLOR_MAX)


def draw():
    background(*GREEN)
    gc.display()
    gc.update()


def mousePressed():
    gc.player_move(mouseX, mouseY)
