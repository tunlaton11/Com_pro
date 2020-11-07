"""[Week 11] Wildcard"""


def main():
    """[Week 11] Wildcard"""
    num = int(input())
    part = input()
    check = part.split("*")
    for _ in range(num):
        word = input()
        if word.startswith(check[0]) and word.endswith(check[1]) and len(word) >= l -1:
            print("YES")
        else:
            print("NO")
main()
