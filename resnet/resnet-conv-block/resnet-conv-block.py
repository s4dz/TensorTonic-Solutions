import numpy as np

def conv_block(x, W1, W2, Ws):
    """
    Returns: np.ndarray with sum of main path output and projected shortcut
    """
    x = np.array(x)
    W1 = np.array(W1)
    W2 = np.array(W2)
    Ws = np.array(Ws)
    h = np.maximum(0, np.dot(x, W1))
    z = np.dot(h, W2)
    shortcut = np.dot(x, Ws)
    return np.maximum(0, z + shortcut)
    pass
