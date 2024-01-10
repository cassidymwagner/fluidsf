import numpy as np


def calculate_advection_scalar_structure_function(scalar, adv, scalar_shift, adv_shift):
    """
    Calculate the scalar-based advective structure function.

    Args
    ----
    scalar (numpy.ndarray): Array of scalar values.
    adv (numpy.ndarray): Array of advection values.
    scalar_shift (numpy.ndarray): Array of shifted scalar values.
    adv_shift (numpy.ndarray): Array of shifted advection values.

    Returns
    -------
    float: The scalar-based advective structure function.
    """
    SF = np.nanmean((adv_shift - adv) * (scalar_shift - scalar))

    return SF
