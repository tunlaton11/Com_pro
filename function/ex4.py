"""630070224"""


def valid_day(day):
    day_check, month, year = int(day[0]), day[1], int(day[2])
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):  # leap year
        if month in ["1", "3", "5", "7", "8", "10", "12"] and day_check <= 31:
            return True
        elif month in ["4", "6", "9", "11"] and day_check <= 30:
            return True
        elif month == "2" and day_check <= 29:
            return True
        else:
            return False
    else:
        if month in ["1", "3", "5", "7", "8", "10", "12"] and day_check <= 31:
            return True
        elif month in ["4", "6", "9", "11"] and day_check <= 30:
            return True
        elif month == "2" and day_check <= 28:
            return True
        else:
            return False


def valid_month(month):
    month_check = int(month[1])
    if 1 <= month_check <= 12:
        return True
    else:
        return False


def valid_year(year):
    year_check = int(year[2])
    if year_check > 0:
        return True
    else:
        return False


def main():
    date = input()
    date_list = date.split("/")
    check = [valid_day(date_list), valid_month(
        date_list), valid_year(date_list)]
    if False in check:
        print("False")
    else:
        print("True")


main()
