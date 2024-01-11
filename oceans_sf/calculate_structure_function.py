import numpy as np

from .shift_array2d import shift_array2d


def calculate_structure_function(
    u,
    v,
    adv_e,
    adv_n,
    down,
    right,
    skip_velocity_sf=False,
    scalar=None,
    adv_scalar=None,
    traditional_order=0,
    boundary="Periodic",
):
    """
    Calculate structure function, either advective or traditional.
    Supports velocity-based structure functions and scalar-based structure functions.

    Args:
    ----
        u (numpy.ndarray): Array of u velocities.
        v (numpy.ndarray): Array of v velocities.
        adv_e (numpy.ndarray): Array of eastward advection values.
        adv_n (numpy.ndarray): Array of northward advection values.
        down (int): Shift amount for downward shift. For periodic data
        should be less than half the column length and less than the column length for
        other boundary conditions.
        right (int): Shift amount for rightward shift. For periodic data
        should be less than half the row length and less than the row length for
        other boundary conditions.
        skip_velocity_sf (bool, optional): Whether to skip velocity-based structure
        function calculation. Defaults to False.
        scalar (numpy.ndarray, optional): Array of scalar values. Defaults to None.
        adv_scalar (numpy.ndarray, optional): Array of scalar advection values.
        Defaults to None.
        traditional_order (int, optional): Order for calculating traditional
        non-advective structure functions. If 0, no traditional structure functions
        are calculated. Defaults to 0.
        boundary (str, optional): Boundary condition for shifting arrays.
        Defaults to "Periodic".

    Returns:
    -------
        dict: A dictionary containing the advection velocity structure functions and
        scalar structure functions (if applicable).
            The dictionary has the following keys:
            - 'SF_velocity_right': The advection velocity structure function in the
            right direction.
            - 'SF_velocity_down': The advection velocity structure function in the down
            direction.
            - 'SF_trad_velocity_right': The traditional velocity structure function in
            the right direction (if traditional_order > 0).
            - 'SF_trad_velocity_down': The traditional velocity structure function in
            the down direction (if traditional_order > 0).
            - 'SF_scalar_right': The scalar structure function in the right direction
            (if scalar is provided).
            - 'SF_scalar_down': The scalar structure function in the down direction
            (if scalar is provided).
            - 'SF_trad_scalar_right': The traditional scalar structure function in the
            right direction (if scalar is provided and traditional_order > 0).
            - 'SF_trad_scalar_down': The traditional scalar structure function in the
            down direction (if scalar is provided and traditional_order > 0).
    """
    inputs = {
        "u": u,
        "v": v,
        "adv_e": adv_e,
        "adv_n": adv_n,
        "scalar": scalar,
        "adv_scalar": adv_scalar,
    }

    if skip_velocity_sf is True:
        inputs.update(
            {
                "u": None,
                "v": None,
                "adv_e": None,
                "adv_n": None,
            }
        )

    shifted_inputs = {}

    for key, value in inputs.items():
        if value is not None:
            right_shift, down_shift = shift_array2d(
                inputs[key], shift_down=down, shift_right=right, boundary=boundary
            )

            shifted_inputs.update(
                {
                    key + "_right_shift": right_shift,
                    key + "_down_shift": down_shift,
                }
            )

    inputs.update(shifted_inputs)
    SF_dict = {}

    for direction in ["right", "down"]:
        if skip_velocity_sf is False:
            SF_dict["SF_velocity_" + direction] = np.nanmean(
                (inputs["adv_e_" + direction + "_shift"] - adv_e)
                * (inputs["u_" + direction + "_shift"] - u)
                + (inputs["adv_n_" + direction + "_shift"] - adv_n)
                * (inputs["v_" + direction + "_shift"] - v)
            )
            if traditional_order > 0:
                N = traditional_order
                SF_dict["SF_trad_velocity_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u) ** N
                )

        if scalar is not None:
            SF_dict["SF_scalar_" + direction] = np.nanmean(
                (inputs["adv_scalar_" + direction + "_shift"] - adv_scalar)
                * (inputs["scalar_" + direction + "_shift"] - scalar)
            )
            if traditional_order > 0:
                N = traditional_order
                SF_dict["SF_trad_scalar_" + direction] = np.nanmean(
                    (inputs["scalar_" + direction + "_shift"] - scalar) ** N
                )
    return SF_dict
