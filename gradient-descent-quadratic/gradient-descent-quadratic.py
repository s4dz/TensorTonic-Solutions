def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    for index in range(steps):
        gradient = 2 * a * x0 + b
        x0 -= gradient * lr
    return x0
    pass