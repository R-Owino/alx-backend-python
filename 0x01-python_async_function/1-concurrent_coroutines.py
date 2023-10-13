#!/usr/bin/env python3
'''
async: multiple coroutines
'''

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    This function spawns 'wait_random' coroutine n times with the specified
    max_delay and returns a list of delays
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    sorted_delays = sorted(results)
    return sorted_delays
