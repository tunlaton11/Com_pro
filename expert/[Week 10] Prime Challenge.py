"""[Week 10] Prime Challenge"""


def main():
    """[Week 10] Prime Challenge"""

    num = int(input())
    prime_count = 0

    for i in range(1, num + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                prime_count += 1
    print(prime_count)

main()
