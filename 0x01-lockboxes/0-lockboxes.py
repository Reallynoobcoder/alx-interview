#!/usr/bin/python3
"""
Function that search and unlock boxex
returns true if all boxex are unlcok and false if not
"""


def canUnlockAll(boxes):
    """return trure if all boxes unlocked"""
    unlocked_boxes = set([0])

    boxes_to_check = [0]

    for current_box in boxes_to_check:
        for key in boxes[current_box]:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                boxes_to_check.append(key)

    return len(unlocked_boxes) == len(boxes)
