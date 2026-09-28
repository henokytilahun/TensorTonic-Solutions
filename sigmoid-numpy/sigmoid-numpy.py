import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    nx = np.array(x)
    arr = 1 / (1 + (math.e**(nx*-1)))    

    return arr