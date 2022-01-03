import numpy as np

async def operation(*args):
    arr = np.array(args)
    return np.sum(arr)