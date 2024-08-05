import itertools

import numpy as np

from .calculate_advection_2d import calculate_advection_2d
from .calculate_sf_maps_2d import calculate_sf_maps_2d


def generate_sf_maps_2d(  # noqa: C901, D417
    u,
    v,
    x,
    y,
    sf_type=["ASF_V"],  # noqa: B006
    scalar=None,
    dx=None,
    dy=None,
    grid_type="uniform",
):
    """
    Full method for generating 2D maps of structure functions for 2D data, either
    advective or traditional structure functions. Supports velocity-based and
    scalar-based structure functions. Defaults to calculating the velocity-based
    advective structure functions for the x and y directions. Can only be used with
    evenly-spaced and periodic data.

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
        sf_type: list
            List of structure function types to calculate. Accepted types are:
            "ASF_V", "ASF_S", "LL", "TT", "SS", "LLL", "LTT", "LSS". Defaults to
            ["ASF_V"].
        scalar: ndarray, optional
            2D array of scalar values. Defaults to None.
        dx: float, optional
            Grid spacing in the x-direction. Defaults to None.
        dy: float, optional
            Grid spacing in the y-direction. Defaults to None.
        grid_type:str, optional
            Type of grid, can only be "uniform" for these maps.

    Returns
    -------
        dict:
            Dictionary containing the requested structure functions and separation
            distances for the x- and y-directions.

    """
    # Initialize variables as NoneType
    SF_adv = None
    adv_x = None
    adv_y = None
    SF_scalar_adv = None
    adv_scalar = None
    SF_LL = None
    SF_TT = None
    SF_SS = None
    SF_LLL = None
    SF_LTT = None
    SF_LSS = None
    separation_distances = None
    separation_angles = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    x_shifts = range(0, int(len(x) / 2))
    y_shifts = range(-int(len(y) / 2), int(len(y) / 2))

    # Initialize the structure functions and other arrays

    separation_distances = np.zeros([len(x_shifts), len(y_shifts)])
    separation_angles = np.zeros([len(x_shifts), len(y_shifts)])

    x_separations = np.zeros([len(x_shifts), len(y_shifts)])
    y_separations = np.zeros([len(x_shifts), len(y_shifts)])

    if any("ASF_V" in t for t in sf_type):
        SF_adv = np.zeros([len(x_shifts), len(y_shifts)])
        adv_x, adv_y = calculate_advection_2d(u, v, x, y, dx, dy, grid_type)
    if any("ASF_S" in t for t in sf_type):
        SF_scalar_adv = np.zeros([len(x_shifts), len(y_shifts)])
        adv_scalar = calculate_advection_2d(u, v, x, y, dx, dy, grid_type, scalar)
    if any("LL" in t for t in sf_type):
        SF_LL = np.zeros([len(x_shifts), len(y_shifts)])
    if any("TT" in t for t in sf_type):
        SF_TT = np.zeros([len(x_shifts), len(y_shifts)])
    if any("SS" in t for t in sf_type):
        SF_SS = np.zeros([len(x_shifts), len(y_shifts)])
    if any("LLL" in t for t in sf_type):
        SF_LLL = np.zeros([len(x_shifts), len(y_shifts)])
    if any("LTT" in t for t in sf_type):
        SF_LTT = np.zeros([len(x_shifts), len(y_shifts)])
    if any("LSS" in t for t in sf_type):
        SF_LSS = np.zeros([len(x_shifts), len(y_shifts)])

    # Iterate over separations right and down
    for x_shift, y_shift in itertools.product(x_shifts, y_shifts):
        x_separation = x_shift * (x[1] - x[0])
        y_separation = y_shift * (y[1] - y[0])
        if x_shift == 0:
            separation_angles[x_shift, y_shift + int(len(y) / 2)] = (
                np.sign(y_separation) * np.pi / 2
            )
        else:
            separation_angles[x_shift, y_shift + int(len(y) / 2)] = np.arctan(
                y_separation / x_separation
            )

        SF_dicts = calculate_sf_maps_2d(
            u,
            v,
            x,
            y,
            adv_x,
            adv_y,
            x_shift,
            y_shift,
            sf_type,
            scalar,
            adv_scalar,
        )

        separation_distances[x_shift, y_shift + int(len(y) / 2)] = np.sqrt(
            x_separation**2 + y_separation**2
        )
        x_separations[x_shift, y_shift + int(len(y) / 2)] = x_separation
        y_separations[x_shift, y_shift + int(len(y) / 2)] = y_separation

        if any("ASF_V" in t for t in sf_type):
            SF_adv[x_shift, y_shift + int(len(y) / 2)] = SF_dicts[
                "SF_advection_velocity_xy"
            ]
        if any("ASF_S" in t for t in sf_type):
            SF_scalar_adv[x_shift, y_shift + int(len(y) / 2)] = SF_dicts[
                "SF_advection_velocity_xy"
            ]
        if any("LL" in t for t in sf_type):
            SF_LL[x_shift, y_shift + int(len(y) / 2)] = SF_dicts["SF_LL_xy"]
        if any("TT" in t for t in sf_type):
            SF_TT[x_shift, y_shift + int(len(y) / 2)] = SF_dicts["SF_TT_xy"]
        if any("SS" in t for t in sf_type):
            SF_SS[x_shift, y_shift + int(len(y) / 2)] = SF_dicts["SF_SS_xy"]
        if any("LLL" in t for t in sf_type):
            SF_LLL[x_shift, y_shift + int(len(y) / 2)] = SF_dicts["SF_LLL_xy"]
        if any("LTT" in t for t in sf_type):
            SF_LTT[x_shift, y_shift + int(len(y) / 2)] = SF_dicts["SF_LTT_xy"]
        if any("LSS" in t for t in sf_type):
            SF_LSS[x_shift, y_shift + int(len(y) / 2)] = SF_dicts["SF_LSS_xy"]

    # When saving data, roll y-axis so that y-values go from most negative to most
    # positive. The arrays created above run y-separations of 0, to most positive, then
    # most negative towards zero, since new_array[-n] writes to the n-th from last index

    data = {
        "SF_advection_velocity_xy": SF_adv,
        "SF_advection_scalar_xy": SF_scalar_adv,
        "SF_LL_xy": SF_LL,
        "SF_TT_xy": SF_TT,
        "SF_SS_xy": SF_SS,
        "SF_LLL_xy": SF_LLL,
        "SF_LTT_xy": SF_LTT,
        "SF_LSS_xy": SF_LSS,
        "separation_distances": separation_distances,
        "separation_angles": separation_angles,
        "x_separations": x_separations,
        "y_separations": y_separations,
    }
    return data
