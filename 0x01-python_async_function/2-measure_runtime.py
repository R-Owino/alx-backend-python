#!/usr/bin/env python3
'''
Measures the runtime
'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 0) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay)
    Returns total_time / n
    '''
    start_time = time.time()

    # Run wait_n(n, max_delay) to measure its execution time
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate the average time per execution
    average_time = total_time / n

    return average_time
