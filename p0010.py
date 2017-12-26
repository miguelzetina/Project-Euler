"""
Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def criba_de_eratostenes(number):
    """
    La Criba de Eratóstenes sirve para recoger los números primos debajo de un
    número n (incluyendolo si así se desea).
    """
    multiples = set()
    primes = []
    for i in range(2, number):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, number, i))
    return primes


def sum_primes_below_of(number):
    return sum(criba_de_eratostenes(number))


number = 2000000

print(sum_primes_below_of(number))  # 142913828922
