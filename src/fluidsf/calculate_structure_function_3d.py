import numpy as np

from .shift_array_3d import shift_array_3d


def calculate_structure_function_3d(  # noqa: D417, C901
    u,
    v,
    w,
    adv_x,
    adv_y,
    adv_z,
    shift_x,
    shift_y,
    shift_z,
    sf_type,
    scalar=None,
    adv_scalar=None,
    boundary="periodic-all",
):
    """
    Calculate structure functions, including advective structure functions.
    Supports velocity-based structure functions and scalar-based structure functions.

    Parameters
    ----------
        u: ndarray
            Array of u velocities.
        v: ndarray
            Array of v velocities.
        w: ndarray
            Array of w velocities.
        adv_x: ndarray
            Array of x-dir advection values.
        adv_y: ndarray
            Array of y-dir advection values.
        adv_z: ndarray
            Array of z-dir advection values.
        shift_x: int
            Shift amount for x shift.
        shift_y: int
            Shift amount for y shift.
        shift_z: int
            Shift amount for z shift.
        sf_type: list
            List of structure function types to calculate.
            Accepted list entries must be one or more of the following strings:
            "ASF_V, "ASF_S", "LL", "TT", "SS", "LLL", "LTT", "LSS".
            Defaults to "ASF_V".
        scalar: ndarray, optional
            Array of scalar values. Defaults to None.
        adv_scalar: ndarray, optional
            Array of scalar advection values. Defaults to None.
        boundary: str, optional
            Boundary condition for shifting arrays. Accepted strings
            are "periodic-x", "periodic-y", "periodic-z" and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        dict:
            A dictionary containing the velocity-based advective structure functions and
            scalar structure functions (if applicable).
            The returned dictionary may contain the following keys, with some keys
            removed if the structure function is not calculated:

                **SF_velocity_x**: The advective velocity structure function in the
                x direction.

                **SF_velocity_y**: The advective velocity structure function in the
                y direction.

                **SF_velocity_z**: The advective velocity structure function in the
                z direction.

                **SF_scalar_x**: The advective scalar structure function in the x
                direction.

                **SF_scalar_y**: The advective scalar structure function in the y
                direction.

                **SF_scalar_z**: The advective scalar structure function in the z
                direction.

                **SF_LL_x**: The second-order longitudinal velocity structure function
                in the x direction.

                **SF_LL_y**: The second-order longitudinal velocity structure function
                in the y direction.

                **SF_LL_z**: The second-order longitudinal velocity structure function
                in the z direction.

                **SF_TT_x**: The second-order transverse velocity structure function
                in the x direction.

                **SF_TT_y**: The second-order transverse velocity structure function
                in the y direction.

                **SF_TT_z**: The second-order transverse velocity structure function
                in the z direction.

                **SF_SS_x**: The second-order scalar structure function in the x
                direction.

                **SF_SS_y**: The second-order scalar structure function in the y
                direction.

                **SF_SS_z**: The second-order scalar structure function in the z
                direction.

                **SF_LLL_x**: The third-order longitudinal velocity structure function
                in the x direction.

                **SF_LLL_y**: The third-order longitudinal velocity structure function
                in the y direction.

                **SF_LLL_z**: The third-order longitudinal velocity structure function
                in the z direction.

                **SF_LTT_x**: The third-order longitudinal-transverse-transverse
                velocity structure function in the x direction.

                **SF_LTT_y**: The third-order longitudinal-transverse-transverse
                velocity structure function in the y direction.

                **SF_LTT_z**: The third-order longitudinal-transverse-transverse
                velocity structure function in the z direction.

                **SF_LSS_x**: The third-order longitudinal-scalar-scalar structure
                function in the x direction.

                **SF_LSS_y**: The third-order longitudinal-scalar-scalar structure
                function in the y direction.

                **SF_LSS_z**: The third-order longitudinal-scalar-scalar structure
                function in the z direction.
    """
    inputs = {
        "u": u,
        "v": v,
        "w": w,
        "adv_x": adv_x,
        "adv_y": adv_y,
        "adv_z": adv_z,
        "scalar": scalar,
        "adv_scalar": adv_scalar,
    }

    shifted_inputs = {}

    for key, value in inputs.items():
        if value is not None:
            x_shift, y_shift, z_shift = shift_array_3d(
                inputs[key],
                shift_x=shift_x,
                shift_y=shift_y,
                shift_z=shift_z,
                boundary=boundary,
            )

            shifted_inputs.update(
                {
                    key + "_x_shift": x_shift,
                    key + "_y_shift": y_shift,
                    key + "_z_shift": z_shift,
                }
            )

    inputs.update(shifted_inputs)
    SF_dict = {}

    for direction in ["x", "y", "z"]:
        if any("ASF_V" in t for t in sf_type):
            SF_dict["SF_advection_velocity_" + direction] = np.nanmean(
                (inputs["adv_x_" + direction + "_shift"] - adv_x)
                * (inputs["u_" + direction + "_shift"] - u)
                + (inputs["adv_y_" + direction + "_shift"] - adv_y)
                * (inputs["v_" + direction + "_shift"] - v)
                + (inputs["adv_z_" + direction + "_shift"] - adv_z)
                * (inputs["w_" + direction + "_shift"] - w)
            )
        if any("ASF_S" in t for t in sf_type):
            SF_dict["SF_advection_scalar_" + direction] = np.nanmean(
                (inputs["adv_scalar_" + direction + "_shift"] - adv_scalar)
                * (inputs["scalar_" + direction + "_shift"] - scalar)
            )
        if any("SS" in t for t in sf_type):
            SF_dict["SF_SS_" + direction] = np.nanmean(
                (inputs["scalar_" + direction + "_shift"] - scalar) ** 2
            )

        if direction == "x":
            if any("LL" in t for t in sf_type):
                SF_dict["SF_LL_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u) ** 2
                )
            if any("TT" in t for t in sf_type):
                SF_dict["SF_TT_" + direction] = np.nanmean(
                    (inputs["v_" + direction + "_shift"] - v) ** 2
                    + (inputs["w_" + direction + "_shift"] - w) ** 2
                )
            if any("LLL" in t for t in sf_type):
                SF_dict["SF_LLL_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u) ** 3
                )
            if any("LTT" in t for t in sf_type):
                SF_dict["SF_LTT_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u)
                    * (
                        (inputs["v_" + direction + "_shift"] - v) ** 2
                        + (inputs["w_" + direction + "_shift"] - w) ** 2
                    )
                )
            if any("LSS" in t for t in sf_type):
                SF_dict["SF_LSS_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u)
                    * (inputs["scalar_" + direction + "_shift"] - scalar) ** 2
                )

        elif direction == "y":
            if any("LL" in t for t in sf_type):
                SF_dict["SF_LL_" + direction] = np.nanmean(
                    (inputs["v_" + direction + "_shift"] - v) ** 2
                )
            if any("TT" in t for t in sf_type):
                SF_dict["SF_TT_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u) ** 2
                    + (inputs["w_" + direction + "_shift"] - w) ** 2
                )
            if any("LLL" in t for t in sf_type):
                SF_dict["SF_LLL_" + direction] = np.nanmean(
                    (inputs["v_" + direction + "_shift"] - v) ** 3
                )
            if any("LTT" in t for t in sf_type):
                SF_dict["SF_LTT_" + direction] = np.nanmean(
                    (inputs["v_" + direction + "_shift"] - v)
                    * (
                        (inputs["u_" + direction + "_shift"] - u) ** 2
                        + (inputs["w_" + direction + "_shift"] - w) ** 2
                    )
                )
            if any("LSS" in t for t in sf_type):
                SF_dict["SF_LSS_" + direction] = np.nanmean(
                    (inputs["v_" + direction + "_shift"] - v)
                    * (inputs["scalar_" + direction + "_shift"] - scalar) ** 2
                )

        elif direction == "z":
            if any("LL" in t for t in sf_type):
                SF_dict["SF_LL_" + direction] = np.nanmean(
                    (inputs["w_" + direction + "_shift"] - w) ** 2
                )
            if any("TT" in t for t in sf_type):
                SF_dict["SF_TT_" + direction] = np.nanmean(
                    (inputs["u_" + direction + "_shift"] - u) ** 2
                    + (inputs["v_" + direction + "_shift"] - v) ** 2
                )
            if any("LLL" in t for t in sf_type):
                SF_dict["SF_LLL_" + direction] = np.nanmean(
                    (inputs["w_" + direction + "_shift"] - w) ** 3
                )
            if any("LTT" in t for t in sf_type):
                SF_dict["SF_LTT_" + direction] = np.nanmean(
                    (inputs["w_" + direction + "_shift"] - w)
                    * (
                        (inputs["u_" + direction + "_shift"] - u) ** 2
                        + (inputs["v_" + direction + "_shift"] - v) ** 2
                    )
                )
            if any("LSS" in t for t in sf_type):
                SF_dict["SF_LSS_" + direction] = np.nanmean(
                    (inputs["w_" + direction + "_shift"] - w)
                    * (inputs["scalar_" + direction + "_shift"] - scalar) ** 2
                )

    return SF_dict
