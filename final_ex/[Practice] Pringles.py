"""[Practice] Pringles"""


def count(potato, num):
    """return num of potato"""
    pot_count = potato[0: num]
    return pot_count.count(")")


def check_left(potato, num):
    """return potato left"""
    if potato[0: num].count(")") == potato.count(")"):
        return "None."
    else:
        return "There are still some left."


def main():
    """main"""
    upp, mid, low = input(), input(), input()
    num = int(input())
    potato = [i for i in mid if i == ")" or i == " "]

    print(count(potato, num))
    print(check_left(potato, num))
    print(upp)
    potato[0: num] = [" "] * num
    print("".join(potato) + "|")
    print(low)


main()
