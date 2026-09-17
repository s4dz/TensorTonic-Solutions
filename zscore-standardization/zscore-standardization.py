import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    X = np.asarray(X, dtype=float)

    mean_x = np.mean(X, axis=axis, keepdims=True)
    std = np.std(X, axis=axis, keepdims=True)

    s_value = np.divide(
        X - mean_x,
        std,
        out=np.zeros_like(X),
        where=std > eps
    )

    return s_value