"""63070224"""


def main():
    date = input().split("/")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    print(valid_day(day, month, year))
    print(valid_month(month))
    print(valid_year(year))
    print(leap_year(year))


def valid_day(day, month, year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):  # leap year
        if month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
            return True
        elif month in [4, 6, 9, 11] and day <= 30:
            return True
        elif month == 2 and day <= 29:
            return True
        else:
            return False
    else:
        if month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
            return True
        elif month in [4, 6, 9, 11] and day <= 30:
            return True
        elif month == 2 and day <= 28:
            return True
        else:
            return False


def valid_month(month):
    if 1 <= month <= 12:
        return True
    else:
        return False


def valid_year(year):
    if year > 0:
        return True
    else:
        return False


def leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
