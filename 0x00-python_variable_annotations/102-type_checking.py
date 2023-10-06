#!/usr/bin/env python3
'''
mypy validation
'''

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Function update to validate using mypy
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # use a tuple instead of a list

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # use an int as the factor
