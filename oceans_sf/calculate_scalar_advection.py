import numpy as np


def calculate_scalar_advection(
    scalar, par_u, par_v, x, y, dx=None, dy=None, grid_type="uniform"
):
    """Add docstring."""
    u = par_u
    v = par_v
    s = scalar

    if grid_type == "latlon":
        xcoords = dx.cumsum()
        ycoords = dy.cumsum()

        dsdx, dsdy = np.gradient(s, xcoords, ycoords, axis=(0, 1))

    else:
        dx = np.abs(x[0] - x[1])
        dy = np.abs(y[0] - y[1])

        dsdx, dsdy = np.gradient(s, dx, dy, axis=(0, 1))

    advection = u * dsdx + v * dsdy

    return advection
