#!/usr/bin/env python3
"""scripting for multiple coroutines"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int , max_delay: int) -> list[float]:
    """this function imports the previous file first;
    waits for random delays concurrently
    Args:
    n: the number of concurrent wait operations
    max_delay: the max delays
    """
    delays_times = await asyncio.gather(*tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(delays_times)
