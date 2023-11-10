import numpy as np


def calculate_velocity_advection(par_u, par_v, x, y):
    """
    Add docstring
    """
    u = par_u
    v = par_v

    dx = 2 * np.abs(x[0] - x[1])
    dy = 2 * np.abs(y[0] - y[1])

    dudx, dudy = np.gradient(u, dx, dy, axis=(1, 0))
    dvdx, dvdy = np.gradient(v, dx, dy, axis=(1, 0))

    eastward_advection = u * dudx + v * dudy
    northward_advection = u * dvdx + v * dvdy

    return (eastward_advection, northward_advection)
