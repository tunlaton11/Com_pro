"""63070224"""


def is_pangram(sentence):
    alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'j', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    set_sen = set(sentence)
    if set_sen.intersection(alpha) == alpha:
        return "Pangram"
    else:
        return is_heterogram(sentence)


def is_heterogram(sentence):
    freq = list(set(sentence.replace(" ", "")))
    count = 0
    for i in freq:
        if sentence.count(i) > 1:
            break
        count += 1
        if count == len(freq):
            return "Heterogram"


def main():
    word = input().lower()
    print(is_pangram(word))


main()
