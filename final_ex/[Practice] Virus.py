"""[Practice] Virus"""


def check_virus(bit):
    """return num of virus"""
    virus = [0, 0, 0]  # 10101 10001 01010
    for i in range(len(bit) - 5):
        idx = 0
        check = "".join(bit[idx: i+5])
        if check == "10101":
            virus[0] += 1
            idx =
        elif check == "10001":
            virus[1] += 1

        elif check == "01010":
            virus[2] += 1

        else:

    return virus


def main():
    """main"""
    bit = []
    num = input()
    while num != "NULL":
        bit.append(num)
        num = input()
    result = check_virus(bit)
    print(*result, sep='\n')


main()
