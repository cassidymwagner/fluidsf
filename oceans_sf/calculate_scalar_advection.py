import numpy as np


def calculate_scalar_advection(
    u, v, x, y, scalar, dx=None, dy=None, grid_type="uniform"
):
    """
    Calculate the scalar advection field using the given velocity components and
    scalar field.

    Args:
    ----
        u (ndarray): The u-component of velocity.
        v (ndarray): The v-component of velocity.
        x (ndarray): The x-coordinates of the grid.
        y (ndarray): The y-coordinates of the grid.
        scalar (ndarray): The scalar field.
        dx (float or ndarray, optional): The grid spacing in the x-direction.
        Defaults to None.
        dy (float or ndarray, optional): The grid spacing in the y-direction.
        Defaults to None.
        grid_type (str, optional): The type of grid. Defaults to "uniform".

    Returns:
    -------
        ndarray: The scalar advection field.
    """
    if grid_type == "latlon":
        xcoords = dx.cumsum()
        ycoords = dy.cumsum()

        dsdy, dsdx = np.gradient(scalar, xcoords, ycoords, axis=(0, 1))

    else:
        dx = np.abs(x[0] - x[1])
        dy = np.abs(y[0] - y[1])

        dsdy, dsdx = np.gradient(scalar, dx, dy, axis=(0, 1))

    advection = u * dsdx + v * dsdy

    return advection
