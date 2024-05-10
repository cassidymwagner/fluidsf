import numpy as np

from .xy_shift_array import xy_shift_array


def calculate_2D_SF_maps(  # noqa: D417, C901
    u,
    v,
    adv_x,
    adv_y,
    shift_in_x,
    shift_in_y,
):
    """
    Calculate structure function, either advective or traditional.
    Supports velocity-based structure functions and scalar-based structure functions.

    Parameters
    ----------
        u: ndarray
            Array of u velocities.
        v: ndarray
            Array of v velocities.
        adv_e: ndarray
            Array of eastward advection values.
        adv_n: ndarray
            Array of northward advection values.
        down: int
            Shift amount for downward shift. For periodic data should be less than half
            the column length and less than the column length for other boundary
            conditions.
        right: int
            Shift amount for rightward shift. For periodic data should be less than
            half the row length and less than the row length for other boundary
            conditions.
        skip_velocity_sf: bool, optional
            Whether to skip velocity-based structure function calculation.
            Defaults to False.
        scalar: ndarray, optional
            Array of scalar values. Defaults to None.
        adv_scalar: ndarray, optional
            Array of scalar advection values. Defaults to None.
        traditional_type: list, optional
            List of traditional structure function types to calculate.
            Accepted types are: "LL", "LLL", "LTT", "LSS". If None,
            no traditional structure functions are calculated. Defaults to None.
        boundary: str, optional
            Boundary condition for shifting arrays. Accepted strings
            are "periodic-x", "periodic-y", and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        dict:
            A dictionary containing the advection velocity structure functions and
            scalar structure functions (if applicable).
            The dictionary has the following keys:
                'SF_velocity_right': The advection velocity structure function in the
                right direction.
                'SF_velocity_down': The advection velocity structure function in the
                down direction.
                'SF_trad_velocity_right': The traditional velocity structure function in
                the right direction (if traditional_order > 0).
                'SF_trad_velocity_down': The traditional velocity structure function in
                the down direction (if traditional_order > 0).
                'SF_scalar_right': The scalar structure function in the right direction
                (if scalar is provided).
                'SF_scalar_down': The scalar structure function in the down direction
                (if scalar is provided).
                'SF_trad_scalar_right': The traditional scalar structure function in the
                right direction (if scalar is provided and traditional_order > 0).
                'SF_trad_scalar_down': The traditional scalar structure function in the
                down direction (if scalar is provided and traditional_order > 0).
    """
    inputs = {
        "u": u,
        "v": v,
        "adv_x": adv_x,
        "adv_y": adv_y,
    }

    shifted_inputs = {}

    for key, value in inputs.items():
        if value is not None:
            xy_shift = xy_shift_array(
                inputs[key], x_shift=shift_in_x, y_shift=shift_in_y
            )

            shifted_inputs.update(
                {
                    key + "_xy_shift": xy_shift,
                }
            )

    inputs.update(shifted_inputs)
    SF_dict = {}

    SF_dict["SF_velocity_advection_xy"] = np.nanmean(
        (inputs["adv_x_xy_shift"] - adv_x)
        * (inputs["u_xy_shift"] - u)
        + (inputs["adv_y_xy_shift"] - adv_y)
        * (inputs["v_xy_shift"] - v)
    )

    return SF_dict
