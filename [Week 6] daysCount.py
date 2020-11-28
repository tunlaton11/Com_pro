"""[Week 6] daysCount"""


def main():
    """[Week 6] daysCount"""
    date = input().split("/")
    day = int(date[1])
    month = int(date[0])
    year = int(date[2])
    date_new = str("%02d" % month) + "/" + str("%02d" % day) + "/" + str(year)
    if is_valid_date(year, month, day) == True:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d_count = list(map(int, date))
        if leap_year(year) == True:
            days[2] += 1
        for i in range(1, len(days)):
            days[i] += days[i-1]
        day_count = days[d_count[0]-1] + d_count[1]
        print(date_new + count(day_count))
    else:
        print(date_new + " is invalid")


def is_valid_date(year, month, day):
    """[Week 6] daysCount"""
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) == True:
        day_count_for_month[2] = 29
    check = (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
    return check


def leap_year(year):
    """[Week 6] daysCount"""
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

def count(day_count):
    """[Week 6] daysCount"""
    if str(day_count)[-1] == "1":
        ordi = "st"
    elif str(day_count)[-1] == "2":
        ordi = "nd"
    elif str(day_count)[-1] == "3":  
        ordi = "rd"
    else:
        ordi = "th"
    new = " is the " + str(day_count) + ordi + " days of the year"
    return new

main()  