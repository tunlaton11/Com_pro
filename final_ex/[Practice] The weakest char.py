"""[Practice] The weakest char"""


def main():
    """main"""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    word = input()
    word_value = alpha.find(word) + 1
    if word not in alpha:
        print(word)
    else:
        for i in range(word_value):
            print(" " * (word_value - i - 1), end='')
            for j in range(i + 1):
                print(alpha[j], end='')
            for k in range(i-1, -1, -1):
                print(alpha[k], end='')
            print()
        for i in range(word_value - 1, 0, -1):
            print(" " * (word_value - i), end='')
            for j in range(i):
                print(alpha[j], end='')
            for k in range(i-1, 0, -1):
                print(alpha[k-1], end='')
            print()


main()
