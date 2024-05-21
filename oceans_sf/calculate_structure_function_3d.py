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
    skip_velocity_sf=False,
    scalar=None,
    adv_scalar=None,
    traditional_type=None,
    boundary="periodic-all",
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
            are "periodic-x", "periodic-y", "periodic-z" and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        dict:
            A dictionary containing the advection velocity structure functions and
            scalar structure functions (if applicable).
            The dictionary has the following keys:
                'SF_velocity_x': The advection velocity structure function in the
                x direction.
                'SF_velocity_y': The advection velocity structure function in the
                y direction.
                'SF_velocity_z': The advection velocity structure function in the
                z direction.
                'SF_scalar_x': The scalar structure function in the x direction.
                'SF_scalar_y': The scalar structure function in the y direction.
                'SF_scalar_z': The scalar structure function in the z direction.
                'SF_LL_x': The traditional structure function LL in the x direction.
                'SF_LL_y': The traditional structure function LL in the y direction.
                'SF_LL_z': The traditional structure function LL in the z direction.
                'SF_LLL_x': The traditional structure function LLL in the x direction.
                'SF_LLL_y': The traditional structure function LLL in the y direction.
                'SF_LLL_z': The traditional structure function LLL in the z direction.
                'SF_LTT_x': The traditional structure function LTT in the x direction.
                'SF_LTT_y': The traditional structure function LTT in the y direction.
                'SF_LTT_z': The traditional structure function LTT in the z direction.
                'SF_LSS_x': The traditional structure function LSS in the x direction.
                'SF_LSS_y': The traditional structure function LSS in the y direction.
                'SF_LSS_z': The traditional structure function LSS in the z direction.
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

    if skip_velocity_sf is True:
        inputs.update(
            {
                "u": None,
                "v": None,
                "w": None,
                "adv_x": None,
                "adv_y": None,
                "adv_z": None,
            }
        )

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
        if skip_velocity_sf is False:
            SF_dict["SF_velocity_" + direction] = np.nanmean(
                (inputs["adv_x_" + direction + "_shift"] - adv_x)
                * (inputs["u_" + direction + "_shift"] - u)
                + (inputs["adv_y_" + direction + "_shift"] - adv_y)
                * (inputs["v_" + direction + "_shift"] - v)
                + (inputs["adv_z_" + direction + "_shift"] - adv_z)
                * (inputs["w_" + direction + "_shift"] - w)
            )
            if traditional_type is not None:
                if any("LL" in t for t in traditional_type):
                    SF_dict["SF_LL_" + direction] = np.nanmean(
                        (inputs["u_" + direction + "_shift"] - u) ** 2
                    )
                if any("LLL" in t for t in traditional_type):
                    SF_dict["SF_LLL_" + direction] = np.nanmean(
                        (inputs["u_" + direction + "_shift"] - u) ** 3
                    )
                if any("LTT" in t for t in traditional_type):
                    if direction == "x":
                        SF_dict["SF_LTT_" + direction] = np.nanmean(
                            (inputs["u_" + direction + "_shift"] - u)
                            * (inputs["v_" + direction + "_shift"] - v) ** 2
                        )

                    if direction == "y":
                        SF_dict["SF_LTT_" + direction] = np.nanmean(
                            (inputs["v_" + direction + "_shift"] - v)
                            * (inputs["u_" + direction + "_shift"] - u) ** 2
                        )

                    if direction == "z":
                        SF_dict["SF_LTT_" + direction] = np.nanmean(
                            (inputs["w_" + direction + "_shift"] - w)
                            * (inputs["u_" + direction + "_shift"] - u) ** 2
                        )

        if scalar is not None:
            SF_dict["SF_scalar_" + direction] = np.nanmean(
                (inputs["adv_scalar_" + direction + "_shift"] - adv_scalar)
                * (inputs["scalar_" + direction + "_shift"] - scalar)
            )
            if traditional_type is not None:
                if any("LSS" in t for t in traditional_type):
                    SF_dict["SF_LSS_" + direction] = np.nanmean(
                        (inputs["u_" + direction + "_shift"] - u)
                        * (inputs["scalar_" + direction + "_shift"] - scalar) ** 2
                    )
    return SF_dict
