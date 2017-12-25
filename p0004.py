"""
Problem 4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

is_palindromic = lambda num: str(num) == str(num)[::-1]


def largest_palindrome(digit_numbers):
    max_num = 10**digit_numbers
    min_num = 10**(digit_numbers-1)

    palindrome = 0
    numbers_multiply = [0, 0]

    for n in range(min_num, max_num):
        for m in range(min_num, max_num):
            multiply = n * m
            if is_palindromic(multiply):
                if multiply > palindrome:
                    palindrome = multiply
                    numbers_multiply[0] = n
                    numbers_multiply[1] = m

    print('El número palíndromo más grande formado por números de {} dígitos es {} ({}*{})'
          .format(digit_numbers, palindrome, numbers_multiply[0], numbers_multiply[1]))


largest_palindrome(1)
largest_palindrome(2)
largest_palindrome(3)
largest_palindrome(4)
