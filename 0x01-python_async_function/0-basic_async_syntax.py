#!/usr/bin/env python3
"""Defines a function an asynchronous coroutine that takes in an integer
   argument that waits for a random delay between 0 and max_delay seconds
   and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """waits for a random delay between 0 and max_delay seconds and
       eventually returns it.
    Args:
        max_delay(int): integer argument
    Returns:
        Random float number
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay