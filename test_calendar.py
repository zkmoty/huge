import calendar


def test_june_2022():
    o = calendar.TextCalendar()
    s = o.formatmonth(2022, 6)
    assert "June 2022" in s
    assert s.splitlines()[-1] == "27 28 29 30"
    assert s.split()[-30:] == [str(x) for x in range(1, 31)]


def test_july_2022():
    o = calendar.TextCalendar()
    s = o.formatmonth(2022, 7)
    assert "July 2022" in s
    assert s.splitlines()[-1] == "25 26 27 28 29 30 31"
