"""[Week 8] Map Direction"""


def main():
    """[Week 8] Map Direction"""
    lo_x = 0
    lo_y = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    move = []
    text = input().upper()
    for i in text:
        if i == "W":
            lo_x -= 1
        elif i == "S":
            lo_y -= 1
        elif i == "N":
            lo_y += 1
        else:
            lo_x += 1
        max_x = max(lo_x, max_x)
        min_x = min(lo_x, min_x)
        max_y = max(lo_y, max_y)
        min_y = min(lo_y, min_y)
        move.append((lo_x, lo_y))
    for i in range(max_y, min_y-1, -1):
        for j in range(min_x, max_x + 1):
            if (i, j) == (0, 0):
                print("B", end=" ")
            elif (j, i) == move[-1]:
                print("E", end=" ")
            elif (j, i) in move:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()
main()
