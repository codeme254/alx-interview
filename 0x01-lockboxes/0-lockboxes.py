#!/usr/bin/python3
"""
Determines if all the boxes can be unlocked
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1.
Each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    """

    boxesUnlockInformation = {}

    boxesUnlockInformation[0] = 'opened'

    for k in range(1, len(boxes)):
        boxesUnlockInformation[k] = 'closed'

    for i in range(0, len(boxes)):
        if boxesUnlockInformation[i] == 'opened':
            current_box = boxes[i]
            for i in range(0, len(current_box)):
                boxesUnlockInformation[i] = 'opened'
                newOpenBox = boxes[i]
                for i in range(0, len(newOpenBox)):
                    boxesUnlockInformation[newOpenBox[i]] = 'opened'
        else:
            # not opened
            # look for the key in all opened boxes and if you find it, open the
            # current box
            for key, value in boxesUnlockInformation.items():
                if value == 'opened':
                    # look for i and if you find it set
                    # boxesUnlockInformation[i] to opened
                    if key <= len(boxes) - 1:
                        openBox = boxes[key]
                        for j in range(0, len(openBox)):
                            if openBox[j] == i:
                                boxesUnlockInformation[i] = 'opened'

    # print(boxesUnlockInformation)
    for key, value in boxesUnlockInformation.items():
        if value == 'closed':
            return False

    return True

# canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
# canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
