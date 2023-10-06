#!/usr/bin/env python3
'''
Duck type an interable object
'''

from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Takes an iterable object and returns a list of tuples
    '''
    return [(i, len(i)) for i in lst]
