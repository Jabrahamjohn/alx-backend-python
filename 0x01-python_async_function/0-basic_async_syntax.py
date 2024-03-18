#!/usr/bin/env python3
"""this script is for basic async learning"""


import random

async def wait_random(max_delay: int = 10) -> float:
    """ this function is asynchronous that:
    waits for a random delay between 0 and a max_delay
    and eventually returns the delay in seconds
    Args:
    max-delay: the interger delay maximum time
    Returns:
    delay: the delay time to in float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
