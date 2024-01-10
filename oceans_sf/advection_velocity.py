import numpy as np

from .bin_data import bin_data
from .calculate_scalar_advection import calculate_scalar_advection
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function_advection import (
    calculate_structure_function_advection,
)
from .calculate_velocity_advection import calculate_velocity_advection
from .shift_array1d import shift_array1d


def advection_velocity(
    u,
    v,
    x,
    y,
    skip_velocity_sf=False,
    scalar=None,
    dx=None,
    dy=None,
    boundary="Periodic",
    even="True",
    grid_type="uniform",
    nbins=10,
):
    """
    Full method for calculating advective structure functions for 2D data.
    Supports velocity-based and scalar-based structure functions.
    Defaults to calculating the velocity-based structure functions for the x (zonal)
    and y (meridional) directions.

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
        dict: Dictionary containing the advection velocity structure functions
        and separation distances for the x- and y-direction (zonal and meridional,
        respectively).

    """
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
        adv_E, adv_N = calculate_velocity_advection(u, v, x, y, dx, dy, grid_type)

    if scalar is not None:
        SF_z_scalar = np.zeros(len(sep_z) + 1)
        SF_m_scalar = np.zeros(len(sep_m) + 1)
        adv_scalar = calculate_scalar_advection(u, v, x, y, scalar, dx, dy, grid_type)
    # Iterate over separations left and down
    for down, left in zip(sep_m, sep_z, strict=False):
        xroll = shift_array1d(x, shift_by=left, boundary=boundary)
        yroll = shift_array1d(y, shift_by=down, boundary=boundary)

        SF_dicts = calculate_structure_function_advection(
            u,
            v,
            adv_E,
            adv_N,
            down,
            left,
            skip_velocity_sf,
            scalar,
            adv_scalar,
            boundary,
        )

        SF_z[left] = SF_dicts["SF_velocity_left"]
        SF_m[down] = SF_dicts["SF_velocity_down"]
        SF_z_scalar[left] = SF_dicts["SF_scalar_left"]
        SF_m_scalar[down] = SF_dicts["SF_scalar_down"]

        # Calculate separation distances in x and y
        xd[left], tmp = calculate_separation_distances(
            x[left], y[left], xroll[left], yroll[left], grid_type
        )
        tmp, yd[down] = calculate_separation_distances(
            x[down], y[down], xroll[down], yroll[down], grid_type
        )

    # Bin the data if the grid is uneven
    if even is False:
        xd, SF_z = bin_data(xd, SF_z, nbins)
        yd, SF_m = bin_data(yd, SF_m, nbins)

    data = {
        "SF_zonal": SF_z,
        "SF_meridional": SF_m,
        "x-diffs": xd,
        "y-diffs": yd,
    }

    return data
