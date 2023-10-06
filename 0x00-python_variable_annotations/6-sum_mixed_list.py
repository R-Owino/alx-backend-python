#!/usr/bin/env python3
'''
Complex types - mixed list
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''
    Takes a list of floats and integers as an arg and returns the sum
    '''
    return float(sum(mxd_lst))
