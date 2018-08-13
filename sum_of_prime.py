from math import sqrt


def sieve_of_eratosthenes(n):
    prime = [True] * (n+1)
    prime[:2] = [False] * 2

    for i in range(2, int(sqrt(n)) + 1):
        if prime[i]:
            for j in range(i*2, n + 1, i):
                prime[j] = False
    return [x for x in range(n+1) if prime[x]]


def sum_primes(primes, n):
    s = 0
    for p in primes:
        if p <= n:
            s += p
    return s


primes = sieve_of_eratosthenes(1000000)

