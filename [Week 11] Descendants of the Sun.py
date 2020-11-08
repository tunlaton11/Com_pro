"""[Week 11] Descendants of the Sun"""


import math


def check_direct(lat1, lat2, lon1, lon2): #check direction of lat and lon
    """[Week 11] Descendants of the Sun"""
    if lon2 == lon1 and lat2 > lat1:
        direct = "N"
    elif lon2 > lon1 and lat2 > lat1:
        direct = "NE"
    elif lon2 > lon1 and lat2 == lat1:
        direct = "E"
    elif lon2 > lon1 and lat2 < lat1:
        direct = "SE"
    elif lon2 == lon1 and lat2 < lat1:
        direct = "S"
    elif lon2 < lon1 and lat2 < lat1:
        direct = "SW"
    elif lon2 < lon1 and lat2 == lat1:
        direct = "W"
    elif lon2 < lon1 and lat2 > lat1:
        direct = "NW"
    return direct


def check_result(lat1, lat2, lon1, lon2):
    """[Week 11] Descendants of the Sun"""
    rad = 6378.137
    result = 2 * rad * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2 + \
             math.cos(lat1)*math.cos(lat2)*math.sin((lon2 - lon1) / 2) ** 2))
    return "%.2f" % result + "km"


def main():
    """[Week 11] Descendants of the Sun"""
    num = int(input())
    if 1 <= num <= 10:
        data = []
        sub = []
        for _ in range(num + 1):
            word = input()
            for j in word.split(", "):
                word = float(j.replace("(", "").replace(")", ""))
                sub.append(word)
            data.append(tuple(sub))
            sub = []

        for i in range(num):
            lat1 = math.radians(data[i][0])
            lon1 = math.radians(data[i][1])
            lat2 = math.radians(data[i+1][0])
            lon2 = math.radians(data[i+1][1])
            print("#" + str(i + 1) + " Distance:", check_result(lat1, lat2, lon1, lon2),
                  "Direction:", check_direct(lat1, lat2, lon1, lon2))


main()
