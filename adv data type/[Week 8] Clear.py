"""[Week 8] Clear"""


def main():
    """[Week 8] Clear"""
    num = input()
    num_list = []
    while num != "END":
        if num == "clear":
            num_list = []
        else:
            num_list.append(num)
        num = input()

    if num_list == []:
        print("list is empty")
    else:
        for i in num_list:
            print(i)

main()
