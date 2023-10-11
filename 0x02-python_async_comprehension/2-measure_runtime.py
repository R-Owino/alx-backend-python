#!/usr/bin/env python3
'''
Contains a coroutine measure_runtime that inherits from async_comprehension
'''

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension four times in parallel
    Measures the total runtime and returns it
    '''
    start_time = asyncio.get_event_loop().time()

    # Create a list of tasks for async_comprehension and run them concurrently
    num_tasks = 4
    tasks = [async_comprehension() for _ in range(num_tasks)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
