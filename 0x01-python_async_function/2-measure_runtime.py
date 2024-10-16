#!/usr/bin/env python3
"""measures the total execution time"""

import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures single runtime"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
