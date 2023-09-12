import numpy as np
import pandas as pd

# import geopy.distance as gd


def traditional_velocity(
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
    order=3,
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

    # if isotropic == True:
    #     SF_iso = np.zeros(np.shape(sep))

    if zonal == False and meridional == False and isotropic == False:
        raise SystemExit(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )
    if len(sep_m) < len(sep_z):
        seps = sep_m
    else:
        seps = sep_z

    if meridional == True:

        for i in range(1, len(sep_m)):
            xroll = np.roll(x, i, axis=0)
            yroll = np.roll(y, i, axis=0)
            xd[i] = (np.abs(xroll - x))[len(sep_m)]

            if boundary == "Periodic":
                dm = np.roll(v, i, axis=0) - v
                dm3 = dm**order

            elif i != 0:
                dm = (
                    np.pad(
                        v,
                        ((0, i), (0, 0)),
                        mode="constant",
                        constant_values=np.nan,
                    )[i:, :]
                    - v
                )
                dm3 = dm**order

            else:
                pass

            SF_m[i] = np.nanmean(dm3)

            if even == False:
                if grid_type == "latlon":
                    # xd_uneven[i] = gd.geodesic((xroll[i], yroll[i]), (y[i], x[i])).km
                    pass
                else:
                    xroll = np.pad(
                        np.float64(x), (i, 0), "constant", constant_values=np.nan
                    )[:-i]
                    xd_uneven[i] = np.abs(xroll - x)[i]

    if zonal == True:

        for i in range(1, len(sep_z)):
            xroll = np.roll(x, i, axis=0)
            yroll = np.roll(y, i, axis=0)
            yd[i] = (np.abs(yroll - y))[len(sep_z)]

            if boundary == "Periodic":
                dz = np.roll(u, i, axis=1) - u
                dz3 = dz**order
            elif i != 0:
                dz = (
                    np.pad(
                        u,
                        ((0, 0), (i, 0)),
                        mode="constant",
                        constant_values=np.nan,
                    )[:, :-i]
                    - u
                )
                dz3 = dz**order
            else:
                pass

            SF_z[i] = np.nanmean(dz3)

            if even == False:
                if grid_type == "latlon":
                    # yd_uneven[i] = gd.geodesic((xroll[i], yroll[i]), (y[i], x[i])).km
                    pass
                else:
                    yroll = np.pad(
                        np.float64(y), (i, 0), "constant", constant_values=np.nan
                    )[:-i]
                    yd_uneven[i] = np.abs(yroll - y)[i]

    if even == False:
        tmp = {"d": yd_uneven, "SF_z": SF_z}
        df = pd.DataFrame(tmp)
        means = df.groupby(pd.qcut(df["d"], q=nbins, duplicates="drop")).mean()
        yd_uneven = means["d"].values
        SF_z_uneven = means["SF_z"].values

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
