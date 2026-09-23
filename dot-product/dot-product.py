import numpy as np


def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    if not x or not y:
        return null
    
    np_x = np.array(x)
    np_y = np.array(y)

    summ = np_x * np_y
    fsumm = float(sum(summ))
    return fsumm


    