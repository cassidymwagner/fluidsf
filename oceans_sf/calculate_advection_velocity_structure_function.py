import numpy as np

from .shift_array2d import shift_array2d


def calculate_advection_velocity_structure_function(
    u,
    v,
    adv_e,
    adv_n,
    down,
    left,
    skip_velocity_sf=False,
    scalar=None,
    adv_scalar=None,
    boundary="Periodic",
):
    """
    Calculate the advective structure function. Supports velocity-based structure
    functions and scalar-based structure functions.

    Args:
    ----
        u (numpy.ndarray): Array of u velocities.
        v (numpy.ndarray): Array of v velocities.
        adv_e (numpy.ndarray): Array of eastward advection values.
        adv_n (numpy.ndarray): Array of northward advection values.
        down (int): Shift amount for downward shift. For periodic data
        should be less than half the column length and less than the column length for
        other boundary conditions.
        left (int): Shift amount for leftward shift. For periodic data
        should be less than half the row length and less than the row length for
        other boundary conditions.
        skip_velocity_sf (bool, optional): Whether to skip velocity-based structure
        function calculation. Defaults to False.
        scalar (numpy.ndarray, optional): Array of scalar values. Defaults to None.
        adv_scalar (numpy.ndarray, optional): Array of scalar advection values.
        Defaults to None.
        boundary (str, optional): Boundary condition for shifting arrays.
        Defaults to "Periodic".

    Returns:
    -------
        dict: A dictionary containing the advection velocity structure functions and
        scalar structure functions (if applicable).
            The dictionary has the following keys:
            - 'SF_velocity_left': The advection velocity structure function in the left
            direction.
            - 'SF_velocity_down': The advection velocity structure function in the down
            direction.
            - 'SF_scalar_left': The scalar structure function in the left direction
            (if scalar is provided).
            - 'SF_scalar_down': The scalar structure function in the down direction
            (if scalar is provided).
    """
    inputs = {
        "u": u,
        "v": v,
        "adv_e": adv_e,
        "adv_n": adv_n,
        "scalar": scalar,
        "adv_scalar": adv_scalar,
    }

    if skip_velocity_sf is False:
        inputs.update(
            {
                "u": None,
                "v": None,
                "adv_e": None,
                "adv_n": None,
            }
        )

    for key, value in inputs.items():
        if value is not None:
            left_shift, down_shift = shift_array2d(
                inputs[key], shift_down=down, shift_left=left, boundary=boundary
            )

            inputs.update(
                {
                    key + "_left_shift": left_shift,
                    key + "_down_shift": down_shift,
                }
            )

    SF_dict = {}

    for direction in ["left", "down"]:
        if skip_velocity_sf is False:
            SF_dict["SF_velocity_" + direction] = np.nanmean(
                (inputs["adv_e_" + direction + "_shift"] - adv_e)
                * (inputs["u_" + direction + "_shift"] - u)
                + (inputs["adv_n_" + direction + "_shift"] - adv_n)
                * (inputs["v_" + direction + "_shift"] - v)
            )

        if scalar is not None:
            SF_dict["SF_scalar_" + direction] = np.nanmean(
                (inputs["adv_scalar_" + direction + "_shift"] - adv_scalar)
                * (inputs["scalar_" + direction + "_shift"] - scalar)
            )

    return SF_dict
