import numpy as np
import pandas as pd
from .calculate_velocity_advection import calculate_velocity_advection


def advection_velocity(
    par_u,
    par_v,
    x,
    y,
    boundary="Periodic",
    zonal=True,
    meridional=True,
    isotropic=False,
):
    """
    Add docstring
    """
    u = par_u
    v = par_v

    if boundary == "Periodic":
        sep = range(int(len(u) / 2))
    else:
        sep = range(int(len(u)))

    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    if zonal == True:
        SF_z = np.zeros(np.shape(sep))

    if meridional == True:
        SF_m = np.zeros(np.shape(sep))

    if isotropic == True:
        SF_iso = np.zeros(np.shape(sep))

    if zonal == False and meridional == False and isotropic == False:
        raise Error(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )

    adv_E, adv_N = calculate_velocity_advection(u, v, x, y)

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x, i, axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y, i, axis=0) - y))[len(sep)]

        if zonal == True:
            SF_z[i] = np.nanmean(
                (np.roll(adv_E, i, axis=1) - adv_E) * (np.roll(u, i, axis=1) - u)
                + (np.roll(adv_N, i, axis=1) - adv_N) * (np.roll(v, i, axis=1) - v)
            )

        if meridional == True:
            SF_m[i] = np.nanmean(
                (np.roll(adv_E, i, axis=0) - adv_E) * (np.roll(u, i, axis=0) - u)
                + (np.roll(adv_N, i, axis=0) - adv_N) * (np.roll(v, i, axis=0) - v)
            )

    if isotropic == True:
        sep_combinations = np.array(np.meshgrid(sep, sep)).T.reshape(-1, 2)
        tmp = np.zeros(np.shape(sep_combinations))
        for idx, xy in enumerate(sep_combinations):
            sep_distance = np.round(np.sqrt(xy[0] ** 2 + xy[1] ** 2))

            SF_iso = np.nanmean(
                (np.roll(adv_E, xy[0]) - adv_E) * (np.roll(u, xy[0]) - u)
                + (np.roll(adv_N, xy[1]) - adv_N) * (np.roll(v, xy[1]) - v)
            )

            tmp[idx] = [sep_distance, SF_iso]

        df = pd.DataFrame(tmp)
        df_mean = df.groupby(0).mean().reset_index()
        isod = df_mean.iloc[:, 0]
        SF_iso = df_mean.iloc[:, 1]

    if zonal == False and meridional == False and isotropic == False:
        raise Error(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )

    try:
        SF_z
    except NameError:
        SF_z = None

    try:
        SF_m
    except NameError:
        SF_m = None

    try:
        SF_iso
    except NameError:
        SF_iso = None

    try:
        xd
    except NameError:
        xd = None

    try:
        yd
    except NameError:
        yd = None

    try:
        isod
    except NameError:
        isod = None

    data = {
        "SF_zonal": SF_z,
        "SF_meridional": SF_m,
        "SF_isotropic": SF_iso,
        "x-diffs": xd,
        "y-diffs": yd,
        "iso-diffs": isod,
    }

    return data
