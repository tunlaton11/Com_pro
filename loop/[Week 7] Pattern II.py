"""[Week 7] Pattern II"""


def main():
    """[Week 7] Pattern II"""
    num = int(input())
    count = 1
    for i in range(0, num):
        count = 1
        print(" " * (num - i -1), end='')
        for _ in range(0, i + 1):
            print(str(count), end=' ')
            count += 1
        print()

main()
