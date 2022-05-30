import calendar
import itertools


def test_june_2022():
    o = calendar.TextCalendar()
    s = o.formatmonth(2022, 6)
    assert "June 2022" in s
    assert s.splitlines()[-1] == "27 28 29 30"


def test_product():
    deck = list(itertools.product("♠♥♦♣", range(1, 14)))
    assert len(deck) == 52
