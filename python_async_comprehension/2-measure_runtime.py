#!/usr/bin/env python3
""" async generator """


import time
from typing import List
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ yields random number after waiting """
    start = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = time()
    return end - start
