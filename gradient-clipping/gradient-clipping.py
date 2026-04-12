import numpy as np

def clip_gradients(g, max_norm):
    if max_norm <= 0: return np.asarray(g)
    g = np.array(g)
    l2_norm = np.linalg.norm(g)
    if l2_norm <= max_norm: return g
    else: return np.multiply(g, max_norm/l2_norm)
    pass