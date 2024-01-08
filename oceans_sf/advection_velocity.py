import numpy as np
import pandas as pd
from geopy.distance import great_circle

from .calculate_velocity_advection import calculate_velocity_advection
from .shift_array1d import shift_array1d
from .shift_array2d import shift_array2d


def advection_velocity(  # noqa: C901
    par_u,
    par_v,
    x,
    y,
    dx=None,
    dy=None,
    boundary="Periodic",
    even="True",
    grid_type="uniform",
    nbins=10,
):
    """Add docstring."""
    u = par_u
    v = par_v

    if boundary == "Periodic":
        sep_z = range(int(len(y) / 2))
    else:
        sep_z = range(int(len(y) - 1))

    yd = np.zeros(np.shape(sep_z))

    SF_z = np.zeros(np.shape(sep_z))

    if even is False:
        yd_uneven = np.zeros(np.shape(sep_z))

    if boundary == "Periodic":
        sep_m = range(int(len(x) / 2))
    else:
        sep_m = range(int(len(x) - 1))

    xd = np.zeros(np.shape(sep_m))

    SF_m = np.zeros(np.shape(sep_m))

    if even is False:
        xd_uneven = np.zeros(np.shape(sep_m))

    adv_E, adv_N = calculate_velocity_advection(u, v, x, y, dx, dy, grid_type)

    if len(sep_m) < len(sep_z):
        seps = sep_m
    else:
        seps = sep_z

    for down, left in (range(1, len(sep_m)), range(1, len(sep_z))):
        xroll = shift_array1d(x, shift_by=left, boundary=boundary)
        yroll = shift_array1d(y, shift_by=down, boundary=boundary)

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

        SF_m[down] = np.nanmean(
            (adv_E_roll_down - adv_E) * (u_roll_down - u)
            + (adv_N_roll_down - adv_N) * (v_roll_down - v)
        )

        SF_z[left] = np.nanmean(
            (adv_E_roll_left - adv_E) * (u_roll_left - u)
            + (adv_N_roll_left - adv_N) * (v_roll_left - v)
        )

        if grid_type == "latlon":
            xd[left] = np.abs(
                great_circle((xroll[left], y[left]), (x[left], y[left])).meters
            )
            yd[down] = np.abs(
                great_circle((x[down], yroll[down]), (x[down], y[down])).meters
            )
        else:
            xd[left] = (np.abs(xroll - x))[len(sep_m)]
            yd[down] = (np.abs(yroll - y))[len(sep_z)]

    if even is False:
        tmp = {"d": yd, "SF_z": SF_z}
        df = pd.DataFrame(tmp)
        means = df.groupby(pd.qcut(df["d"], q=nbins, duplicates="drop")).mean()
        yd_uneven = means["d"].values
        SF_z_uneven = means["SF_z"].values

    try:
        type(SF_z)
    except NameError:
        SF_z = None

    try:
        type(SF_z_uneven)
    except NameError:
        SF_z_uneven = None

    # Commented this out for later use -- I want to add in this functionality,
    # but I don't want to conflict with SF_z_uneven until I can test that the
    # new version is unchanged compared to the previous.
    # try:
    #     type(SF_m_uneven)
    # except NameError:
    #     SF_m_uneven = None

    try:
        type(SF_m)
    except NameError:
        SF_m = None

    try:
        type(SF_iso)
    except NameError:
        SF_iso = None

    try:
        type(xd)
    except NameError:
        xd = None

    try:
        type(yd)
    except NameError:
        yd = None

    try:
        type(isod)
    except NameError:
        isod = None

    try:
        type(yd_uneven)
    except NameError:
        yd_uneven = None

    try:
        type(xd_uneven)
    except NameError:
        xd_uneven = None

    data = {
        "SF_zonal": SF_z,
        "SF_zonal_uneven": SF_z_uneven,
        "SF_meridional": SF_m,
        "SF_isotropic": SF_iso,
        "x-diffs": xd,
        "y-diffs": yd,
        "iso-diffs": isod,
        "x-diffs_uneven": xd_uneven,
        "y-diffs_uneven": yd_uneven,
    }

    return data
