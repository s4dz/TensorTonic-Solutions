import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    l = np.where(margin - y_true * y_score > 0, margin - y_true * y_score, 0)
    if reduction == "mean": return float(np.mean(l))
    else: return float(np.sum(l))
    pass