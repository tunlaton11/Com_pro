def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False

        else:
            return True
    else:
        return False


def main():
    num = int(input())
    print(check_prime(num))


if __name__ == "__main__":
    main()
