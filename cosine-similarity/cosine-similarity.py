import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    if not a or not b:
        return null

    ea = np.linalg.norm(a)
    eb = np.linalg.norm(b)

    dot = np.dot(a,b)
    dot = float(dot)
    if dot == 0.0:
        return 0.0

    cos = dot / (ea * eb)
    cos = float(cos)

    return cos
    