import numpy as np

from .bin_data import bin_data
from .calculate_advection import calculate_advection
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function import (
    calculate_structure_function,
)
from .shift_array1d import shift_array1d


def generate_structure_functions(  # noqa: C901
    u,
    v,
    x,
    y,
    skip_velocity_sf=False,
    scalar=None,
    traditional_order=0,
    dx=None,
    dy=None,
    boundary="Periodic",
    even="True",
    grid_type="uniform",
    nbins=10,
):
    """
    Full method for generating structure functions for 2D data, either advective or
    traditional structure functions. Supports velocity-based and scalar-based structure
    functions. Defaults to calculating the velocity-based advective structure functions
    for the x (zonal) and y (meridional) directions.

    Args:
    ----
        u (ndarray): 2D array of u velocity components.
        v (ndarray): 2D array of v velocity components.
        x (ndarray): 1D array of x-coordinates.
        y (ndarray): 1D array of y-coordinates.
        skip_velocity_sf (bool, optional): Flag used to skip calculating the
        velocity-based structure function if the user only wants to calculate the
        scalar-based structure function. Defaults to False.
        scalar (ndarray, optional): 2D array of scalar values. Defaults to None.
        traditional_order (int, optional): Order for calculating traditional
        non-advective structure functions. If 0, no traditional structure functions
        are calculated. Defaults to 0.
        dx (float, optional): Grid spacing in the x-direction. Defaults to None.
        dy (float, optional): Grid spacing in the y-direction. Defaults to None.
        boundary (str, optional): Boundary condition of the data.
        Defaults to "Periodic".
        even (bool, optional): Flag indicating if the grid is evenly spaced.
        Defaults to True.
        grid_type (str, optional): Type of grid, either "uniform" or "latlon".
        Defaults to "uniform".
        nbins (int, optional): Number of bins for binning the data. Defaults to 10.

    Returns:
    -------
        dict: Dictionary containing the requested structure functions and separation
        distances for the x- and y-direction (zonal and meridional, respectively).

    """
    # Initialize variables as NoneType
    SF_z = None
    SF_m = None
    SF_z_scalar = None
    SF_m_scalar = None
    SF_z_trad_velocity = None
    SF_m_trad_velocity = None
    SF_z_trad_scalar = None
    SF_m_trad_scalar = None
    adv_E = None
    adv_N = None
    adv_scalar = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    if boundary == "Periodic":
        sep_z = range(1, int(len(x) / 2))
        sep_m = range(1, int(len(y) / 2))
    else:
        sep_z = range(1, int(len(x) - 1))
        sep_m = range(1, int(len(y) - 1))

    # Initialize the separation distance arrays
    xd = np.zeros(len(sep_z) + 1)
    yd = np.zeros(len(sep_m) + 1)

    # Initialize the structure function arrays
    if skip_velocity_sf is False:
        SF_z = np.zeros(len(sep_z) + 1)
        SF_m = np.zeros(len(sep_m) + 1)
        adv_E, adv_N = calculate_advection(u, v, x, y, dx, dy, grid_type)
        if traditional_order > 0:
            SF_z_trad_velocity = np.zeros(len(sep_z) + 1)
            SF_m_trad_velocity = np.zeros(len(sep_m) + 1)

    if scalar is not None:
        SF_z_scalar = np.zeros(len(sep_z) + 1)
        SF_m_scalar = np.zeros(len(sep_m) + 1)
        adv_scalar = calculate_advection(u, v, x, y, dx, dy, grid_type, scalar)
        if traditional_order > 0:
            SF_z_trad_scalar = np.zeros(len(sep_z) + 1)
            SF_m_trad_scalar = np.zeros(len(sep_m) + 1)

    # Iterate over separations right and down
    for down, right in zip(sep_m, sep_z, strict=False):
        xroll = shift_array1d(x, shift_by=right, boundary=boundary)
        yroll = shift_array1d(y, shift_by=down, boundary=boundary)

        SF_dicts = calculate_structure_function(
            u,
            v,
            adv_E,
            adv_N,
            down,
            right,
            skip_velocity_sf,
            scalar,
            adv_scalar,
            traditional_order,
            boundary,
        )

        # Maybe don't do this and just let the dict have Nones in it,
        # probably a lot easier and less silly
        if skip_velocity_sf is False:
            SF_z[right] = SF_dicts["SF_velocity_right"]
            SF_m[down] = SF_dicts["SF_velocity_down"]
            if traditional_order > 0:
                SF_z_trad_velocity[right] = SF_dicts["SF_trad_velocity_right"]
                SF_m_trad_velocity[down] = SF_dicts["SF_trad_velocity_down"]
        if scalar is not None:
            SF_z_scalar[right] = SF_dicts["SF_scalar_right"]
            SF_m_scalar[down] = SF_dicts["SF_scalar_down"]
            if traditional_order > 0:
                SF_z_trad_scalar[right] = SF_dicts["SF_trad_scalar_right"]
                SF_m_trad_scalar[down] = SF_dicts["SF_trad_scalar_down"]

        # Calculate separation distances in x and y
        xd[right], tmp = calculate_separation_distances(
            x[right], y[right], xroll[right], yroll[right], grid_type
        )
        tmp, yd[down] = calculate_separation_distances(
            x[down], y[down], xroll[down], yroll[down], grid_type
        )

    # Bin the data if the grid is uneven
    if even is False:
        if skip_velocity_sf is False:
            xd_bin, SF_z = bin_data(xd, SF_z, nbins)
            yd_bin, SF_m = bin_data(yd, SF_m, nbins)
            if traditional_order > 0:
                xd_bin, SF_z_trad_velocity = bin_data(xd, SF_z_trad_velocity, nbins)
                yd_bin, SF_m_trad_velocity = bin_data(yd, SF_m_trad_velocity, nbins)
        if scalar is not None:
            xd_bin, SF_z_scalar = bin_data(xd, SF_z_scalar, nbins)
            yd_bin, SF_m_scalar = bin_data(yd, SF_m_scalar, nbins)
            if traditional_order > 0:
                xd_bin, SF_z_trad_scalar = bin_data(xd, SF_z_trad_scalar, nbins)
                yd_bin, SF_m_trad_scalar = bin_data(yd, SF_m_trad_scalar, nbins)
        xd = xd_bin
        yd = yd_bin

    data = {
        "SF_advection_velocity_zonal": SF_z,
        "SF_advection_velocity_meridional": SF_m,
        "SF_advection_scalar_zonal": SF_z_scalar,
        "SF_advection_scalar_meridional": SF_m_scalar,
        "SF_traditional_velocity_zonal": SF_z_trad_velocity,
        "SF_traditional_velocity_meridional": SF_m_trad_velocity,
        "SF_traditional_scalar_zonal": SF_z_trad_scalar,
        "SF_traditional_scalar_meridional": SF_m_trad_scalar,
        "x-diffs": xd,
        "y-diffs": yd,
    }
    return data
