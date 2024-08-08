#!/usr/bin/python3
""" lock box """


def minOperations(n):
    """ loock box """
    n = len(boxes)
    opened = set()
    opened.add(0)
    keys = [0]
 keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < n and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == n
