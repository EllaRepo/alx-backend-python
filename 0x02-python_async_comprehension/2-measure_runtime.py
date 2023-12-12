#!/usr/bin/env python3
"""Defines a coroutine that coroutine that will execute async_comprehension
   four times in parallel using asyncio.gather
"""
import asyncio
import time
from typing import List

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using asyncio.gather
    Args:
        None
    Returns:
        the total runtime
    """
    s: float = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comp(),
        async_comp(),
        async_comp(),
        async_comp()
    )
    return asyncio.get_event_loop().time() - s
