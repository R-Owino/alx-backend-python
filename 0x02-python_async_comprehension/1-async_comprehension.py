#!/usr/bin/env python3
'''
Contains a coroutine async_comprehension that inherits from async_generator
'''

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collects 10 random numbers using an async comprehensing over
    async_generator and returns the numbers
    '''
    random_numbers = [number async for number in async_generator()]

    return random_numbers
