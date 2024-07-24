def calculate_separation_distances_3d(x, y, z, x_shift, y_shift, z_shift):
    """
    Calculate the separation distances between two points.

    Parameters
    ----------
    x: float
        The x-coordinate of the first point.
    y: float
        The y-coordinate of the first point.
    z: float
        The z-coordinate of the first point.
    x_shift: float
        The x-coordinate of the second point.
    y_shift: float
        The y-coordinate of the second point.
    z_shift: float
        The z-coordinate of the second point.

    Returns
    -------
    tuple:
        A tuple containing the x, y, and z separation distances. In code units for a
        uniform grid.
    """
    xd = x_shift - x
    yd = y_shift - y
    zd = z_shift - z

    return (xd, yd, zd)
