import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    Z1 = np.asarray(Z1)
    Z2 = np.asarray(Z2)
    logits= (Z1 @ Z2.T) / temperature
    shifted = logits - np.max(logits, axis=1, keepdims=True)
    log_denominator = np.log(np.sum(np.exp(shifted), axis=1))
    losses = -np.diag(shifted) + log_denominator
    return float(np.mean(losses))
    pass