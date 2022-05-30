import itertools


def test_product():
    deck = list(itertools.product("♠♥♦♣", range(1, 14)))
    assert len(deck) == 52
