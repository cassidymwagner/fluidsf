import numpy as np

from .shift_array_xy import shift_array_xy


def calculate_sf_maps_2d(  # noqa: D417, C901
    u,
    v,
    x,
    y,
    adv_x,
    adv_y,
    shift_in_x,
    shift_in_y,
    sf_type,
    scalar=None,
    adv_scalar=None,
):
    """
    Calculate structure functions, including advective structure functions.
    Supports velocity-based structure functions and scalar-based structure functions.
    Can only be used with periodic, evenly-spaced data.

    Parameters
    ----------
        u: ndarray
            Array of u velocities.
        v: ndarray
            Array of v velocities.
        x: ndarray
            1D array of x-coordinates.
        y: ndarray
            1D array of y-coordinates.
        adv_x: ndarray
            Array of x-dir advection values.
        adv_y: ndarray
            Array of y-dir advection values.
        shift_in_x: int
            Shift amount for x shift.
        shift_in_y: int
            Shift amount for y shift.
        sf_type: list
            List of structure function types to calculate.
            Accepted list entries must be one or more of the following strings:
            "ASF_V", "ASF_S", "LL", "TT", "SS", "LLL", "LTT", "LSS".
        scalar: ndarray, optional
            Array of scalar values. Defaults to None.
        adv_scalar: ndarray, optional
            Array of scalar advection values. Defaults to None.

    Returns
    -------
        dict:
            A dictionary containing the advection velocity structure functions and
            scalar structure functions (if applicable).
            The returned dictionary may contain the following keys, with some keys
            removed if the structure function is not calculated:

                **SF_advection_velocity_xy**: The advective velocity structure function
                for separation vectors in the x-y plane.

                **SF_advection_scalar_xy**: The advective scalar structure function
                for separation vectors in the x-y plane.

                **SF_LL_xy**: The second-order longitudinal velocity structure function for 
                separation vectors in the x-y plane.

                **SF_TT_xy**: The second-order transverse velocity structure function for 
                separation vectors in the x-y plane.

                **SF_SS_xy**: The second-order scalar structure function for 
                separation vectors in the x-y plane.

                **SF_LLL_xy**: The third-order longitudinal velocity structure function for 
                separation vectors in the x-y plane.

                **SF_LTT_xy**: The third-order longitudinal-transverse-transverse velocity 
                structure function for separation vectors in the x-y plane.

                **SF_LSS_xy**: The third-order longitudinal-scalar-scalar structure function 
                for separation vectors in the x-y plane.

    """
    inputs = {
        "u": u,
        "v": v,
        "adv_x": adv_x,
        "adv_y": adv_y,
        "scalar": scalar,
        "adv_scalar": adv_scalar,
    }

    shifted_inputs = {}

    for key, value in inputs.items():
        if value is not None:
            xy_shift = shift_array_xy(
                inputs[key], x_shift=shift_in_x, y_shift=shift_in_y
            )

            shifted_inputs.update(
                {
                    key + "_xy_shift": xy_shift,
                }
            )

    inputs.update(shifted_inputs)
    SF_dict = {}

    if any("ASF_V" in t for t in sf_type):
        SF_dict["SF_advection_velocity_xy"] = np.nanmean(
            (inputs["adv_x_xy_shift"] - adv_x) * (inputs["u_xy_shift"] - u)
            + (inputs["adv_y_xy_shift"] - adv_y) * (inputs["v_xy_shift"] - v)
        )

    if any("ASF_S" in t for t in sf_type):
        SF_dict["SF_advection_scalar_xy"] = np.nanmean(
            (inputs["adv_scalar_xy_shift"] - adv_scalar)
            * (inputs["scalar_xy_shift"] - scalar)
        )

    if any(t not in ["ASF_V", "ASF_S"] for t in sf_type):
        x_separation = shift_in_x * (x[1] - x[0])
        y_separation = shift_in_y * (y[1] - y[0])
        cosine_angle = x_separation / np.sqrt(x_separation**2 + y_separation**2)
        sine_angle = y_separation / np.sqrt(x_separation**2 + y_separation**2)

        if any("LL" in t for t in sf_type):
            SF_dict["SF_LL_xy"] = np.nanmean(
                (
                    (inputs["u_xy_shift"] - u) * cosine_angle
                    + (inputs["v_xy_shift"] - v) * sine_angle
                )
                ** 2
            )
        if any("TT" in t for t in sf_type):
            SF_dict["SF_TT_xy"] = np.nanmean(
                (
                    (inputs["v_xy_shift"] - v) * cosine_angle
                    - (inputs["u_xy_shift"] - u) * sine_angle
                )
                ** 2
            )
        if any("SS" in t for t in sf_type):
            SF_dict["SF_SS_xy"] = np.nanmean((inputs["scalar_xy_shift"] - scalar) ** 2)

        if any("LLL" in t for t in sf_type):
            SF_dict["SF_LLL_xy"] = np.nanmean(
                (
                    (inputs["u_xy_shift"] - u) * cosine_angle
                    + (inputs["v_xy_shift"] - v) * sine_angle
                )
                ** 3
            )
        if any("LTT" in t for t in sf_type):
            SF_dict["SF_LTT_xy"] = np.nanmean(
                (
                    (inputs["u_xy_shift"] - u) * cosine_angle
                    + (inputs["v_xy_shift"] - v) * sine_angle
                )
                * (
                    (inputs["v_xy_shift"] - v) * cosine_angle
                    - (inputs["u_xy_shift"] - u) * sine_angle
                )
                ** 2
            )

        if any("LSS" in t for t in sf_type):
            SF_dict["SF_LSS_xy"] = np.nanmean(
                (
                    (inputs["u_xy_shift"] - u) * cosine_angle
                    + (inputs["v_xy_shift"] - v) * sine_angle
                )
                * (inputs["scalar_xy_shift"] - scalar) ** 2
            )

    return SF_dict
