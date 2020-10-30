"""[Week 10] พ่อขุนไซเฟอร์"""


def main():
    """[Week 10] พ่อขุนไซเฟอร์"""
    word = input()
    move = int(input())
    text = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
    vo_line = 'ฯะาำเแโใไๅๆ'
    vo_up = 'ัิีึื็์'
    vo_down = 'ุู'
    van = '่้๊๋'
    num = '๐๑๒๓๔๕๖๗๘๙'


    new_word = ''
    for i in word:
        if i in text:
            new_word += text[(text.find(i) + move) % len(text)]
        elif i in vo_line:
            new_word += vo_line[(vo_line.find(i) + move) % len(vo_line)]
        elif i in vo_up:
            new_word += vo_up[(vo_up.find(i) + move) % len(vo_up)]
        elif i in vo_down:
            new_word += vo_down[(vo_down.find(i) + move) % len(vo_down)]
        elif i in van:
            new_word += van[(van.find(i) + move) % len(van)]
        elif i in num:
            new_word += num[(num.find(i) + move) % len(num)]
        else:
            new_word += i

    print(new_word)

main()
