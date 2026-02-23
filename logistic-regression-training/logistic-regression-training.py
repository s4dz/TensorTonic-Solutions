import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    m, n = X.shape
    w = np.zeros(n)
    b = 0
    for i in range(steps):
        pre = _sigmoid(np.dot(X, w) + b)
        error = pre - y
        gradientw = (1/m) * np.dot(X.T, error)
        gradientb = (1/m) * np.sum(error)
        w = w - lr * gradientw
        b = b - lr * gradientb
    return w, b
    pass