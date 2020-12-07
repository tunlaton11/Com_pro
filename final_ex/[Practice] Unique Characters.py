"""[Practice] Unique Characters"""


def main():
    """main"""
    text = input()
    uniq = ''
    i = 0
    while i < len(text):
        count = 1
        if i == len(text) - 1:
            break
        while text[(i+count) % len(text)] == text[i]:
            uniq = text[i] * count
            uniq += text[i]
            count += 1
            if count == len(text):
                break
        if uniq != '':
            text = text.replace(uniq, '')
            print(text)
            uniq = ''
            i = 0

        else:
            i += 1
            continue


main()
