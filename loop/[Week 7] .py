"""[Week 7] *"""


def main():
    """[Week 7] *"""
    text = input().upper()
    count = 0
    for i in range(len(text) - 1, 0, - 1):
        line = 2 * len(text) - 3
        print(" " * count + text[i] + " " * (line - count) + text[i] + " " *
              (line - count) + text[i])
        count += 2
    for j in text[::-1]:
        print(j, end=' ')
    for k in text[1:]:
        print(k, end=' ')
    print()
    count = line - 1
    for re_i in range(1, len(text)):
        print(" " * count + text[re_i] + " " * (line - count) + text[re_i] +
              " " * (line - count) + text[re_i])
        count -= 2
main()
