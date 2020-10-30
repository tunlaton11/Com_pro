"""[Week 8] Backspace"""


def main():
    """[Week 8] Backspace"""
    text = input()
    text_list = [i for i in text]
    count_text = text.count("<")
    for _ in range(count_text):
        del text_list[text_list.index("<") - 1: text_list.index("<") + 1]

    print("".join(text_list))

main()
