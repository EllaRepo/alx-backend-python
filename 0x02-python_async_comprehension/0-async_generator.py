#!/usr/bin/env python3
"""Defines a coroutine will loop 10 times, each time asynchronously wait 1
   second, then yield a random number between 0 and 10
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine will loop 10 times, each time asynchronously wait 1 second,
       then yield a random number between 0 and 10
    Args:
        None
    Returns:
        Random float number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
