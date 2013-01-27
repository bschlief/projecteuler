import itertools
import math

goal = 64 

# Courtest of StackOverflow.  Enumerate is a cute trick.
def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False    

# Courtesty of wikipedia
def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n == 1: return [1]
    primes = list(primes_sieve(int(n**0.5) + 1))
    prime_factors = []
 
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)
 
    return prime_factors


print trial_division(600851475143)

