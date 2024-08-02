import numpy as np

from .bin_data import bin_data
from .calculate_advection_3d import calculate_advection_3d
from .calculate_separation_distances_3d import calculate_separation_distances_3d
from .calculate_structure_function_3d import calculate_structure_function_3d
from .shift_array_1d import shift_array_1d


def generate_structure_functions_3d(  # noqa: C901, D417
    u,
    v,
    w,
    x,
    y,
    z,
    sf_type=["ASF_V"],  # noqa: B006
    scalar=None,
    boundary="periodic-all",
    nbins=None,
):
    """
    Full method for generating structure functions for uniform and even 3D data, either
    advective or traditional structure functions. Supports velocity-based and
    scalar-based structure functions. Defaults to calculating the
    velocity-based advective structure functions for the x, y, and z directions.

    Parameters
    ----------
        u: ndarray
            3D array of u velocity components.
        v: ndarray
            3D array of v velocity components.
        w: ndarray
            3D array of w velocity components.
        x: ndarray
            1D array of x-coordinates.
        y: ndarray
            1D array of y-coordinates.
        z: ndarray
            1D array of z-coordinates.
        sf_type: list
            List of structure function types to calculate. Accepted types are:
            "ASF_V", "ASF_S", "LL", "TT", "SS", "LLL", "LTT", "LSS". Defaults to
            ["ASF_V"].
        scalar: ndarray, optional
            3D array of scalar values. Defaults to None.
        boundary: str, optional
            Boundary condition of the data. Accepted strings are "periodic-x",
            "periodic-y", "periodic-z", and "periodic-all". Defaults to "periodic-all".
        nbins: int, optional
            Number of bins in the structure function. Defaults to None, i.e. does
            not bin the data.

    Returns
    -------
        dict:
            Dictionary containing the requested structure functions and separation
            distances for the x, y, and z directions.

    """
    # Initialize variables as NoneType
    SF_adv_x = None
    SF_adv_y = None
    SF_adv_z = None
    SF_x_scalar = None
    SF_y_scalar = None
    SF_z_scalar = None
    adv_x = None
    adv_y = None
    adv_z = None
    adv_scalar = None
    SF_x_LL = None
    SF_y_LL = None
    SF_z_LL = None
    SF_x_TT = None
    SF_y_TT = None
    SF_z_TT = None
    SF_x_SS = None
    SF_y_SS = None
    SF_z_SS = None
    SF_x_LLL = None
    SF_y_LLL = None
    SF_z_LLL = None
    SF_x_LTT = None
    SF_y_LTT = None
    SF_z_LTT = None
    SF_x_LSS = None
    SF_y_LSS = None
    SF_z_LSS = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    sep_x = range(1, int(len(x) - 1))
    sep_y = range(1, int(len(y) - 1))
    sep_z = range(1, int(len(z) - 1))

    if boundary is not None:
        if "periodic-all" in boundary:
            sep_x = range(1, int(len(x) / 2))
            sep_y = range(1, int(len(y) / 2))
            sep_z = range(1, int(len(z) / 2))
        if "periodic-x" in boundary:
            sep_x = range(1, int(len(x) / 2))
        if "periodic-y" in boundary:
            sep_y = range(1, int(len(y) / 2))
        if "periodic-z" in boundary:
            sep_z = range(1, int(len(z) / 2))

    # Initialize the separation distance arrays
    xd = np.zeros(len(sep_x) + 1)
    yd = np.zeros(len(sep_y) + 1)
    zd = np.zeros(len(sep_z) + 1)

    # Initialize the structure function arrays
    if any("ASF_V" in t for t in sf_type):
        SF_adv_x = np.zeros(len(sep_x) + 1)
        SF_adv_y = np.zeros(len(sep_y) + 1)
        SF_adv_z = np.zeros(len(sep_z) + 1)
        adv_x, adv_y, adv_z = calculate_advection_3d(u, v, w, x, y, z)
    if any("ASF_S" in t for t in sf_type):
        SF_x_scalar = np.zeros(len(sep_x) + 1)
        SF_y_scalar = np.zeros(len(sep_y) + 1)
        SF_z_scalar = np.zeros(len(sep_z) + 1)
        adv_scalar = calculate_advection_3d(u, v, w, x, y, z, scalar)
    if any("LL" in t for t in sf_type):
        SF_x_LL = np.zeros(len(sep_x) + 1)
        SF_y_LL = np.zeros(len(sep_y) + 1)
        SF_z_LL = np.zeros(len(sep_z) + 1)
    if any("TT" in t for t in sf_type):
        SF_x_TT = np.zeros(len(sep_x) + 1)
        SF_y_TT = np.zeros(len(sep_y) + 1)
        SF_z_TT = np.zeros(len(sep_z) + 1)
    if any("SS" in t for t in sf_type):
        SF_x_SS = np.zeros(len(sep_x) + 1)
        SF_y_SS = np.zeros(len(sep_y) + 1)
        SF_z_SS = np.zeros(len(sep_z) + 1)
    if any("LLL" in t for t in sf_type):
        SF_x_LLL = np.zeros(len(sep_x) + 1)
        SF_y_LLL = np.zeros(len(sep_y) + 1)
        SF_z_LLL = np.zeros(len(sep_z) + 1)
    if any("LTT" in t for t in sf_type):
        SF_x_LTT = np.zeros(len(sep_x) + 1)
        SF_y_LTT = np.zeros(len(sep_y) + 1)
        SF_z_LTT = np.zeros(len(sep_z) + 1)
    if any("LSS" in t for t in sf_type):
        SF_x_LSS = np.zeros(len(sep_x) + 1)
        SF_y_LSS = np.zeros(len(sep_y) + 1)
        SF_z_LSS = np.zeros(len(sep_z) + 1)

    # Iterate over separations in x, y, and z
    for x_shift in sep_x:
        y_shift = 1
        z_shift = 1
        if boundary is not None:
            if any("periodic-all" in b for b in boundary) or any(
                "periodic-x" in b for b in boundary
            ):
                xroll = shift_array_1d(x, shift_by=x_shift, boundary="Periodic")

            else:
                xroll = shift_array_1d(x, shift_by=x_shift, boundary=None)
        else:
            xroll = shift_array_1d(x, shift_by=x_shift, boundary=None)

        SF_dicts = calculate_structure_function_3d(
            u,
            v,
            w,
            adv_x,
            adv_y,
            adv_z,
            x_shift,
            y_shift,
            z_shift,
            sf_type,
            scalar,
            adv_scalar,
            boundary,
        )

        if any("ASF_V" in t for t in sf_type):
            SF_adv_x[x_shift] = SF_dicts["SF_advection_velocity_x"]
        if any("ASF_S" in t for t in sf_type):
            SF_x_scalar[x_shift] = SF_dicts["SF_advection_scalar_x"]
        if any("LL" in t for t in sf_type):
            SF_x_LL[x_shift] = SF_dicts["SF_LL_x"]
        if any("TT" in t for t in sf_type):
            SF_x_TT[x_shift] = SF_dicts["SF_TT_x"]
        if any("SS" in t for t in sf_type):
            SF_x_SS[x_shift] = SF_dicts["SF_SS_x"]
        if any("LLL" in t for t in sf_type):
            SF_x_LLL[x_shift] = SF_dicts["SF_LLL_x"]
        if any("LTT" in t for t in sf_type):
            SF_x_LTT[x_shift] = SF_dicts["SF_LTT_x"]
        if any("LSS" in t for t in sf_type):
            SF_x_LSS[x_shift] = SF_dicts["SF_LSS_x"]

        # Calculate separation distances in x
        xd[x_shift], tmp, tmp = calculate_separation_distances_3d(
            x[0], y[0], z[0], xroll[0], y[0], z[0]
        )

    for y_shift in sep_y:
        x_shift = 1
        z_shift = 1
        if boundary is not None:
            if any("periodic-all" in b for b in boundary) or any(
                "periodic-y" in b for b in boundary
            ):
                yroll = shift_array_1d(y, shift_by=y_shift, boundary="Periodic")
            else:
                yroll = shift_array_1d(y, shift_by=y_shift, boundary=None)

        else:
            yroll = shift_array_1d(y, shift_by=y_shift, boundary=None)

        SF_dicts = calculate_structure_function_3d(
            u,
            v,
            w,
            adv_x,
            adv_y,
            adv_z,
            x_shift,
            y_shift,
            z_shift,
            sf_type,
            scalar,
            adv_scalar,
            boundary,
        )

        if any("ASF_V" in t for t in sf_type):
            SF_adv_y[y_shift] = SF_dicts["SF_advection_velocity_y"]
        if any("ASF_S" in t for t in sf_type):
            SF_y_scalar[y_shift] = SF_dicts["SF_advection_scalar_y"]
        if any("LL" in t for t in sf_type):
            SF_y_LL[y_shift] = SF_dicts["SF_LL_y"]
        if any("TT" in t for t in sf_type):
            SF_y_TT[y_shift] = SF_dicts["SF_TT_y"]
        if any("SS" in t for t in sf_type):
            SF_y_SS[y_shift] = SF_dicts["SF_SS_y"]
        if any("LLL" in t for t in sf_type):
            SF_y_LLL[y_shift] = SF_dicts["SF_LLL_y"]
        if any("LTT" in t for t in sf_type):
            SF_y_LTT[y_shift] = SF_dicts["SF_LTT_y"]
        if any("LSS" in t for t in sf_type):
            SF_y_LSS[y_shift] = SF_dicts["SF_LSS_y"]

        # Calculate separation distances in y
        tmp, yd[y_shift], tmp = calculate_separation_distances_3d(
            x[0], y[0], z[0], x[0], yroll[0], z[0]
        )

    for z_shift in sep_z:
        x_shift = 1
        y_shift = 1
        if boundary is not None:
            if any("periodic-all" in b for b in boundary) or any(
                "periodic-z" in b for b in boundary
            ):
                zroll = shift_array_1d(z, shift_by=z_shift, boundary="Periodic")

            else:
                zroll = shift_array_1d(z, shift_by=z_shift, boundary=None)
        else:
            zroll = shift_array_1d(z, shift_by=z_shift, boundary=None)

        SF_dicts = calculate_structure_function_3d(
            u,
            v,
            w,
            adv_x,
            adv_y,
            adv_z,
            x_shift,
            y_shift,
            z_shift,
            sf_type,
            scalar,
            adv_scalar,
            boundary,
        )

        if any("ASF_V" in t for t in sf_type):
            SF_adv_z[z_shift] = SF_dicts["SF_advection_velocity_z"]
        if any("ASF_S" in t for t in sf_type):
            SF_z_scalar[z_shift] = SF_dicts["SF_advection_scalar_z"]
        if any("LL" in t for t in sf_type):
            SF_z_LL[z_shift] = SF_dicts["SF_LL_z"]
        if any("TT" in t for t in sf_type):
            SF_z_TT[z_shift] = SF_dicts["SF_TT_z"]
        if any("SS" in t for t in sf_type):
            SF_z_SS[z_shift] = SF_dicts["SF_SS_z"]
        if any("LLL" in t for t in sf_type):
            SF_z_LLL[z_shift] = SF_dicts["SF_LLL_z"]
        if any("LTT" in t for t in sf_type):
            SF_z_LTT[z_shift] = SF_dicts["SF_LTT_z"]
        if any("LSS" in t for t in sf_type):
            SF_z_LSS[z_shift] = SF_dicts["SF_LSS_z"]

        # Calculate separation distances in z
        tmp, tmp, zd[z_shift] = calculate_separation_distances_3d(
            x[0], y[0], z[0], x[0], y[0], zroll[0]
        )

    if nbins is not None:
        if any("ASF_V" in t for t in sf_type):
            xd_bin, SF_adv_x = bin_data(xd, SF_adv_x, nbins)
            yd_bin, SF_adv_y = bin_data(yd, SF_adv_y, nbins)
            zd_bin, SF_adv_z = bin_data(zd, SF_adv_z, nbins)
        if any("ASF_S" in t for t in sf_type):
            xd_bin, SF_x_scalar = bin_data(xd, SF_x_scalar, nbins)
            yd_bin, SF_y_scalar = bin_data(yd, SF_y_scalar, nbins)
            zd_bin, SF_z_scalar = bin_data(zd, SF_z_scalar, nbins)
        if any("LL" in t for t in sf_type):
            xd_bin, SF_x_LL = bin_data(xd, SF_x_LL, nbins)
            yd_bin, SF_y_LL = bin_data(yd, SF_y_LL, nbins)
            zd_bin, SF_z_LL = bin_data(zd, SF_z_LL, nbins)
        if any("TT" in t for t in sf_type):
            xd_bin, SF_x_TT = bin_data(xd, SF_x_TT, nbins)
            yd_bin, SF_y_TT = bin_data(yd, SF_y_TT, nbins)
            zd_bin, SF_z_TT = bin_data(zd, SF_z_TT, nbins)
        if any("SS" in t for t in sf_type):
            xd_bin, SF_x_SS = bin_data(xd, SF_x_SS, nbins)
            yd_bin, SF_y_SS = bin_data(yd, SF_y_SS, nbins)
            zd_bin, SF_z_SS = bin_data(zd, SF_z_SS, nbins)
        if any("LLL" in t for t in sf_type):
            xd_bin, SF_x_LLL = bin_data(xd, SF_x_LLL, nbins)
            yd_bin, SF_y_LLL = bin_data(yd, SF_y_LLL, nbins)
            zd_bin, SF_z_LLL = bin_data(zd, SF_z_LLL, nbins)
        if any("LTT" in t for t in sf_type):
            xd_bin, SF_x_LTT = bin_data(xd, SF_x_LTT, nbins)
            yd_bin, SF_y_LTT = bin_data(yd, SF_y_LTT, nbins)
            zd_bin, SF_z_LTT = bin_data(zd, SF_z_LTT, nbins)
        if any("LSS" in t for t in sf_type):
            xd_bin, SF_x_LSS = bin_data(xd, SF_x_LSS, nbins)
            yd_bin, SF_y_LSS = bin_data(yd, SF_y_LSS, nbins)
            zd_bin, SF_z_LSS = bin_data(zd, SF_z_LSS, nbins)
        xd = xd_bin
        yd = yd_bin
        zd = zd_bin

    data = {
        "SF_advection_velocity_x": SF_adv_x,
        "SF_advection_velocity_y": SF_adv_y,
        "SF_advection_velocity_z": SF_adv_z,
        "SF_advection_scalar_x": SF_x_scalar,
        "SF_advection_scalar_y": SF_y_scalar,
        "SF_advection_scalar_z": SF_z_scalar,
        "SF_LL_x": SF_x_LL,
        "SF_LL_y": SF_y_LL,
        "SF_LL_z": SF_z_LL,
        "SF_TT_x": SF_x_TT,
        "SF_TT_y": SF_y_TT,
        "SF_TT_z": SF_z_TT,
        "SF_SS_x": SF_x_SS,
        "SF_SS_y": SF_y_SS,
        "SF_SS_z": SF_z_SS,
        "SF_LLL_x": SF_x_LLL,
        "SF_LLL_y": SF_y_LLL,
        "SF_LLL_z": SF_z_LLL,
        "SF_LTT_x": SF_x_LTT,
        "SF_LTT_y": SF_y_LTT,
        "SF_LTT_z": SF_z_LTT,
        "SF_LSS_x": SF_x_LSS,
        "SF_LSS_y": SF_y_LSS,
        "SF_LSS_z": SF_z_LSS,
        "x-diffs": xd,
        "y-diffs": yd,
        "z-diffs": zd,
    }
    return data
