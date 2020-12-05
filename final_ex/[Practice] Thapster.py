"""[Practice] Thapster"""


def check_score(num, note, player):
    """return score"""
    score = [0] * num
    for i in range(num):
        if note[i] == player[i]:
            score[i] = 1 + score[i-1]
        else:
            continue
    return sum(score)


def main():
    """main"""
    count = int(input())
    total = []
    for _ in range(count):
        num = int(input())
        note, player = input().split(" "), input().split(" ")
        total.append(check_score(num, note, player))
    print(*total, sep="\n")


main()
