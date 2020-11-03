def check_win(check_num):
    """check winner"""
    if check_num[0] == "X" and check_num[1] == "X" and check_num[2] == "X":
        return "The winner is X!!"
    elif check_num[3] == "X" and check_num[4] == "X" and check_num[5] == "X":
        return "The winner is X!!"
    elif check_num[6] == "X" and check_num[7] == "X" and check_num[8] == "X":
        return "The winner is X!!"
    elif check_num[0] == "X" and check_num[3] == "X" and check_num[6] == "X":
        return "The winner is X!!"
    elif check_num[1] == "X" and check_num[4] == "X" and check_num[7] == "X":
        return "The winner is X!!"
    elif check_num[2] == "X" and check_num[5] == "X" and check_num[8] == "X":
        return "The winner is X!!"
    elif check_num[0] == "X" and check_num[4] == "X" and check_num[8] == "X":
        return "The winner is X!!"
    elif check_num[2] == "X" and check_num[4] == "X" and check_num[6] == "X":
        return "The winner is X!!"

check_num = ["X","X","O","O","X",6,7,"O","X"]
print(check_win(check_num))