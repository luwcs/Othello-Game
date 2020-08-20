from playground import Playground


def test_constructor():
    pg = Playground(800, 8, 100, 3)
    assert pg.BOARD_LEN == 800
    assert pg.SQUARE_LEN == 100
    assert pg.SQUARE_NUM == 8
    assert pg.STROKE_WEIGHT == 3
