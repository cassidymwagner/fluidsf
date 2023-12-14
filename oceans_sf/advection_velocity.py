import numpy as np
import pandas as pd
from .calculate_velocity_advection import calculate_velocity_advection
from geopy.distance import great_circle


def advection_velocity(
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
    zonal=True,
    meridional=True,
    isotropic=False,
):
    """
    Add docstring
    """
    u = par_u
    v = par_v

    if zonal == True:
        if boundary == "Periodic":
            sep_z = range(int(len(y) / 2))
        else:
            sep_z = range(int(len(y) - 1))

        yd = np.zeros(np.shape(sep_z))

        SF_z = np.zeros(np.shape(sep_z))

        if even == False:
            yd_uneven = np.zeros(np.shape(sep_z))

    if meridional == True:
        if boundary == "Periodic":
            sep_m = range(int(len(x) / 2))
        else:
            sep_m = range(int(len(x) - 1))

        xd = np.zeros(np.shape(sep_m))

        SF_m = np.zeros(np.shape(sep_m))

        if even == False:
            xd_uneven = np.zeros(np.shape(sep_m))

    if zonal == False and meridional == False and isotropic == False:
        raise SystemExit(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )

    if grid_type == 'latlon':

        adv_E, adv_N = calculate_velocity_advection(
            u, v, x, y, dx, dy, grid_type)

    else:
        adv_E, adv_N = calculate_velocity_advection(u, v, x, y)

    if len(sep_m) < len(sep_z):
        seps = sep_m
    else:
        seps = sep_z

    if meridional == True:

        if grid_type == 'latlon':
            sep_m = seps

        for i in range(1, len(sep_m)):

            xroll = np.full(np.shape(x), np.nan)
            yroll = np.full(np.shape(y), np.nan)

            adv_E_roll = np.full(np.shape(adv_E), np.nan)
            adv_N_roll = np.full(np.shape(adv_N), np.nan)
            u_roll = np.full(np.shape(u), np.nan)
            v_roll = np.full(np.shape(v), np.nan)

            if boundary == "Periodic":

                xroll[:i] = x[-i:]
                xroll[i:] = x[:-i]
                yroll[:i] = y[-i:]
                yroll[i:] = y[:-i]

                adv_E_roll[:i, :] = adv_E[-i:, :]
                adv_E_roll[i:, :] = adv_E[:-i, :]
                adv_N_roll[:i, :] = adv_N[-i:, :]
                adv_N_roll[i:, :] = adv_N[:-i, :]

                u_roll[:i, :] = u[-i:, :]
                u_roll[i:, :] = u[:-i, :]
                v_roll[:i, :] = v[-i:, :]
                v_roll[i:, :] = v[:-i, :]

            else:

                xroll[i:] = x[:-i]
                yroll[i:] = y[:-i]

                adv_E_roll[i:, :] = adv_E[:-i, :]
                adv_N_roll[i:, :] = adv_N[:-i, :]
                u_roll[i:, :] = u[:-i, :]
                v_roll[i:, :] = v[:-i, :]

            SF_m[i] = np.nanmean(
                (adv_E_roll - adv_E) * (u_roll - u)
                + (adv_N_roll - adv_N) * (v_roll - v)
            )

            if grid_type == 'latlon':
                xd[i] = np.abs(great_circle(
                    (xroll[i], yroll[i]), (x[i], y[i])).meters)
            else:
                xd[i] = (np.abs(xroll - x))[len(sep_m)]

    if zonal == True:

        if grid_type == 'latlon':
            sep_z = seps

        for i in range(1, len(sep_z)):
            xroll = np.full(np.shape(x), np.nan)
            yroll = np.full(np.shape(y), np.nan)

            adv_E_roll = np.full(np.shape(adv_E), np.nan)
            adv_N_roll = np.full(np.shape(adv_N), np.nan)
            u_roll = np.full(np.shape(u), np.nan)
            v_roll = np.full(np.shape(v), np.nan)

            if boundary == "Periodic":

                xroll[:i] = x[-i:]
                xroll[i:] = x[:-i]
                yroll[:i] = y[-i:]
                yroll[i:] = y[:-i]

                adv_E_roll[:, :i] = adv_E[:, -i:]
                adv_E_roll[:, i:] = adv_E[:, :-i]
                adv_N_roll[:, :i] = adv_N[:, -i:]
                adv_N_roll[:, i:] = adv_N[:, :-i]

                u_roll[:, :i] = u[:, -i:]
                u_roll[:, i:] = u[:, :-i]
                v_roll[:, :i] = v[:, -i:]
                v_roll[:, i:] = v[:, :-i]

            else:

                xroll[i:] = x[:-i]
                yroll[i:] = y[:-i]

                adv_E_roll[:, i:] = adv_E[:, :-i]
                adv_N_roll[:, i:] = adv_N[:, :-i]
                u_roll[:, i:] = u[:, :-i]
                v_roll[:, i:] = v[:, :-i]

            SF_z[i] = np.nanmean(
                (adv_E_roll - adv_E) * (u_roll - u)
                + (adv_N_roll - adv_N) * (v_roll - v)
            )

            if grid_type == 'latlon':
                yd[i] = np.abs(great_circle(
                    (xroll[i], yroll[i]), (x[i], y[i])).meters)
            else:
                yd[i] = (np.abs(yroll - y))[len(sep_z)]

    if even == False:
        tmp = {"d": yd, "SF_z": SF_z}
        df = pd.DataFrame(tmp)
        means = df.groupby(pd.qcut(df["d"], q=nbins, duplicates="drop")).mean()
        yd_uneven = means["d"].values
        SF_z_uneven = means["SF_z"].values

    if isotropic == True:
        if boundary == "Periodic":
            sep = range(int(len(x) / 2))
        else:
            sep = range(int(len(x)) - 1)

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
        raise SystemExit(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )

    try:
        SF_z
    except NameError:
        SF_z = None

    try:
        SF_z_uneven
    except NameError:
        SF_z_uneven = None

    try:
        SF_m_uneven
    except NameError:
        SF_m_uneven = None

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

    try:
        yd_uneven
    except NameError:
        yd_uneven = None

    try:
        xd_uneven
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
