#!/usr/bin/env python3
"""Defines a function that measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n.
"""
import asyncio
import time
from typing import List, Any
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)
    Args:
        n(int): number of times function spawned
        max_delay(int): integer argument
    Returns:
        Returns total_time / n
    """
    s: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - s
    return total_time / n
