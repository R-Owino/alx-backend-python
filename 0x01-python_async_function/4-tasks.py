#!/usr/bin/env python3
'''
Contains a function task_wait_n
'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Returns the wait times in sorted order of each call to
    task_wait_random
    '''
    results = []

    for res in asyncio.as_completed([*(task_wait_random(max_delay)
                                       for _ in range(n))]):
        completed_tasks = await res
        results.append(completed_tasks)
        return results
