#!/usr/bin/env python3
"""Defines a function an async routine that spawn wait_random n times
   with the specified max_delay
"""
import asyncio
from typing import List, Any
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay
    Args:
        n(int): number of times function spawned
        max_delay(int): integer argument
    Returns:
        The list of all the delays (float values)
    """
    delays: List[float] = []

    async def wait_and_append(delay):
        result = await wait_random(delay)
        delays.append(result)

    tasks: List[Any] = [wait_and_append(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)

    return delays
