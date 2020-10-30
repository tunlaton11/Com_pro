"""[Week 10] Classroom"""


def main():
    """[Week 10] Classroom"""
    num = int(input())
    num_array = []
    for member in range(num):
        num_array.append([])
        for _ in range(num):
            num_array[member].append(int(input()))

    num_array_t = [list(i) for i in zip(*num_array)] #Transpose_array__

    left = [min(i) for i in num_array]
    right = [max(j) for j in num_array_t]

    if max(left) == min(right):
        print(max(left))
    else:
        print("404 Not Found!")

main()
