"""[Week 10] Tic-Tac-Toe"""


def main():
    """[Week 10] Tic-Tac-Toe"""
    print("Welcome to OX!")
    count = 1
    pos_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    check_num = []
    while True:
        if count % 2 != 0:
            print("It's X's turn!")
            mark = "X"
        else:
            print("It's O's turn!")
            mark = "O"

        check_num = [num_j for num_i in pos_array for num_j in num_i]
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

main()