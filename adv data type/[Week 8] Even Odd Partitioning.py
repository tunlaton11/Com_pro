"""[Week 8] Even Odd Partitioning"""


def main():
    """[Week 8] Even Odd Partitioning"""
    num = input()
    num_list = []
    while num != "END":
        num_list.append(int(num))
        num = input()

    even = "Even:"
    odd = "Odd:"
    for i in num_list:
        if i % 2 == 0:
            even += " " + str(i)
        else:
            odd += " " + str(i)
    print(even)
    print(odd)

main()
