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
        dsdz, dsdy, dsdx = np.gradient(scalar, dx, dy, dz, axis=(0, 1, 2))

        advection_i = v * dsdz - w * dsdy
        advection_j = w * dsdx - u * dsdz
        advection_k = u * dsdy - v * dsdx
        advection = advection_i + advection_j + advection_k

    else:
        dudz, dudy, dudx = np.gradient(u, dx, dy, dz, axis=(0, 1, 2))
        dvdz, dvdy, dvdx = np.gradient(v, dx, dy, dz, axis=(0, 1, 2))
        dwdz, dwdy, dwdx = np.gradient(w, dx, dy, dz, axis=(0, 1, 2))

        east_adv_i = v * dudz - w * dudy
        east_adv_j = w * dudx - u * dudz
        east_adv_k = u * dudy - v * dudx
        eastward_advection = east_adv_i + east_adv_j + east_adv_k

        north_adv_i = v * dvdz - w * dvdy
        north_adv_j = w * dvdx - u * dvdz
        north_adv_k = u * dvdy - v * dvdx
        northward_advection = north_adv_i + north_adv_j + north_adv_k

        down_adv_i = v * dwdz - w * dwdy
        down_adv_j = w * dwdx - u * dwdz
        down_adv_k = u * dwdy - v * dwdx
        downward_advection = down_adv_i + down_adv_j + down_adv_k
        advection = (eastward_advection, northward_advection, downward_advection)

    return advection
