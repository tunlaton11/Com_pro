"""[Week 11] Bowling"""


def result(log, rep, i):
    """[Week 11] Bowling"""
    keep = 0
    bow = 10
    if i == "X":
        for i in rep[log: log+2]:
            if i == "X":
                keep += 10
            elif i == "/":
                keep += bow
            elif i == "-":
                keep += 0
            else:
                keep += int(i)
                bow -= int(i)
        return keep
    else:
        for i in rep[log: log+1]:
            if i == "X":
                keep += 10
            elif i == "/":
                keep += bow
            elif i == "-":
                keep += 0
            else:
                keep += int(i)
                bow -= int(i)
        return keep


def main():
    """[Week 11] Bowling"""
    frame = input()
    score = 0
    count = 1
    ball = 10
    rep = frame.replace(" ", "")
    log = 0
    for i in frame:
        if count <= 9:
            if i == " ":
                count += 1
                ball = 10
            elif i == "X":
                log += 1
                score += 10 + result(log, rep, i)
            elif i == "/":
                log += 1
                score += ball + result(log, rep, i)
            elif i == "-":
                log += 1
                score += 0
            else:
                log += 1
                score += int(i)
                ball -= int(i)
        else:
            if i == "X":
                score += 10
            elif i == "/":
                score += ball
                ball = 10
            elif i == "-":
                score += 0
            else:
                score += int(i)
                ball -= int(i)
    print(score)


main()
