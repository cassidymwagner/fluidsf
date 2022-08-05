import numpy as np
from .calculate_scalar_advection import calculate_scalar_advection

def advection_scalar(scalar, par_u, par_v, x, y, boundary="Periodic"):
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

    SF_z = np.zeros(np.shape(sep))
    SF_m = np.zeros(np.shape(sep))
    # SF_iso = np.zeros(np.shape(sep))
    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    adv = calculate_scalar_advection(s, u, v, x, y)

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x, i, axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y, i, axis=0) - y))[len(sep)]

        SF_z[i] = np.nanmean(
            (np.roll(adv, i, axis=1) - adv) * (np.roll(s, i, axis=1) - s)
        )

        SF_m[i] = np.nanmean(
            (np.roll(adv, i, axis=0) - adv) * (np.roll(s, i, axis=0) - s)
        )

    # for i in range(len(sep)):
    #     for j in range(len(sep)):
    #         xd[i] = (np.abs(np.roll(x, i, axis=0) - x))[len(sep)]
    #         yd[j] = (np.abs(np.roll(y, j, axis=0) - y))[len(sep)]

    #         SF_iso[i] = 0.5 * np.nanmean(
    #             (np.roll(adv_E, i) - adv_E) * (np.roll(u, i) - u)
    #             + (np.roll(adv_N, j) - adv_N) * (np.roll(v, j) - v)
    #         )            

    return (SF_z, SF_m, xd, yd)
    # return (SF_z, SF_m, SF_iso, xd, yd)
