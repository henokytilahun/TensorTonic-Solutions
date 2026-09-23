from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    nx = np.array(x)
    

    seen = {}

    for n in nx:
        if n in seen:
            seen[n] +=1
        else:
            seen[n] = 1

    max_count = 0
    mode = 0

    for n in seen:
        if seen[n] > max_count:
            max_count = seen[n]
            mode = n

    dic = {"mean": float(np.mean(nx)), "median": float(np.median(nx)), "mode": float(mode)}
        
    return dic