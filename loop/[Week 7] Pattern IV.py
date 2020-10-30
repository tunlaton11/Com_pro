"""[Week 7] Pattern IV"""


def main():
    """[Week 7] Pattern IV"""
    num = int(input())
    mid = int((num + 1) / 2)
    if num % 2 != 0:
        count = 0
        for i in range(num, mid - 1, - 1):
            for j in range(i, mid - count - 1, - 1):
                print(j, end=' ')
            for k in range(mid + 1 - count, i + 1):
                print(k, end=' ')
            count += 1
            print()

        count = 0
        for re_i in range(mid + 1, num + 1):
            for re_j in range(re_i, count + 1, - 1):
                print(re_j, end=' ')
            for re_k in range(count + 3, re_i + 1):
                print(re_k, end=' ')
            count += 1
            print()
main()
