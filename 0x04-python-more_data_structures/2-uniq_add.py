#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_numbers = []
    total = 0

    for number in my_list:

        if number not in unique_numbers:
            unique_numbers.append(number)
            total += number

    return total
