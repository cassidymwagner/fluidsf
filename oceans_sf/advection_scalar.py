import numpy as np
from .calculate_scalar_advection import calculate_scalar_advection


def advection_scalar(
    scalar,
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
    s = scalar

    if boundary == "Periodic":
        sep = range(int(len(u) / 2))
    else:
        sep = range(int(len(u)))

    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    if zonal == True:
        SF_z = np.zeros(np.shape(sep))

    elif meridional == True:
        SF_m = np.zeros(np.shape(sep))

    elif isotropic == True:
        SF_iso = np.zeros(np.shape(sep))

    else:
        raise Error(
            "You must select at least one of the sampling options: meridional, zonal, or isotropic."
        )

    adv = calculate_scalar_advection(s, u, v, x, y)

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x, i, axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y, i, axis=0) - y))[len(sep)]

        if zonal == True:
            SF_z[i] = np.nanmean(
                (np.roll(adv, i, axis=1) - adv) * (np.roll(s, i, axis=1) - s)
            )
        if meridional == True:
            SF_m[i] = np.nanmean(
                (np.roll(adv, i, axis=0) - adv) * (np.roll(s, i, axis=0) - s)
            )

    if isotropic == True:
        sep_combinations = np.array(np.meshgrid(sep, sep)).T.reshape(-1, 2)
        tmp = np.zeros(np.shape(sep_combinations))
        for idx, xy in enumerate(sep_combinations):
            sep_distance = np.round(np.sqrt(xy[0] ** 2 + xy[1] ** 2))

            SF_iso = np.nanmean((np.roll(adv, xy[0]) - adv) * (np.roll(s, xy[0]) - s))

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

    return (SF_z, SF_m, SF_iso, xd, yd, isod)
