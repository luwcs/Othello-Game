from tiles import Tiles

NOTHING = -1
BLACK = 0
WHITE = 255


def test_constructor():
    t = Tiles(8, 100, 90)
    assert t.SQUARE_NUM == 8
    assert t.SQUARE_LEN == 100
    assert t.DIAMETER == 90
    assert t.black_turn


def test_first_four_tiles():
    t = Tiles(4, 100, 90)
    assert t.tiles_lst[0][0] == NOTHING
    assert t.tiles_lst[1][1] == WHITE


def test_add_tile():
    t = Tiles(4, 100, 90)
    assert t.black_count == 2
    assert t.black_turn
    t.add_tile(0, 1)
    assert not t.black_turn
    assert t.tiles_lst[1][1] == BLACK
    assert t.black_count == 4


def test_update():
    t = Tiles(4, 100, 90)
    assert (2, 0) not in t.valid_lst
    t.add_tile(0, 1)
    assert (2, 0) in t.valid_lst


def test_on_board():
    t = Tiles(4, 100, 90)
    assert t.on_board(1, 1)
    assert not t.on_board(12, 12)


def test_valid_or_flip():
    t = Tiles(4, 100, 90)
    assert t.tiles_lst[1][1] == t.WHITE
    t.valid_or_flip(0, 1, True)
    assert t.tiles_lst[1][1] == t.BLACK