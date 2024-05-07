#!/usr/bin/env python3

'''
    Interview Question 2 of python:
        TODO:
                1. Implement a function using merge sort algorithm to sort a list of integers.
'''

def merge_sort(arr):
    '''
        Function to sort a list of integers using merge sort algorithm.
            not handling the case where the list contains duplicate numbers.
            positive integers only for this implementation.

        Args:
            arr: list of integers.

        Returns:
            sorted list of integers.
    '''

    length = len(arr)
    mptr = length // 2
    larr = arr[:mptr]
    rarr = arr[mptr:]

    '''
        Base case:
            If the length of the list is greater than 0 and equals to 1, return the list.
    '''
    if length == 1 and length > 0:
        return arr

    '''
        Recursive case:
            If the length of the list is greater than 1, recursively call the merge_sort function.
    '''
    lptr = merge_sort(larr)
    rptr = merge_sort(rarr)

    merged_arr = []
    lptr_index = 0
    rptr_index = 0

    '''
        Loop through the left and right pointers to merge the list.
    '''
    while lptr_index < len(lptr) and rptr_index < len(rptr):
        if lptr[lptr_index] < rptr[rptr_index]:
            merged_arr.append(lptr[lptr_index])
            lptr_index += 1
        else:
            merged_arr.append(rptr[rptr_index])
            rptr_index += 1

    merged_arr += lptr[lptr_index:]
    merged_arr += rptr[rptr_index:]

    return merged_arr

'''
    Test case:
        arr = [9, 7, 3, 10, 1, 6, 5, 8, 2, 4]
        arr1 = [9]
        arr2 = [9, 7]
        arr3 = [9, 3, 1, 6, 10]
        arr4 = [9, 3, 1, 6, 10, 6, 9]
        print(merge_sort(arr))
        print(merge_sort(arr1))
        print(merge_sort(arr2))
        print(merge_sort(arr3))
        print(merge_sort(arr4))
'''
