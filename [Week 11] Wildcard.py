"""[Week 11] Wildcard"""


def main():
    """[Week 11] Wildcard"""
    num = int(input())
    part = input()
    lisx = part.split("*")
    for _ in range(num):
        word = input()
        if word.startswith(lisx[0]) and word.endswith(lisx[1]) and len(word) >= len(part)-1:
            print("YES")
        else:
            print("NO")
main()
