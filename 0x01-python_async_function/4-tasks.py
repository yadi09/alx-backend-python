#!/usr/bin/env python3
"""spawn wait_random n times with the specified max_delay"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times"""
    list = []
    delaies = []

    for _ in range(n):
        list.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(list):
        delay = await task
        delaies.append(delay)

    return delaies
