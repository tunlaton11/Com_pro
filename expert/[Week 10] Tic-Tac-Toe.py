"""[Week 10] Tic-Tac-Toe"""


def main():
    """[Week 10] Tic-Tac-Toe"""
    print("Welcome to OX!")
    count = 1
    pos_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    while True:
        if count % 2 != 0:
            print("It's X's turn!")
            mark = "X"
        else:
            print("It's O's turn!")
            mark = "O"

        num = int(input("Please enter cell number (1-9) --> "))
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