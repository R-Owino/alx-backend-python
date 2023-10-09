#!/usr/bin/env python3
'''
Async basics
'''

import asyncio
import random


async def wait_random(max_delay=10):
    '''
    Async coroutine that takes in an int arg
    that waits for the random delay between 0 and max_delay
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
