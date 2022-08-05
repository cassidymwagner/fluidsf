import numpy as np


def calculate_scalar_advection(scalar, par_u, par_v, x, y):
    """
    Add docstring
    """
    u = par_u
    v = par_v
    s = scalar

    dx = np.abs(x[0] - x[1])
    dy = np.abs(y[0] - y[1])

    s_ip1 = np.roll(s, -1, axis=1)
    s_im1 = np.roll(s, 1, axis=1)
    s_jp1 = np.roll(s, -1, axis=0)
    s_jm1 = np.roll(s, 1, axis=0)

    dsdx = (s_ip1 - s_im1) / (2 * dx)
    dsdy = (s_jp1 - s_jm1) / (2 * dy)

    advection = u * dsdx + v * dsdy

    return (advection)
