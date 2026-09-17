import numpy as np

def adagrad_step(w: list, g: list, G: list, lr: float = 0.01, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w and new_G.
    """
    w = np.asarray(w)
    g = np.asarray(g)
    G = np.asarray(G)
    G_t = G + g ** 2
    w_t = w - lr *(g/np.sqrt(G_t + eps))
    ans = {"new_w" : w_t,
            "new_G": G_t}
    return ans
    pass