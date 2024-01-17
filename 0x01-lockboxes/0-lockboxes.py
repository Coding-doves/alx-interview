#!/usr/bin/python3

'''Lock Boxes'''


def canUnlockAll(boxes):
    '''if boxes is not a list'''
    if type(boxes) != list:
        return False

    opened_boxes = set()  # to remove duplicate keys
    keys = [0]  # first key is 0

    while keys:
        '''
        pop a key and append(unlock a box)
        and add to oppened_boxes
        '''
        get_key = keys.pop()
        opened_boxes.add(get_key)

        if type(boxes[get_key]) != list:
            return False

        # if new key is unique add it to keys array
        for k in boxes[get_key]:
            if (k < len(boxes)) and (k not in opened_boxes)\
             and (k not in keys):
                keys.append(k)

    '''
    if the number of boxes opened/unlocked
    is to the boxes passed as argument return true
    '''
    return len(opened_boxes) == len(boxes)
