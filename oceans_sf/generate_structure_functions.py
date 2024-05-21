import numpy as np

from .bin_data import bin_data
from .calculate_advection import calculate_advection
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function import (
    calculate_structure_function,
)
from .shift_array1d import shift_array1d


def generate_structure_functions(  # noqa: C901, D417
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
    for the x and y directions.

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
            distances for the x- and y-direction.

    """
    # Initialize variables as NoneType
    SF_adv_x = None
    SF_adv_y = None
    SF_x_scalar = None
    SF_y_scalar = None
    adv_x = None
    adv_y = None
    adv_scalar = None
    SF_x_LL = None
    SF_y_LL = None
    SF_x_LLL = None
    SF_y_LLL = None
    SF_x_LTT = None
    SF_y_LTT = None
    SF_x_LSS = None
    SF_y_LSS = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    if boundary == "periodic-all":
        sep_x = range(1, int(len(x) / 2))
        sep_y = range(1, int(len(y) / 2))
    elif boundary == "periodic-x":
        sep_x = range(1, int(len(x) / 2))
        sep_y = range(1, int(len(y) - 1))
    elif boundary == "periodic-y":
        sep_x = range(1, int(len(x) - 1))
        sep_y = range(1, int(len(y) / 2))
    elif boundary is None:
        sep_x = range(1, int(len(x) - 1))
        sep_y = range(1, int(len(y) - 1))

    # Initialize the separation distance arrays
    xd = np.zeros(len(sep_x) + 1)
    yd = np.zeros(len(sep_y) + 1)

    # Initialize the structure function arrays
    if skip_velocity_sf is False:
        SF_adv_x = np.zeros(len(sep_x) + 1)
        SF_adv_y = np.zeros(len(sep_y) + 1)
        adv_x, adv_y = calculate_advection(u, v, x, y, dx, dy, grid_type)
        if traditional_type is not None:
            if any("LL" in t for t in traditional_type):
                SF_x_LL = np.zeros(len(sep_x) + 1)
                SF_y_LL = np.zeros(len(sep_y) + 1)
            if any("LLL" in t for t in traditional_type):
                SF_x_LLL = np.zeros(len(sep_x) + 1)
                SF_y_LLL = np.zeros(len(sep_y) + 1)
            if any("LTT" in t for t in traditional_type):
                SF_x_LTT = np.zeros(len(sep_x) + 1)
                SF_y_LTT = np.zeros(len(sep_y) + 1)

    if scalar is not None:
        SF_x_scalar = np.zeros(len(sep_x) + 1)
        SF_y_scalar = np.zeros(len(sep_y) + 1)
        adv_scalar = calculate_advection(u, v, x, y, dx, dy, grid_type, scalar)
        if traditional_type is not None:
            if any("LSS" in t for t in traditional_type):
                SF_x_LSS = np.zeros(len(sep_x) + 1)
                SF_y_LSS = np.zeros(len(sep_y) + 1)

    # Iterate over separations in x and y
    for x_shift in sep_x:
        y_shift = 1
        if boundary == "periodic-all" or boundary == "periodic-x":
            xroll = shift_array1d(x, shift_by=x_shift, boundary="Periodic")
        else:
            xroll = shift_array1d(x, shift_by=x_shift, boundary=None)

        SF_dicts = calculate_structure_function(
            u,
            v,
            adv_x,
            adv_y,
            x_shift,
            y_shift,
            skip_velocity_sf,
            scalar,
            adv_scalar,
            traditional_type,
            boundary,
        )

        if skip_velocity_sf is False:
            SF_adv_x[x_shift] = SF_dicts["SF_velocity_x"]
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    SF_x_LL[x_shift] = SF_dicts["SF_LL_x"]
                if any("LLL" in t for t in traditional_type):
                    SF_x_LLL[x_shift] = SF_dicts["SF_LLL_x"]
                if any("LTT" in t for t in traditional_type):
                    SF_x_LTT[x_shift] = SF_dicts["SF_LTT_x"]
        if scalar is not None:
            SF_x_scalar[x_shift] = SF_dicts["SF_scalar_x"]
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    SF_x_LSS[x_shift] = SF_dicts["SF_LSS_x"]

        # Calculate separation distances in x
        xd[x_shift], tmp = calculate_separation_distances(
            x[x_shift], y[y_shift], xroll[x_shift], y[y_shift], grid_type
        )

    for y_shift in sep_y:
        x_shift = 1
        if boundary == "periodic-all" or boundary == "periodic-y":
            yroll = shift_array1d(y, shift_by=y_shift, boundary="Periodic")
        else:
            yroll = shift_array1d(y, shift_by=y_shift, boundary=None)

        SF_dicts = calculate_structure_function(
            u,
            v,
            adv_x,
            adv_y,
            x_shift,
            y_shift,
            skip_velocity_sf,
            scalar,
            adv_scalar,
            traditional_type,
            boundary,
        )

        if skip_velocity_sf is False:
            SF_adv_y[y_shift] = SF_dicts["SF_velocity_y"]
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    SF_y_LL[y_shift] = SF_dicts["SF_LL_y"]
                if any("LLL" in t for t in traditional_type):
                    SF_y_LLL[y_shift] = SF_dicts["SF_LLL_y"]
                if any("LTT" in t for t in traditional_type):
                    SF_y_LTT[y_shift] = SF_dicts["SF_LTT_y"]
        if scalar is not None:
            SF_y_scalar[y_shift] = SF_dicts["SF_scalar_y"]
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    SF_y_LSS[y_shift] = SF_dicts["SF_LSS_y"]

        # Calculate separation distances in y
        tmp, yd[y_shift] = calculate_separation_distances(
            x[x_shift], y[y_shift], x[x_shift], yroll[y_shift], grid_type
        )



    # Bin the data if the grid is uneven
    if even is False:
        if skip_velocity_sf is False:
            xd_bin, SF_adv_x = bin_data(xd, SF_adv_x, nbins)
            yd_bin, SF_adv_y = bin_data(yd, SF_adv_y, nbins)
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    xd_bin, SF_x_LL = bin_data(xd, SF_x_LL, nbins)
                    yd_bin, SF_y_LL = bin_data(yd, SF_y_LL, nbins)
                if any("LLL" in t for t in traditional_type):
                    xd_bin, SF_x_LLL = bin_data(xd, SF_x_LLL, nbins)
                    yd_bin, SF_y_LLL = bin_data(yd, SF_y_LLL, nbins)
                if any("LTT" in t for t in traditional_type):
                    xd_bin, SF_x_LTT = bin_data(xd, SF_x_LTT, nbins)
                    yd_bin, SF_y_LTT = bin_data(yd, SF_y_LTT, nbins)
        if scalar is not None:
            xd_bin, SF_x_scalar = bin_data(xd, SF_x_scalar, nbins)
            yd_bin, SF_y_scalar = bin_data(yd, SF_y_scalar, nbins)
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    xd_bin, SF_x_LSS = bin_data(xd, SF_x_LSS, nbins)
                    yd_bin, SF_y_LSS = bin_data(yd, SF_y_LSS, nbins)
        xd = xd_bin
        yd = yd_bin

    data = {
        "SF_advection_velocity_x": SF_adv_x,
        "SF_advection_velocity_y": SF_adv_y,
        "SF_advection_scalar_x": SF_x_scalar,
        "SF_advection_scalar_y": SF_y_scalar,
        "SF_LL_x": SF_x_LL,
        "SF_LL_y": SF_y_LL,
        "SF_LLL_x": SF_x_LLL,
        "SF_LLL_y": SF_y_LLL,
        "SF_LTT_x": SF_x_LTT,
        "SF_LTT_y": SF_y_LTT,
        "SF_LSS_x": SF_x_LSS,
        "SF_LSS_y": SF_y_LSS,
        "x-diffs": xd,
        "y-diffs": yd,
    }
    return data
