import numpy as np
def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    X = np.array(X)
    H, W = X.shape
    Hn = H // pool_size
    Wn = W // pool_size
    view = X[:Hn * pool_size, :Wn * pool_size].reshape(Hn, pool_size, Wn, pool_size)
    return view.mean(axis=(1,3)).tolist()