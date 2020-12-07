"""[Practice] Virus"""


def check_virus(bit):
    """return num of virus"""
    virus = [0, 0, 0]  # 10101 10001 01010
    virus_point = {"10101": 0, "10001": 1, "01010": 2}
    check = ''
    for i in bit:
        check += i
        if len(check) == 5:
            if check in virus_point:
                virus[virus_point[check]] += 1
                check_virus(bit.replace(check, "", 1))
            else:
                check_virus(bit.replace(bit[0], ""))
            check = ''

    return virus


def main():
    """main"""
    bit = ''
    num = input()
    while num != "NULL":
        bit += num
        num = input()
    result = check_virus(bit)
    print(*result, sep='\n')


main()
