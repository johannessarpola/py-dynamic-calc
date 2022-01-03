import numpy as np
import asyncio
from scipy import mean


async def operation(*args):
    await asyncio.sleep(2) # Artificial delay for shiz and giggles
    arr = np.array(args)
    return mean(arr)