"""
Problem 7: 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.
What is the 10 001st prime number?
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


def prime_number(number):
    x = 0
    count = 0
    while count != number:
        x += 1
        if is_prime(x):
            count += 1
    return x


print(prime_number(1001))
