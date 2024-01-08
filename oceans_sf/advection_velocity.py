import numpy as np

from .bin_data import bin_data
from .calculate_advection_velocity_structure_function import (
    calculate_advection_velocity_structure_function,
)
from .calculate_separation_distances import calculate_separation_distances
from .calculate_velocity_advection import calculate_velocity_advection
from .shift_array1d import shift_array1d
from .shift_array2d import shift_array2d


def advection_velocity(
    u,
    v,
    x,
    y,
    dx=None,
    dy=None,
    boundary="Periodic",
    even="True",
    grid_type="uniform",
    nbins=10,
):
    """
    Calculate the advection velocity structure function for 2D u and v velocity fields.

    Args:
    ----
        u (ndarray): 2D array of u velocity components.
        v (ndarray): 2D array of v velocity components.
        x (ndarray): 2D array of x-coordinates.
        y (ndarray): 1D array of y-coordinates.
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
        and separation distances for the x- and y-direction (zonal and meridional).

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
    xd = np.zeros(np.shape(sep_z))
    yd = np.zeros(np.shape(sep_m))

    # Initialize the structure function arrays
    SF_z = np.zeros(np.shape(sep_z))
    SF_m = np.zeros(np.shape(sep_m))
    print(sep_z, sep_m)
    adv_E, adv_N = calculate_velocity_advection(u, v, x, y, dx, dy, grid_type)
    # print(adv_E, adv_N)
    # Iterate over separations left and down
    for down, left in zip(sep_m, sep_z):
        xroll = shift_array1d(x, shift_by=left, boundary=boundary)
        yroll = shift_array1d(y, shift_by=down, boundary=boundary)
        print(xroll, yroll)
        adv_E_roll_left, adv_E_roll_down = shift_array2d(
            adv_E, shift_down=down, shift_left=left, boundary=boundary
        )
        adv_N_roll_left, adv_N_roll_down = shift_array2d(
            adv_N, shift_down=down, shift_left=left, boundary=boundary
        )
        u_roll_left, u_roll_down = shift_array2d(
            u, shift_down=down, shift_left=left, boundary=boundary
        )
        v_roll_left, v_roll_down = shift_array2d(
            v, shift_down=down, shift_left=left, boundary=boundary
        )

        SF_m[down] = calculate_advection_velocity_structure_function(
            u,
            v,
            adv_E,
            adv_N,
            u_roll_down,
            v_roll_down,
            adv_E_roll_down,
            adv_N_roll_down,
        )

        SF_m[left] = calculate_advection_velocity_structure_function(
            u,
            v,
            adv_E,
            adv_N,
            u_roll_left,
            v_roll_left,
            adv_E_roll_left,
            adv_N_roll_left,
        )

        # Calculate separation distances in x and y
        xd[left], tmp = calculate_separation_distances(
            x[left], y[left], xroll[left], yroll[left], grid_type
        )
        tmp, y[down] = calculate_separation_distances(
            x[down], y[down], xroll[down], yroll[down], grid_type
        )

    # Bin the data if the grid is uneven
    if even is False:
        xd, SF_z = bin_data(xd, SF_z)
        yd, SF_m = bin_data(yd, SF_m)

    print(xd, yd, SF_z, SF_m)

    data = {
        "SF_zonal": SF_z,
        "SF_meridional": SF_m,
        "x-diffs": xd,
        "y-diffs": yd,
    }

    return data
