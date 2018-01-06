"""
Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""


def letters_for_num(num):
    t_letters = 0
    hundreds = num // 100
    temp = num % 100
    tens = temp // 10
    ones = temp % 10

    if hundreds == 10:
        t_letters += 11  # one thousand
    elif hundreds == 6 or hundreds == 2 or hundreds == 1:
        t_letters += 3  # six, two, one
    elif hundreds == 9 or hundreds == 5 or hundreds == 4:
        t_letters += 4  # nine, five, four
    elif hundreds == 8 or hundreds == 7 or hundreds == 3:
        t_letters += 5  # eight, seven, three

    if 99 < num <= 1000:
        if tens + ones == 0:
            t_letters += 7  # hundred
        else:
            t_letters += 10  # hundred and

    if tens == 9 or tens == 8 or tens == 3 or tens == 2:
        t_letters += 6  # ninety, eighty, thirty, twenty
    elif tens == 4 or tens == 6 or tens == 5:
        t_letters += 5  # forty, sixty, fifty
    elif tens == 7:
        t_letters += 7  # seventy
    elif tens == 1:
        if ones == 0:
            t_letters += 3  # ten
        elif ones == 2 or ones == 1:
            t_letters += 6  # twelve, eleven
        elif ones == 9 or ones == 8 or ones == 4 or ones == 3:
            t_letters += 8  # ninteen, eighteen, fourteen, thirteen
        elif ones == 6 or ones == 5:
            t_letters += 7  # sixteen, fifteen
        elif ones == 7:
            t_letters += 9  # seventeen

    if tens != 1:
        if ones == 6 or ones == 2 or ones == 1:
            t_letters += 3  # six, two, one
        elif ones == 9 or ones == 5 or ones == 4:
            t_letters += 4  # nine, five, four
        elif ones == 8 or ones == 7 or ones == 3:
            t_letters += 5  # eight, seven, three

    return t_letters


def numbers_letters_from_to(min, max):
    sum = 0
    if max < min: min, max = max, min
    if min < 1:
        print("El rango mínimo es 1. Este será establecido.")
    for i in range(min, max+1):
        sum += letters_for_num(i)

    return sum


print(letters_for_num(1000))
print(letters_for_num(202))

letters_first_1000 = numbers_letters_from_to(1, 1000)

print(letters_first_1000)
