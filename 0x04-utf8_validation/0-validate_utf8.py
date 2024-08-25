#!/usr/bin/python3


"""
This module contains a function to
check if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): A list of integers, where each integer  byte

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0
    for i in data:
        if i > 255:
            return False  # Invalid byte value

        bin_rep = format(i, '08b')  # Get the binary representation

        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue  # 1-byte character
            elif bin_rep[:3] == '110':
                n_bytes = 1  # 2-byte character
            elif bin_rep[:4] == '1110':
                n_bytes = 2  # 3-byte character
            elif bin_rep[:5] == '11110':
                n_bytes = 3  # 4-byte character
            else:
                return False  # Invalid start byte
        else:
            # Continuation byte must start with '10'
            if bin_rep[:2] != '10':
                return False

        n_bytes -= 1  # Decrease the number of bytes to process

    # If n_bytes is not 0, then we have an incomplete character
    return n_bytes == 0
