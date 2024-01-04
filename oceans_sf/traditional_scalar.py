import numpy as np
import pandas as pd
import geopy.distance as gd


def traditional_scalar(
    scalar, x, y, boundary="Periodic", order=3, even="True", nbins=10
):
    """
    Add docstring
    """

    s = scalar

    if boundary == "Periodic":
        sep = range(int(len(y) / 2))
    else:
        sep = range(int(len(y) - 1))

    SF_z = np.zeros(np.shape(sep))
    SF_m = np.zeros(np.shape(sep))
    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    if even == False:
        d_uneven = np.zeros(np.shape(sep))

    for i in range(len(sep)):
        xroll = np.roll(x, i, axis=0)
        yroll = np.roll(y, i, axis=0)
        xd[i] = (np.abs(xroll - x))[len(sep)]
        yd[i] = (np.abs(yroll - y))[len(sep)]

        dm = np.roll(s, i, axis=0) - s
        dm3 = dm**order
        if boundary == None:
            dm3 = dm[i:] ** order
        SF_m[i] = np.nanmean(dm3)

        dz = np.roll(s, i, axis=1) - s
        dz3 = dz**order
        if boundary == None:
            dz3 = dz[:, i:] ** order
        SF_z[i] = np.nanmean(dz3)

        if even == False:
            d_uneven[i] = gd.geodesic((xroll[i], yroll[i]), (x[i], y[i])).km

    if even == False:
        tmp = {"d": d_uneven, "SF_z": SF_z}
        df = pd.DataFrame(tmp)
        means = df.groupby(pd.qcut(df["d"], q=nbins)).mean()
        d_uneven = means["d"].values
        SF_z_uneven = means["SF_z"].values

    try:
        d_uneven
    except NameError:
        d_uneven = None

    try:
        SF_z_uneven
    except NameError:
        SF_z_uneven = None

    data = {
        "SF_zonal": SF_z,
        "SF_zonal_uneven": SF_z_uneven,
        "SF_meridional": SF_m,
        "x-diffs": xd,
        "y-diffs": yd,
        "x-diffs_uneven": d_uneven,
    }

    return data
