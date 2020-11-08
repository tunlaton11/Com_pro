"""[Week 11] Casino"""

def check_pos(pos, move):
    """[Week 11] Casino"""
    if pos == "L":
        pos_list = ["O", "X", "X"]
    elif pos == "C":
        pos_list = ["X", "O", "X"]
    elif pos == "R":
        pos_list = ["X", "X", "O"]

    for i in move:
        if i == "A":
            pos_list[0], pos_list[1] = pos_list[1], pos_list[0]
        elif i == "B":
            pos_list[1], pos_list[2] = pos_list[2], pos_list[1]
        elif i == "C":
            pos_list[0], pos_list[2] = pos_list[2], pos_list[0]

    if pos_list.index("O") == 0:
        return "L"
    if pos_list.index("O") == 1:
        return "C"
    if pos_list.index("O") == 2:
        return "R"


def main():
    """[Week 11] Casino"""
    pos = input()
    move = input()
    print(check_pos(pos, move))

main()
