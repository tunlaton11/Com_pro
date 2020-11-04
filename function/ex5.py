"""63070224"""


def is_prime(n):
    if n > 1:
        for j in range(2, n):
            if (n % j) == 0:
                return False
                break
        else:
            return True


def main():
    num = int(input())
    print("Primes: ", end='')
    for n in range(2, num + 1):
        if is_prime(n) == True:
            print(n, end=' ')
        else:
            continue


main()
