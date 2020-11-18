"""63070224"""


def main():
    word = input().lower()
    print(filter_words(word))
    print(word_count(filter_words(word)))


def filter_words(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    word_new = ''
    for i in word:
        if i in alpha:
            word_new += i
        elif i == ' ':
            word_new += i
        else:
            continue
    return word_new


def word_count(word):
    word_freq = []
    count_freq = []
    word_list = word.split(" ")
    for i in word_list:
        if i not in word_freq:
            word_freq.append(i)
            count_freq.append(word_list.count(i))
        else:
            continue
    return word_freq, count_freq


if __name__ == '__main__':
    main()
