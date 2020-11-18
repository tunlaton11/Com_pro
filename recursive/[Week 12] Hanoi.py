"""[Week 12] Hanoi"""


def hanoi_tower(disks, move1, move2, target):
    """[Week 12] Hanoi"""
    if disks == 1:
        print(move1, target)
        return

    hanoi_tower(disks - 1, move1, target, move2)
    print(move1, target)
    hanoi_tower(disks - 1, move2, move1, target)



hanoi_tower(int(input()), '1', '2', '3')
