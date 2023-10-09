#!/usr/bin/env python3
'''
Contains a function task_wait_random
'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Function that takes an integer and returns the class of the task
    '''
    return asyncio.create_task(wait_random(max_delay))
