#!/usr/bin/env python3
"""async_comprehension"""

async_generator = __import__("0-async_generator").async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers
    then return the 10 random numbers."""
    return [x async for x in async_generator()]
