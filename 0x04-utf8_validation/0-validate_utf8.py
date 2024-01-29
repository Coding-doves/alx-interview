#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    '''
    0x80 is 1-byte - 10_000_000
    0xC0 is 2-byte - 11_000_000
    0xE0 is 3-byte - 11_100_000
    0xF0 is 4-byte - 11_110_000
    '''

    i = 0

    while i < len(data):
        # is graphing contained in one byte
        if data[i] & 0x80 == 0x00:
            i += 1
        # is graphing contained in two byte
        elif data[i] & 0xE0 == 0xC0:
            if i + 1 >= len(data) or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        # is graphing contained in 3 byte
        elif data[i] & 0xF0 == 0xE0:
            if 1 + 2 >= len(data) or data[i + 1] & 0xC0 != 0x80\
                    or data[i + 2] & 0xC0 != 0x80:
                return False
            i += 3
        # is graphing contained in 4 byte
        elif data[i] & 0xF8 == 0xF0:
            if i + 3 >= len(data) or data[i + 1] & 0xC0 != 0x80\
                    or data[i + 2] & 0xC0 != 0x80 or data[i + 3]\
                    & 0xC0 != 0x80:
                return False
            i += 4
        else:
            return False
    return True
