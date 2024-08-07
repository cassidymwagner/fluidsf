from geopy.distance import great_circle


def calculate_separation_distances(
    x, y, x_shift, y_shift, grid_type="uniform", radius=None
):
    """
    Calculate the separation distances between two points.

    Parameters
    ----------
    x: float
        The x-coordinate of the first point.
    y: float
        The y-coordinate of the first point.
    x_shift: float
        The x-coordinate of the second point.
    y_shift: float
        The y-coordinate of the second point.
    grid_type: str
        The type of grid used for the coordinates. A uniform grid results in a simple
        distance calculation, but a latlon grid uses geopy's great_circle
        function to estimate the distance in meters. Defaults to "uniform".
    radius: float, optional
        The radius of the sphere for latlon grids. Defaults to None, which will use
        the default value of the Earth's radius. Must be in units of kilometers if
        provided.

    Returns
    -------
    tuple:
        A tuple containing the x and y separation distances. Either in meters in the
        case of a latlon grid or code units for a uniform grid
    """
    if grid_type == "latlon":
        if radius is not None:
            xd = great_circle((y, x_shift), (y, x), radius=radius).meters
            yd = great_circle((y_shift, x), (y, x), radius=radius).meters
        else:
            xd = great_circle((y, x_shift), (y, x)).meters
            yd = great_circle((y_shift, x), (y, x)).meters
    else:
        xd = x_shift - x
        yd = None
        if y is not None and y_shift is not None:
            yd = y_shift - y

    return (xd, yd)
