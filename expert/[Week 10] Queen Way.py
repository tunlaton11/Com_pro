"""[Week 10] Queen Way"""


def main():
    """[Week 10] Queen Way"""
    q_row = int(input())
    q_col = int(input())
    print(" _ _ _ _ _ _ _ _")
    for i in range(8): #rows
        for j in range(8): #column
            if i == q_row and j == q_col:
                print("|" + "Q", end='')
            elif q_col == j or q_row == i or abs(q_col - j) == abs(q_row - i):
                print("|" + "x", end='')
            else:
                print("|" + "_", end='')
        print("|")

main()
