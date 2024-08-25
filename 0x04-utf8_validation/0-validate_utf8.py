#!/usr/bin/python3
""" valid UTF-8 encoding checker """


def validUTF8(data: list[int]) -> bool:
    """ valid UTF-8 encoding checker """
    n_bytes = 0
    for i in data:
        if i > 255:
            return False
        bin_rep = format(i, '08b')
        
        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue 
            elif bin_rep[:3] == '110':
                n_bytes = 1
            elif bin_rep[:4] == '1110':
                n_bytes = 2
            elif bin_rep[:5] == '11110':
                n_bytes = 3
            else:
                return False
        else:
            if bin_rep[:2] != '10':
                return False
        
        n_bytes -= 1

    return n_bytes == 0
