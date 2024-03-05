#!/usr/bin/python3
'''
making change

testcase
print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
print(makeChange([1, 2, 25], 0))
print(makeChange([1, 2, 5], 3))
print(makeChange([1, 2, 10], 11)) -> 2
'''


def makeChange(coins, total) -> int:
    '''
    Finding smallest amount
    to change.
    Sort and Reverse coins list
    Loop through, div total by each coin
    Add the answer -> change += total / one_coin
    New total = total % one_coin
    return change if total == 0
    '''
    change = 0

    sort_n_reverse = sorted(coins, reverse=True)

    for one_coin in sort_n_reverse:
        if total <= 0:
            return change

        # if one_coin <= total: ->optional
        change += total // one_coin
        total = total % one_coin

    if total == 0:  # Check if total is zero after using all the coins
        return change
    else:
        return -1
