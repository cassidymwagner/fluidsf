import numpy as np
import pandas as pd
from .calculate_velocity_advection import calculate_velocity_advection


def advection_velocity(par_u, par_v, x, y, boundary="Periodic"):
    """
    Add docstring
    """
    u = par_u
    v = par_v

    if boundary == "Periodic":
        sep = range(int(len(u) / 2))
    else:
        sep = range(int(len(u)))

    SF_z = np.zeros(np.shape(sep))
    SF_m = np.zeros(np.shape(sep))
    SF_iso = np.zeros(np.shape(sep))
    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    adv_E, adv_N = calculate_velocity_advection(u, v, x, y)

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x, i, axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y, i, axis=0) - y))[len(sep)]

        SF_z[i] = np.nanmean(
            (np.roll(adv_E, i, axis=1) - adv_E) * (np.roll(u, i, axis=1) - u)
            + (np.roll(adv_N, i, axis=1) - adv_N) * (np.roll(v, i, axis=1) - v)
        )

        SF_m[i] = np.nanmean(
            (np.roll(adv_E, i, axis=0) - adv_E) * (np.roll(u, i, axis=0) - u)
            + (np.roll(adv_N, i, axis=0) - adv_N) * (np.roll(v, i, axis=0) - v)
        )

    #Isotropic sampling
    sep_combinations = np.array(np.meshgrid(sep,sep)).T.reshape(-1,2)
    tmp = np.zeros(np.shape(sep_combinations))
    for idx,xy in enumerate(sep_combinations):
        sep_distance = np.round(np.sqrt(xy[0]**2 + xy[1]**2))

        SF_iso = np.nanmean(
            (np.roll(adv_E, xy[0]) - adv_E) * (np.roll(u, xy[0]) - u)
            + (np.roll(adv_N, xy[1]) - adv_N) * (np.roll(v, xy[1]) - v)
        ) 

        tmp[idx] = [sep_distance,SF_iso]
    
    df = pd.DataFrame(tmp)
    df_mean = df.groupby(0).mean().reset_index()
    isod = df_mean.iloc[:,0] #Binned separation distances
    SF_iso = df_mean.iloc[:,1]
    
    return (SF_z, SF_m, SF_iso, xd, yd, isod)
