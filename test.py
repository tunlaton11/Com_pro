
def score(num, note, player):
    score = [0] * num
    total = 0
    for i in range(num):
        if note[i] == player[i]:
            total += 1 + score[i - 1]
        else:
            continue
    return total


print(score(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
