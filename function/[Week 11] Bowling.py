"""[Week 11] Bowling"""


def bowling_score(line):
    """[Week 11] Bowling""" #test
    score = 0
    for i in range(len(line)):
        if line[i] == 'X':
            line[i] = 10
        elif line[i] == '-':
            line[i] = 0
        elif line[i] == '/':
            continue
        else:
            line[i] = int(line[i])
    for j in range(len(line)):
        ball = line[j]
        if len(line) - 3 <= j:
            if ball == '/':
                score += (10 - line[j - 1])
            else:
                score += ball
            continue
        elif ball == 10:
            score += ball
            score += line[j + 1]
            if line[j + 2] == '/':
                score += (10 - line[j + 1])
            else:
                score += line[j + 2]
        elif ball == '/':
            score += (10 - line[j - 1])
            score += line[j + 1]
        else:
            score += ball
    return score


def main():
    """[Week 11] Bowling"""
    line = list(''.join(input().split()))
    print(bowling_score(line))


main()
