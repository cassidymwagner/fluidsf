import numpy as np


def calculate_advection(  # noqa: D417
    u,
    v,
    x=None,
    y=None,
    lats=None,
    lons=None,
    dx=None,
    dy=None,
    grid_type="uniform",
    scalar=None,
):
    """
    Calculate the advection for a velocity field or scalar field. The velocity field
    will return advection components in the x and y directions.
    The scalar field will return the scalar advection. Defaults to advection for
    velocity field.

    Parameters
    ----------
        u: ndarray
            The u-component of velocity.
        v: ndarray
            The v-component of velocity.
        x: ndarray, optional
            The x-coordinates of the grid. Defaults to None, but required if grid_type
            is not "latlon".
        y: ndarray
            The y-coordinates of the grid. Defaults to None, but required if grid_type
            is not "latlon".
        lats: ndarray, optional
            The 2D latitude coordinates of the grid. Defaults to None, but required if
            grid_type is "latlon".
        lons: ndarray, optional
            The 2D longitude coordinates of the grid. Defaults to None, but required if
            grid_type is "latlon".
        dx: float or ndarray, optional
            The grid spacing in the x-direction. Defaults to None.
        dy: float or ndarray, optional
            The grid spacing in the y-direction. Defaults to None.
        grid_type: str, optional
            The type of grid. Defaults to "uniform".
        scalar: ndarray, optional
            Array of scalar values. Defaults to None.

    Returns
    -------
        tuple or ndarray:
            A tuple of advection components (x and y) if scalar is not provided,
            otherwise returns an ndarray of scalar advection.
    """
    if grid_type == "uniform":
        dx = np.abs(x[0] - x[1])
        dy = np.abs(y[0] - y[1])

        if scalar is not None:
            dsdx, dsdy = np.gradient(scalar, dx, dy, axis=(1, 0))
        else:
            dudx, dudy = np.gradient(u, dx, dy, axis=(1, 0))
            dvdx, dvdy = np.gradient(v, dx, dy, axis=(1, 0))

    elif grid_type == "latlon":
        lat_meters = lats[:, 0] * 111000
        lon_meters = lons[0, :] * 111000 * np.cos(np.deg2rad(lats[0, :]))

        if scalar is not None:
            dsdx, dsdy = np.gradient(scalar, lon_meters, lat_meters, axis=(1, 0))
        else:
            dudx, dudy = np.gradient(u, lon_meters, lat_meters, axis=(1, 0))
            dvdx, dvdy = np.gradient(v, lon_meters, lat_meters, axis=(1, 0))

    else:
        xcoords = dx.cumsum()
        ycoords = dy.cumsum()

        if scalar is not None:
            dsdx, dsdy = np.gradient(scalar, xcoords, ycoords, axis=(1, 0))
        else:
            dudx, dudy = np.gradient(u, xcoords, ycoords, axis=(1, 0))
            dvdx, dvdy = np.gradient(v, xcoords, ycoords, axis=(1, 0))

    if scalar is not None:
        advection = u * dsdx + v * dsdy
    else:
        x_advection = u * dudx + v * dudy
        y_advection = u * dvdx + v * dvdy
        advection = (x_advection, y_advection)

    return advection
