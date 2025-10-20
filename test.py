from _datetime import date, timedelta

def checkio(start_date, end_date):
    count_days = 0

    while start_date <= end_date:
        if start_date.weekday() >= 5:
            count_days += 1
        start_date += timedelta(days=1)

    return count_days

if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"