"""[Week 8] Tanabata"""


def main():
    """[Week 8] Tanabata"""
    word = input()
    word_split = word.split(".")
    max_len_list = [len(i) for i in word_split]
    max_len = max(max_len_list)

    for i in range(len(word_split)):
        for _ in range(max_len - len(word_split[i])):
            word_split[i] += " "
    print("_|_ " * len(word_split))

    for j in range(max_len):
        for k in range(len(word_split)):
            print("|" + word_split[k][j] + "|", end=' ')
        print()
    print("|_| " * len(word_split))

main()
