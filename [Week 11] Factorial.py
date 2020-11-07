"""[Week 11] Factorial"""

def factorial(num):
    """[Week 11] Factorial"""
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(int(input())))
