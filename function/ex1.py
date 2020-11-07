"""63070224"""
import math


def cal_area(rad):
    area = math.pi * rad ** 2
    return area


def cal_circumference(r):
    cir = 2 * math.pi * r
    return cir


def main():
    rad = float(input())
    print("Area of the circle:", "%.2f" % cal_area(rad))
    print("Circumfernce of circle:", "%.2f" % cal_circumference(rad))


main()
