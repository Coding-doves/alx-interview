#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    calculates the fewest number of operations (copy, paste)
    """
    len_H = 1
    sum_of_copied_H = 0
    sum_of_operations = 0

    while len_H < n:
        if n % len_H == 0:
            sum_of_operations += 2
            sum_of_copied_H = len_H
        else:
            total_operations += 1
    
        len_H += sum_of_copied_H

    return total_operations
