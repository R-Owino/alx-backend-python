#!/usr/bin/env python3
'''
Complex types - string and int/float to tuple
'''

from typing import List, Tuple, Union


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[str, float]:
    '''
    Takes a string and int/float and returns a tuple
    containing both starting with the str, then a float
    '''
    return (k, v**2)
