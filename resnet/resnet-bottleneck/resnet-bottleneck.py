import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns: np.ndarray with bottleneck residual block output (compress, process, expand + skip)
    """
    x = np.array(x)
    W1 = np.array(W1)
    W2 = np.array(W2)
    W3 = np.array(W3)
    Ws = np.array(Ws)
    shortcut = np.dot(x, Ws)
    l1 = np.maximum(0, np.dot(x, W1))
    l2 = np.maximum(0, np.dot(l1, W2))
    l3 = np.dot(l2, W3)
    return np.maximum(0, l3 + shortcut)
    pass
