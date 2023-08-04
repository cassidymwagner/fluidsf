import numpy as np


def calculate_velocity_advection(par_u, par_v, x, y, boundary="Periodic"):
    """
    Add docstring
    """
    u = par_u
    v = par_v

    dx = np.abs(x[0] - x[1])
    dy = np.abs(y[0] - y[1])

    u_ip1 = np.roll(u, -1, axis=1)
    u_im1 = np.roll(u, 1, axis=1)
    v_ip1 = np.roll(v, -1, axis=1)
    v_im1 = np.roll(v, 1, axis=1)

    v_jp1 = np.roll(v, -1, axis=0)
    v_jm1 = np.roll(v, 1, axis=0)
    u_jp1 = np.roll(u, -1, axis=0)
    u_jm1 = np.roll(u, 1, axis=0)

    dudx = (u_ip1 - u_im1) / (2 * dx)
    dvdx = (v_ip1 - v_im1) / (2 * dx)
    dudy = (u_jp1 - u_jm1) / (2 * dy)
    dvdy = (v_jp1 - v_jm1) / (2 * dy)

    if boundary == "Periodic":

        eastward_advection = u * dudx + v * dudy
        northward_advection = u * dvdx + v * dvdy

    else:

        eastward_advection = (u * dudx + v * dudy)[1:-1, 1:-1]
        northward_advection = (u * dvdx + v * dvdy)[1:-1, 1:-1]

    return (eastward_advection, northward_advection)
