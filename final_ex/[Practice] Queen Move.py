"""[Practice] Queen Mpve"""


def main():
    """main"""
    num = input()
    q_row = int(num[0])
    q_col = int(num[2])
    print(" _ _ _ _ _ _ _ _")
    for i in range(1, 9):
        for j in range(1, 9):
            if i == q_row and j == q_col:
                print("|" + "Q", end='')
            elif q_col == j or q_row == i or abs(q_col - j) == abs(q_row - i):
                print("|" + "+", end='')
            else:
                print("|" + "_", end='')
        print("|")


main()
