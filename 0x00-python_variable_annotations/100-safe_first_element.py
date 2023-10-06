#!/usr/bin/env python3
'''
More duck types
'''
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Takes a sequence 'lst' as input and returns its first element,
    if it exists, or None if the sequence is empty
    '''
    if lst:
        return lst[0]
    else:
        return None
