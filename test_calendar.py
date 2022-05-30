import calendar


def test_june_2022():
    o = calendar.TextCalendar()
    s = o.formatmonth(2022, 6)
    assert "June 2022" in s
