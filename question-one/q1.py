#!/usr/bin/env python3

'''
    Interview Question 1 of python:
        TODO:
            1. write a function that takes list of integers as input and returns the sum of all the integers in the list for the even numbers.
'''

def sum_even_numbers(list_of_integers):
    '''
        Function to sum all the even numbers in the list of integers assuming all the integers are positive numbers.

        Args:
            list_of_integers: list of integers.

        Returns:
            sum of all the even numbers in the list.
    '''

    sum_of_even_numbers = 0

    for i in list_of_integers:
        if i % 2 == 0:
            sum_of_even_numbers += i

    return sum_of_even_numbers

'''
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(arr))
'''
