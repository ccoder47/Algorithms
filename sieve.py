def sieve_of_eratosthenes(n):
    """
    Finds all primes up to n by marking multiples.
    Time: O(n log log n), Space: O(n)
    """
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if sieve[p]:
            for multiple in range(p*p, n+1, p):
                sieve[multiple] = False
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


if __name__ == "__main__":
    print("Primes up to 50:", sieve_of_eratosthenes(50))
