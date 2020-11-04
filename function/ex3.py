"""63070224"""


def sort_height(height):
    h_sort = (sorted(height))[::-1]
    str_num = [str(i) for i in h_sort]
    return ", ".join(str_num)


def median_height(height):
    h_sort = sorted(height)
    if len(h_sort) % 2 == 0:
        med = (h_sort[(len(height) + 1) // 2 - 1] +
               h_sort[(len(height) + 1) // 2]) / 2
    else:
        med = h_sort[(len(height) + 1) // 2 - 1]
    return med


def main():
    num = float(input())
    h_list = []
    while num > 0:
        h_list.append(num)
        num = float(input())
    print(sort_height(h_list))
    print(median_height(h_list))


main()
