"""[Week 10] Tic-Tac-Toe"""

def check_win(check_num):
    """check winner"""
    if check_num[0] == "X" and check_num[1] == "X" and check_num[2] == "X":
        return True
    elif check_num[3] == "X" and check_num[4] == "X" and check_num[5] == "X":
        return True
    elif check_num[6] == "X" and check_num[7] == "X" and check_num[8] == "X":
        return True
    elif check_num[0] == "X" and check_num[3] == "X" and check_num[6] == "X":
        return True
    elif check_num[1] == "X" and check_num[4] == "X" and check_num[7] == "X":
        return True
    elif check_num[2] == "X" and check_num[5] == "X" and check_num[8] == "X":
        return True
    elif check_num[0] == "X" and check_num[4] == "X" and check_num[8] == "X":
        return True
    elif check_num[2] == "X" and check_num[4] == "X" and check_num[6] == "X":
        return True
    else:
        False

def check_win_2(check_num):
    """check winner"""
    if check_num[0] == "O" and check_num[1] == "O" and check_num[2] == "O":
        return True
    elif check_num[3] == "O" and check_num[4] == "O" and check_num[5] == "O":
        return True
    elif check_num[6] == "O" and check_num[7] == "O" and check_num[8] == "O":
        return True
    elif check_num[0] == "O" and check_num[3] == "O" and check_num[6] == "O":
        return True
    elif check_num[1] == "O" and check_num[4] == "O" and check_num[7] == "O":
        return True
    elif check_num[2] == "O" and check_num[5] == "O" and check_num[8] == "O":
        return True
    elif check_num[0] == "O" and check_num[4] == "O" and check_num[8] == "O":
        return True
    elif check_num[2] == "O" and check_num[4] == "O" and check_num[6] == "O":
        return True
    else:
        return False

def main():
    """[Week 10] Tic-Tac-Toe"""
    print("Welcome to OX!\n")
    pos_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(len(pos_array)):
        print("+-+-+-+")
        for j in range(3):
            print("|" + str(pos_array[i][j]), end='')
        print("|")
    print("+-+-+-+\n")

    winner = ''
    count = 1
    is_win = ''
    while is_win == '':
        check_num = [num_j for num_i in pos_array for num_j in num_i]
        if check_win(check_num) == True:
            winner = 'The winner is X!!'
            break

        elif check_win_2(check_num) == True:
            winner = 'The winner is O!!'
            break
        elif count == 10:
            winner = 'Draw!!'
            break

        if count % 2 != 0:
            print("It's X's turn!")
            mark = "X"
        else:
            print("It's O's turn!")
            mark = "O"

        num = int(input("Please enter cell number (1-9) --> "))
        if not(1 <= num <= 9) or check_num[num - 1] == "X" or check_num[num - 1] == "O":
            continue
        else:
            for i in range(len(pos_array)):
                print("+-+-+-+")
                for j in range(3):
                    if pos_array[i][j] == num:
                        print("|" + mark, end='')
                        pos_array[i][j] = mark
                    else:
                        print("|" + str(pos_array[i][j]), end='')
                print("|")
            print("+-+-+-+\n")
            count += 1
    print(winner)

main()
