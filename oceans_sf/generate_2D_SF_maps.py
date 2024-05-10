import numpy as np
import itertools

from .bin_data import bin_data
from .calculate_advection import calculate_advection
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function import (
    calculate_structure_function,
)
from .shift_array1d import shift_array1d

from .calculate_2D_SF_maps import calculate_2D_SF_maps


def generate_2D_SF_maps(  # noqa: C901, D417
    u,
    v,
    x,
    y,
    skip_velocity_sf=False,
    scalar=None,
    traditional_type=None,
    dx=None,
    dy=None,
    boundary="periodic-all",
    even="True",
    grid_type="uniform",
    nbins=10,
):
    """
    TEST
    Full method for generating structure functions for 2D data, either advective or
    traditional structure functions. Supports velocity-based and scalar-based structure
    functions. Defaults to calculating the velocity-based advective structure functions
    for the x (zonal) and y (meridional) directions.

    Parameters
    ----------
        u: ndarray
            2D array of u velocity components.
        v: ndarray
            2D array of v velocity components.
        x: ndarray
            1D array of x-coordinates.
        y: ndarray
            1D array of y-coordinates.
        skip_velocity_sf: bool, optional
            Flag used to skip calculating the velocity-based structure function if
            the user only wants to calculate the scalar-based structure function.
            Defaults to False.
        scalar: ndarray, optional
            2D array of scalar values. Defaults to None.
        traditional_type: list, optional
            List of traditional structure function types to calculate.
            Accepted types are: "LL", "LLL", "LTT", "LSS". If None,
            no traditional structure functions are calculated. Defaults to None.
        dx: float, optional
            Grid spacing in the x-direction. Defaults to None.
        dy: float, optional
            Grid spacing in the y-direction. Defaults to None.
        boundary: str, optional
            Boundary condition of the data. Accepted strings are "periodic-x",
            "periodic-y", and "periodic-all". Defaults to "periodic-all".
        even: bool, optional
            Flag indicating if the grid is evenly spaced. Defaults to True.
        grid_type:str, optional
            Type of grid, either "uniform" or "latlon". Defaults to "uniform".
        nbins: int, optional
            Number of bins for binning the data. Defaults to 10.

    Returns
    -------
        dict:
            Dictionary containing the requested structure functions and separation
            distances for the x- and y-direction (zonal and meridional, respectively).

    """
    # Initialize variables as NoneType
    SF_adv = None
    adv_x = None
    adv_y = None
    separation_vector = None


    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    x_shifts = range(0, int(len(x) / 2))
    y_shifts = range(-int(len(y) / 2, int(len(y) / 2))

    # Initialize the structure function arrays
    SF_adv = np.zeros([len(x_shifts), len(y_shifts)])
    adv_x, adv_y = calculate_advection(u, v, x, y, dx, dy, grid_type)

    separation_vectors = np.zeros([len(x_shifts), len(y_shifts)])
    separation_angles = np.zeros([len(x_shifts), len(y_shifts)])

    x_separations = np.zeros([len(x_shifts), len(y_shifts)])
    y_separations = np.zeros([len(x_shifts), len(y_shifts)])

    # Iterate over separations right and down
    for x_shift, y_shift in itertools.product(x_shifts, y_shifts):
        
        x_separation = x_shift * (x[1] - x[0])
        y_separation = y_shift * (y[1] - y[0])
        

        SF_dicts = calculate_2D_SF_maps(
            u,
            v,
            adv_x,
            adv_y,
            x_shift,
            y_shift,
        )

        SF_adv[x_shift, y_shift] = SF_dicts["SF_velocity_advection_xy"]
        separation_vectors[x_shift, y_shift] = np.sqrt(x_separation**2 + y_separation**2)
        separation_angles[x_shift, y_shift] = np.arctan(y_separation/x_separation)
        x_separations[x_shift, y_shift] = x_separation
        y_separations[x_shift, y_shift] =y_separation

    data = {
        "SF_velocity_advection_xy": SF_adv,
        "separation_vectors": separation_vectors,
        "separation_angles": separation_angles,
        "x_separations": x_separations,
        "y_separations": y_separations,
    }
    return data
