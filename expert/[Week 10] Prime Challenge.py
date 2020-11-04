"""[Week 10] Prime Challenge"""


def main():
    """[Week 10] Prime Challenge"""
    num = int(input())
    if num < 2:
        return print(0)
    elif num % 2 == 0:
        idx = [True]*(num // 2)
    else:
        idx = [True]*((num // 2)+1)
    for i in range(3, int(num**0.5) + 1, 2):
        if idx[i//2]:
            idx[i//2 + i::i] = [False] * len(idx[i//2 + i::i])
    print(idx.count(True))

main()
