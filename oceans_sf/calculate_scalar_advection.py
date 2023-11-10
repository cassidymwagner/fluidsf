import numpy as np


def calculate_scalar_advection(scalar, par_u, par_v, x, y):
    """
    Add docstring
    """
    u = par_u
    v = par_v
    s = scalar

    dx = 2 * np.abs(x[0] - x[1])
    dy = 2 * np.abs(y[0] - y[1])

    dsdx, dsdy = np.gradient(s, dx, dy, axis=(1,0))
    advection = u * dsdx + v * dsdy

    return (advection)
