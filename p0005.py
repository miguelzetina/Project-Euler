"""
Problem 5: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def number_divisible(num, max, min=1):
    for n in range(min, max):
        if num % n != 0:
            return False
    return True


def smallest_multiple(max, min=1):
    num = 0
    while True:
        num += max
        # print(num)
        if number_divisible(num, max, min):
            # print("El número {} es divisible total".format(num))
            break
    print('El número más chico que es posible dividir con todos los números '
          'de {} a {} es {}'.format(min, max, num))


smallest_multiple(20, 1)
