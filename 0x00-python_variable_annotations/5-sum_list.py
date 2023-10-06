#!/usr/bin/env python3
'''
Complex types - list of floats
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Takes a list of floats as an arg and returns the sum
    '''
    return float(sum(input_list))
