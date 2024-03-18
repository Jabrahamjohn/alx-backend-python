#!/usr/bin/env python3
"""scripting for multiple coroutines"""


import asyncio
import random

wait_random = __import__('0-basic_async_syntax.py').wait_random

async def wait_n(n: int , max_delay: int) -> float:
    """this function imports the previous file first;
    waits for random delays concurrently
    Args:
    n: the number of concurrent wait operations
    max_delay: the max delays
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

wait_random = __import__('0-basic_async_syntax.py').wait_random