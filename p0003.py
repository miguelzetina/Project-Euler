"""
Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(x):
    if x > 1:
        divisor = 2
        for i in range(divisor, x):
            if x % i == 0:
                return False
    else:
        return False
    return True


def is_prime_of(a, b):
    return b % a == 0


def largest_prime_of(b):
    mult = 1
    for n in range(2, b):
        if is_prime(n):
            if is_prime_of(n, b):
                mult *= n
                if mult == b:
                    return n


print(largest_prime_of(600851475143))