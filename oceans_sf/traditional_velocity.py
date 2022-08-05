import numpy as np

def traditional_velocity(par_u, par_v, x, y, boundary="Periodic",order=3):
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

    for i in range(len(sep)):
        xd[i] = (np.abs(np.roll(x,i,axis=0) - x))[len(sep)]
        yd[i] = (np.abs(np.roll(y,i,axis=0) - y))[len(sep)]
        
        dz = np.roll(u,i,axis=1) - u
        dm = np.roll(v,i,axis=0) - v
        dz3 = dz**order
        dm3 = dm**order
        SF_z[i] = np.nanmean(dz3)
        SF_m[i] = np.nanmean(dm3)

    return(SF_z,SF_m,xd,yd)