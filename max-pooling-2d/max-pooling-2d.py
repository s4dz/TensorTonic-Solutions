import numpy as np
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    X = np.array(X)
    H, W = X.shape
    Hout = H // pool_size
    Wout = W // pool_size
    out = np.full((Hout, Wout), -1e9)
    for i in range(Hout):
        for j in range(Wout):
            for a in range(pool_size):
                for b in range(pool_size):
                    out[i][j] = max(X[i * pool_size + a][j * pool_size + b], out[i][j])
    return out.tolist()