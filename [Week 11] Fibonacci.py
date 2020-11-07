"""[Week 11] Fibonacci"""


def fibonacci(num):
    """[Week 11] Fibonacci"""
    if num >= 0:
        if num == 1:
            return 0
        elif num == 2:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    """[Week 11] Fibonacci"""
    print(fibonacci(int(input()) + 1))

main()
