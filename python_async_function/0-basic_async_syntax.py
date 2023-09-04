#!/usr/bin/env python3
""" basic async syntax """


import asyncio
import random


async def wait_random(max_delay = 10):
    """ waits a random time """
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay
