from game_controller import GameController
from playground import Playground
from tiles import Tiles


def test_constructor():
    pg = Playground(400, 4, 100, 3)
    tiles = Tiles(4, 100, 90)
    gc = GameController(400, 100, 90, tiles, pg)
    assert not gc.black_wins
    assert not gc.white_wins
    assert not gc.tie
    assert gc.save_score
    assert gc.SQUARE_LEN == 100
    assert gc.BOARD_LEN == 400
    assert gc.time_counter == 0


def test_player_move():
    pg = Playground(400, 4, 100, 3)
    tiles = Tiles(4, 100, 90)
    gc = GameController(400, 100, 90, tiles, pg)
    gc.player_move(50, 150)
    assert gc.tiles.black_count == 4


def test_update():
    pg = Playground(400, 4, 100, 3)
    tiles = Tiles(4, 100, 90)
    gc = GameController(400, 100, 90, tiles, pg)
    gc.player_move(50, 150)
    assert gc.time_counter == 0
    assert not gc.tiles.black_turn
    gc.update()



def test_AI_move():
    pg = Playground(800, 8, 100, 3)
    tiles = Tiles(8, 100, 90)
    gc = GameController(800, 100, 90, tiles, pg)
    gc.player_move(100, 100)
    assert gc.tiles.white_count == 2

