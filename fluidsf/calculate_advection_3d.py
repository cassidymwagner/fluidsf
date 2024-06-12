import numpy as np


def calculate_advection_3d(  # noqa: D417
    u,
    v,
    w,
    x,
    y,
    z,
    scalar=None,
):
    """
    Calculate the advection for a velocity field or scalar field. The velocity field
    will return advection components in the x, y, and z directions.
    The scalar field will return the scalar advection. Defaults to advection for
    velocity field. If the velocity advection is skipped or a scalar field is not
    provided, the relevant dictionary key will return None.

    Parameters
    ----------
        u: ndarray
            The u-component of velocity.
        v: ndarray
            The v-component of velocity.
        w: ndarray
            The w-component of velocity.
        x: ndarray
            The x-coordinates of the grid.
        y: ndarray
            The y-coordinates of the grid.
        z: ndarray
            The z-coordinates of the grid.
        scalar: ndarray, optional
            Array of scalar values. Defaults to None.

    Returns
    -------
        tuple or ndarray:
            A tuple of advection components (x, y, z) if scalar is not provided,
            otherwise returns an ndarray of scalar advection.
    """
    dx = np.abs(x[0] - x[1])
    dy = np.abs(y[0] - y[1])
    dz = np.abs(z[0] - z[1])

    if scalar is not None:
        dsdz, dsdy, dsdx = np.gradient(scalar, dz, dy, dx, axis=(0, 1, 2))

        advection = u * dsdx + v * dsdy + w * dsdz

    else:
        dudz, dudy, dudx = np.gradient(u, dz, dy, dx, axis=(0, 1, 2))
        dvdz, dvdy, dvdx = np.gradient(v, dz, dy, dx, axis=(0, 1, 2))
        dwdz, dwdy, dwdx = np.gradient(w, dz, dy, dx, axis=(0, 1, 2))

        u_advection = u * dudx + v * dudy + w * dudz
        v_advection = u * dvdx + v * dvdy + w * dvdz
        w_advection = u * dwdx + v * dwdy + w * dwdz
        
        advection = (u_advection, v_advection, w_advection)

    return advection
