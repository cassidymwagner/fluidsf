import numpy as np

from .shift_array1d import shift_array1d


def calculate_structure_function_1d(  # noqa: D417
    u,
    v,
    sep_id,
    scalar=None,
    traditional_type=["LLL"],  # noqa: B006
    boundary="Periodic",
):
    """
    Calculate traditional structure functions for 1D data.
    Supports velocity-based structure functions and scalar-based structure functions.
    Defaults to calculating the third-order longitudinal velocity structure function
    ('LLL') along the data track.

    Parameters
    ----------
        u: ndarray
            Array of u velocities.
        v: ndarray
            Array of v velocities.
        sep_id: ndarray
            Array of separation distances.
        scalar: ndarray, optional
            Array of scalar values. Defaults to None.
        traditional_type: list, optional
            List of traditional structure function types to calculate.
            Accepted types are: "LL", "LLL", "LTT", "LSS". Defaults to "LLL". If you
            include "LSS", you must provide a 1D array for scalar.
        boundary: str, optional
            Boundary condition for shifting arrays. Defaults to "Periodic". Set to None
            if no boundary conditions.

    Returns
    -------
        dict:
            A dictionary containing the velocity structure functions and
            scalar structure functions (if applicable).
            The dictionary has the following keys:
                'SF_LL': The second-order longitudinal velocity structure function.
                'SF_LLL': The third-order longitudinal velocity structure function.
                'SF_LTT': The longitudinal-transverse velocity structure function.
                'SF_LSS': The longitudinal-scalar structure function.
    """
    inputs = {"u": u, "v": v, "scalar": scalar}

    shifted_inputs = {}

    for key, value in inputs.items():
        if value is not None:
            shift = shift_array1d(inputs[key], shift_by=sep_id, boundary=boundary)
            shifted_inputs.update({key + "_shift": shift})

    inputs.update(shifted_inputs)
    SF_dict = {}

    if "LL" in traditional_type:
        SF_dict["SF_LL"] = np.nanmean((inputs["u_shift"] - u) ** 2)
    if "LLL" in traditional_type:
        SF_dict["SF_LLL"] = np.nanmean((inputs["u_shift"] - u) ** 3)
    if "LTT" in traditional_type:
        SF_dict["SF_LTT"] = np.nanmean(
            (inputs["u_shift"] - u) * (inputs["v_shift"] - v) ** 2
        )
    if "LSS" in traditional_type and scalar is not None:
        SF_dict["SF_LSS"] = np.nanmean(
            (inputs["u_shift"] - u) * (inputs["scalar_shift"] - scalar) ** 2
        )

    return SF_dict
