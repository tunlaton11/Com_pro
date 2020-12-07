bit = ''
num = input()
while num != "NULL":
    bit += num
    num = input()

virus = [0, 0, 0]  # 10101 10001 01010
virus_point = {"10101": 0, "10001": 1, "01010": 2}
check = ''
for i in bit:
    check += i
    if len(check) == 5:
        if check in virus_point:
            virus[virus_point[check]] += 1
            bit.replace(check, "", 1)
        else:
            bit.replace(check, check[1:5], 1)
        check = ''

print(virus)
