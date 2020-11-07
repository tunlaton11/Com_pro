"""[Week 11] Descendants of the Sun"""


import math


def direct(lat1, lat2, lon1, lon2):
    """[Week 11] Descendants of the Sun"""
    dLon = (lon2 - lon1)
    y_num = math.sin(dLon) * math.cos(lat2)
    x_num = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)
    bearing = int((math.atan2(y_num, x_num) * 180 / math.pi + 360) % 360)
    if bearing == 0:
        direct = "N"
    elif 0 < bearing < 90:
        direct = "NE"
    elif bearing == 90:
        direct = "E"
    elif 90 < bearing < 180:
        direct = "SE"
    elif bearing == 180:
        direct = "S"
    elif 180 < bearing < 270:
        direct = "SW"
    elif bearing == 270:
        direct = "W"
    elif 270 < bearing < 360:
        direct = "NW"
    return direct


def result(lat1, lat2, lon1, lon2):
    """[Week 11] Descendants of the Sun"""
    rad = 6378.137
    result = 2 * rad * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2 - lon1) / 2) ** 2))
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
            print("#" + str(i + 1) + " Distance:", result(lat1, lat2, lon1, lon2), "Direction:", direct(lat1, lat2, lon1, lon2))


main()
