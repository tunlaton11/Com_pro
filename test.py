"""primes"""


def primes(num):
    """ Returns  a list of primes < n """
    if num >= 2:
        sieve = [True] * num
        for i in range(3, int(num**0.5)+1, 2):
            if sieve[i]:
                sieve[i*i::2*i] = [False]*((num-i*i-1)//(2*i)+1)

        return len([2] + [i for i in range(3, num, 2) if sieve[i]])
    else:
        return 0


print(primes(int(input())))
