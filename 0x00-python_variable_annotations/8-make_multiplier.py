#!/usr/bin/env python3
'''
Complex types - functions
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Takes a float arg and returns a function that multiplies a float
    by the arg
    '''
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
