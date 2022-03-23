"""
Write a function solve(items) that takes items, 
a list of integers, and returns the smallest integer greater than 0 that appears in the list, 
or 0 if there is none.
"""


def solve(items):

    minimum = 0
    for i in items:
        if i > 0 and (minimum == 0 or i < minimum):
            minimum = i
    return minimum

