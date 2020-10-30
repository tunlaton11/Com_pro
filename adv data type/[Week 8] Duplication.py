""""[Week 8] Duplication"""


def main():
    """[Week 8] Duplication"""
    num = []
    num_uniq = []
    for _ in range(16):
        num.append(int(input()))

    for i in num:
        if num.count(i) > 1:
            if i not in num_uniq:
                num_uniq.append(i)
    if num_uniq != []:
        for j in sorted(num_uniq):
            print(j)

main()
