import numpy as np


def calculate_advection_velocity_structure_function(
    u, v, adv_e, adv_n, u_shift, v_shift, adv_e_shift, adv_n_shift
):
    """
    Calculate the velocity-based advective structure function.

    Args
    ----
    u (numpy.ndarray): Array of u velocities.
    v (numpy.ndarray): Array of v velocities.
    adv_e (numpy.ndarray): Array of eastward advection values.
    adv_n (numpy.ndarray): Array of northward advection values.
    u_shift (numpy.ndarray): Array of shifted u velocities.
    v_shift (numpy.ndarray): Array of shifted v velocities.
    adv_e_shift (numpy.ndarray): Array of shifted eastward advection values.
    adv_n_shift (numpy.ndarray): Array of shifted northward advection values.

    Returns
    -------
    float: The advection velocity structure function.
    """
    SF = np.nanmean(
        (adv_e_shift - adv_e) * (u_shift - u) + (adv_n_shift - adv_n) * (v_shift - v)
    )

    return SF
