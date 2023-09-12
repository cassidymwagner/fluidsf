import numpy as np
import pandas as pd
import geopy.distance as gd
from .calculate_velocity_advection import calculate_velocity_advection


def advection_velocity(
    par_u,
    par_v,
    x,
    y,
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
    b = boundary

    # if boundary == "Periodic":
    #     sep = range(int(len(u) / 2))
    # else:
    #     sep = range(int(len(u)) - 1)

    # xd = np.zeros(np.shape(sep))
    # yd = np.zeros(np.shape(sep))

    # if even == False:
    #     d_uneven = np.zeros(np.shape(sep))

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

    # if isotropic == True:
    #     SF_iso = np.zeros(np.shape(sep))

    if zonal == False and meridional == False and isotropic == False:
        raise SystemExit(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )

    adv_E, adv_N = calculate_velocity_advection(u, v, x, y)

    if len(sep_m) < len(sep_z):
        seps = sep_m
    else:
        seps = sep_z

    if meridional == True:
        # if boundary == "Periodic":
        #     sep = range(int(len(y) / 2))
        # else:
        #     sep = range(int(len(y)) - 1)

        for i in range(1, len(sep_m)):
            xroll = np.roll(x, i, axis=0)
            yroll = np.roll(y, i, axis=0)
            xd[i] = (np.abs(xroll - x))[len(sep_m)]
            # yd[i] = (np.abs(yroll - y))[len(sep)]
            if boundary == "Periodic":
                SF_m[i] = np.nanmean(
                    (np.roll(adv_E, i, axis=0) - adv_E) * (np.roll(u, i, axis=0) - u)
                    + (np.roll(adv_N, i, axis=0) - adv_N) * (np.roll(v, i, axis=0) - v)
                )
            elif i != 0:
                SF_m[i] = np.nanmean(
                    (
                        (
                            np.pad(
                                adv_E,
                                ((i, 0), (0, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:-i, :]
                            - adv_E
                        )
                        * (
                            np.pad(
                                u,
                                ((i, 0), (0, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:-i, :]
                            - u
                        )
                        + (
                            np.pad(
                                adv_N,
                                ((i, 0), (0, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:-i, :]
                            - adv_N
                        )
                        * (
                            np.pad(
                                v,
                                ((i, 0), (0, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:-i, :]
                            - v
                        )
                    )
                )
            else:
                pass

            if even == False:

                if grid_type == "latlon":

                    xd_uneven[i] = gd.geodesic(
                        (xroll[i], yroll[i]), (y[i], x[i])
                    ).km  # Geopy takes lat,lon instead of lon,lat; may need to change later

                else:
                    # xd_uneven[i] = gd.geodesic((xroll[i], yroll[i]), (x[i], y[i])).km
                    xroll = np.pad(
                        np.float64(x), (i, 0), "constant", constant_values=np.nan
                    )[:-i]
                    xd_uneven[i] = np.abs(xroll - x)[i]

    if zonal == True:
        # if boundary == "Periodic":
        #     sep = range(int(len(x) / 2))
        # else:
        #     sep = range(int(len(x)) - 1)

        for i in range(1, len(sep_z)):
            xroll = np.roll(x, i, axis=0)
            yroll = np.roll(y, i, axis=0)
            # xd[i] = (np.abs(xroll - x))[len(sep)]
            yd[i] = (np.abs(yroll - y))[len(sep_z)]

            if boundary == "Periodic":
                SF_z[i] = np.nanmean(
                    (np.roll(adv_E, i, axis=1) - adv_E) * (np.roll(u, i, axis=1) - u)
                    + (np.roll(adv_N, i, axis=1) - adv_N) * (np.roll(v, i, axis=1) - v)
                )
            elif i != 0:
                SF_z[i] = np.nanmean(
                    (
                        (
                            np.pad(
                                adv_E,
                                ((0, 0), (i, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:, :-i]
                            - adv_E
                        )
                        * (
                            np.pad(
                                u,
                                ((0, 0), (i, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:, :-i]
                            - u
                        )
                        + (
                            np.pad(
                                adv_N,
                                ((0, 0), (i, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:, :-i]
                            - adv_N
                        )
                        * (
                            np.pad(
                                v,
                                ((0, 0), (i, 0)),
                                mode="constant",
                                constant_values=np.nan,
                            )[:, :-i]
                            - v
                        )
                    )
                )
            else:
                pass

            if even == False:

                if grid_type == "latlon":

                    yd_uneven[i] = gd.geodesic(
                        (xroll[i], yroll[i]), (y[i], x[i])
                    ).km  # Geopy takes lat,lon instead of lon,lat; may need to change later

                else:
                    # yroll = np.roll(y, i, axis=0)
                    yroll = np.pad(
                        np.float64(y), (i, 0), "constant", constant_values=np.nan
                    )[:-i]
                    yd_uneven[i] = np.abs(yroll - y)[i]
                    # yd_uneven[i] = gd.geodesic((xroll[i], yroll[i]), (x[i], y[i])).km

    if even == False:
        tmp = {"d": yd_uneven, "SF_z": SF_z}
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
