#!/usr/bin/env python3
'''
Measures the runtime
'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 0) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay)
    Returns total_time / n
    '''
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start_time) / n
