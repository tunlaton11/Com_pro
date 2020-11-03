n = 1
for _ in range(3):
    print("+-+-+-+")
    for j in range(n, n + 3):
        print("|" + str(j), end='')
    print("|")
    n += 3
print("+-+-+-+")
