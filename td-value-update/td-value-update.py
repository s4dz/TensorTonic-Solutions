import numpy as np

def td_value_update(V: list, s: int, r: float, s_next: int, alpha: float, gamma: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as V.
    """
    V = np.asarray(V, dtype = float)
    V_ans = np.copy(V)
    delta = r + gamma * V_ans[s_next] - V_ans[s]
    V_ans[s] += alpha * delta
    return V_ans