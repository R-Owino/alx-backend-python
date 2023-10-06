#!/usr/bin/env python3
'''
Type annotations: TypeVar
'''

from typing import TypeVar, Union, Mapping, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''
    Safely gets a value from a dictionary 'dct' using the provided 'key'
    '''
    if key in dct:
        return dct[key]
    else:
        return default
