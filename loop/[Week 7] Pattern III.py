"""[Week 7] Pattern III"""


def main():
    """[Week 7] Pattern III"""
    num = int(input())
    for i in range(1, num + 1):
        print(" " * (num - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for k in range(i - 1, 0, -1):
            print(k, end='')
        print()

    for re_i in range(num - 1, 0, -1):
        print(" " * (num - re_i), end='')
        for re_j in range(1, re_i + 1):
            print(re_j, end='')
        for re_k in range(re_i - 1, 0, -1):
            print(re_k, end='')
        print()

main()
