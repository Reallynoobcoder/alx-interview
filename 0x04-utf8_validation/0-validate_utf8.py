#!/usr/bin/python3
"""
A function that checks if a data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return true if data is valid."""
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if (byte & 0b10000000) == 0:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            num_bytes -= 1
    return num_bytes == 0
