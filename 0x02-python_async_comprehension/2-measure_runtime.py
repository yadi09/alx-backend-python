#!/usr/bin/env python3
"""measure runtime"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """measure runtime"""
    list = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]

    start_time = time.time()

    await asyncio.gather(*list)

    end_time = time.time()
    runtime = end_time - start_time

    return runtime
