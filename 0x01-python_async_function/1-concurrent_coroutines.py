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
    delays = {}
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    for i, delay in enumerate(results):
        delays[i] = delay

    sorted_delays = [delay for _, delay in sorted(delays.items())]
    return sorted_delays
