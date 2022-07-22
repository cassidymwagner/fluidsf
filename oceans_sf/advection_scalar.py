import numpy as np
from .calculate_advection import calculate_advection

def advection_scalar(par_u, par_v, x, y, boundary="Periodic"):
    """
    Add docstring
    """
    u = par_u
    v = par_v

    if boundary=="Periodic":
        sep = range(int(len(u)/2))
    else:
        sep = range(int(len(u)))

    SF_z = np.zeros(np.shape(sep))
    SF_m = np.zeros(np.shape(sep))
    xd = np.zeros(np.shape(sep))
    yd = np.zeros(np.shape(sep))

    adv_E, adv_N = calculate_advection(u,v,x,y)

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x,i,axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y,i,axis=0) - y))[len(sep)]

        SF_z[i] = 0.5 * np.nanmean( (np.roll(adv_E,i,axis=1) - adv_E) *  
                                    (np.roll(u,i,axis=1) - u) + 
                                    (np.roll(adv_N,i,axis=1) - adv_N) * 
                                    (np.roll(v,i,axis=1) - v) )
        
        SF_m[i] = 0.5 * np.nanmean( (np.roll(adv_E,i,axis=0) - adv_E) * 
                                    (np.roll(u,i,axis=0) - u) + 
                                    (np.roll(adv_N,i,axis=0) - adv_N) *
                                    (np.roll(v,i,axis=0) - v) )

    return(SF_z,SF_m,xd,yd)