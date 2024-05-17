import numpy as np

from .bin_data import bin_data
from .calculate_advection import calculate_advection
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function import (
    calculate_structure_function,
)
from .shift_array_1d import shift_array_1d


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
    SF_z = None
    SF_m = None
    SF_z_scalar = None
    SF_m_scalar = None
    adv_E = None
    adv_N = None
    adv_scalar = None
    SF_z_LL = None
    SF_m_LL = None
    SF_z_LLL = None
    SF_m_LLL = None
    SF_z_LTT = None
    SF_m_LTT = None
    SF_z_LSS = None
    SF_m_LSS = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    if boundary == "periodic-all":
        sep_z = range(1, int(len(x) / 2))
        sep_m = range(1, int(len(y) / 2))
    elif boundary == "periodic-x":
        sep_z = range(1, int(len(x) / 2))
        sep_m = range(1, int(len(y) - 1))
    elif boundary == "periodic-y":
        sep_z = range(1, int(len(x) - 1))
        sep_m = range(1, int(len(y) / 2))
    elif boundary is None:
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
        if traditional_type is not None:
            if any("LL" in t for t in traditional_type):
                SF_z_LL = np.zeros(len(sep_z) + 1)
                SF_m_LL = np.zeros(len(sep_m) + 1)
            if any("LLL" in t for t in traditional_type):
                SF_z_LLL = np.zeros(len(sep_z) + 1)
                SF_m_LLL = np.zeros(len(sep_m) + 1)
            if any("LTT" in t for t in traditional_type):
                SF_z_LTT = np.zeros(len(sep_z) + 1)
                SF_m_LTT = np.zeros(len(sep_m) + 1)

    if scalar is not None:
        SF_z_scalar = np.zeros(len(sep_z) + 1)
        SF_m_scalar = np.zeros(len(sep_m) + 1)
        adv_scalar = calculate_advection(u, v, x, y, dx, dy, grid_type, scalar)
        if traditional_type is not None:
            if any("LSS" in t for t in traditional_type):
                SF_z_LSS = np.zeros(len(sep_z) + 1)
                SF_m_LSS = np.zeros(len(sep_m) + 1)

    # Iterate over separations right and down
    for down in sep_m:
        right = 1
        if boundary == "periodic-all" or boundary == "periodic-y":
            yroll = shift_array_1d(y, shift_by=down, boundary="Periodic")
        else:
            yroll = shift_array_1d(y, shift_by=down, boundary=None)

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
            traditional_type,
            boundary,
        )

        if skip_velocity_sf is False:
            SF_m[down] = SF_dicts["SF_velocity_down"]
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    SF_m_LL[down] = SF_dicts["SF_LL_down"]
                if any("LLL" in t for t in traditional_type):
                    SF_m_LLL[down] = SF_dicts["SF_LLL_down"]
                if any("LTT" in t for t in traditional_type):
                    SF_m_LTT[down] = SF_dicts["SF_LTT_down"]
        if scalar is not None:
            SF_m_scalar[down] = SF_dicts["SF_scalar_down"]
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    SF_m_LSS[down] = SF_dicts["SF_LSS_down"]

        # Calculate separation distances in y
        tmp, yd[down] = calculate_separation_distances(
            x[right], y[down], x[right], yroll[down], grid_type
        )

    for right in sep_z:
        down = 1
        if boundary == "periodic-all" or boundary == "periodic-x":
            xroll = shift_array_1d(x, shift_by=right, boundary="Periodic")
        else:
            xroll = shift_array_1d(x, shift_by=right, boundary=None)

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
            traditional_type,
            boundary,
        )

        if skip_velocity_sf is False:
            SF_z[right] = SF_dicts["SF_velocity_right"]
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    SF_z_LL[right] = SF_dicts["SF_LL_right"]
                if any("LLL" in t for t in traditional_type):
                    SF_z_LLL[right] = SF_dicts["SF_LLL_right"]
                if any("LTT" in t for t in traditional_type):
                    SF_z_LTT[right] = SF_dicts["SF_LTT_right"]
        if scalar is not None:
            SF_z_scalar[right] = SF_dicts["SF_scalar_right"]
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    SF_z_LSS[right] = SF_dicts["SF_LSS_right"]

        # Calculate separation distances in x
        xd[right], tmp = calculate_separation_distances(
            x[right], y[down], xroll[right], y[down], grid_type
        )

    # Bin the data if the grid is uneven
    if even is False:
        if skip_velocity_sf is False:
            xd_bin, SF_z = bin_data(xd, SF_z, nbins)
            yd_bin, SF_m = bin_data(yd, SF_m, nbins)
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    xd_bin, SF_z_LL = bin_data(xd, SF_z_LL, nbins)
                    yd_bin, SF_m_LL = bin_data(yd, SF_m_LL, nbins)
                if any("LLL" in t for t in traditional_type):
                    xd_bin, SF_z_LLL = bin_data(xd, SF_z_LLL, nbins)
                    yd_bin, SF_m_LLL = bin_data(yd, SF_m_LLL, nbins)
                if any("LTT" in t for t in traditional_type):
                    xd_bin, SF_z_LTT = bin_data(xd, SF_z_LTT, nbins)
                    yd_bin, SF_m_LTT = bin_data(yd, SF_m_LTT, nbins)
        if scalar is not None:
            xd_bin, SF_z_scalar = bin_data(xd, SF_z_scalar, nbins)
            yd_bin, SF_m_scalar = bin_data(yd, SF_m_scalar, nbins)
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    xd_bin, SF_z_LSS = bin_data(xd, SF_z_LSS, nbins)
                    yd_bin, SF_m_LSS = bin_data(yd, SF_m_LSS, nbins)
        xd = xd_bin
        yd = yd_bin

    data = {
        "SF_advection_velocity_zonal": SF_z,
        "SF_advection_velocity_meridional": SF_m,
        "SF_advection_scalar_zonal": SF_z_scalar,
        "SF_advection_scalar_meridional": SF_m_scalar,
        "SF_LL_zonal": SF_z_LL,
        "SF_LL_meridional": SF_m_LL,
        "SF_LLL_zonal": SF_z_LLL,
        "SF_LLL_meridional": SF_m_LLL,
        "SF_LTT_zonal": SF_z_LTT,
        "SF_LTT_meridional": SF_m_LTT,
        "SF_LSS_zonal": SF_z_LSS,
        "SF_LSS_meridional": SF_m_LSS,
        "x-diffs": xd,
        "y-diffs": yd,
    }
    return data
