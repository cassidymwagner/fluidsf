import numpy as np


def shift_array_3d(  # noqa: D417
    input_array, shift_x=1, shift_y=1, shift_z=1, boundary=None
):
    """
    Shifts 3D array in x/y/z by the specified integer amounts and returns
    the shifted arrays. Either wraps the array or shifts and pads with NaNs.

    Parameters
    ----------
        input_array: array_like
            3-dimensional array to be shifted.
        shift_x: int, optional
            Shift amount in x direction. For periodic data should be less than
            half the row length and less than the row length for other boundary
            conditions. Defaults to 1.
        shift_y: int, optional
            Shift amount in y direction. For periodic data should be less than
            half the column length and less than the column length for other boundary
            conditions. Defaults to 1.
        shift_z: int, optional
            Shift amount in z direction. For periodic data should be less than
            half the depth length and less than the depth length for other boundary
            conditions. Defaults to 1.
        boundary: list, optional
            List of boundary conditions for input array. Periodic boundary conditions
            will wrap the array, otherwise the array will be padded with NaNs. Accepted
            strings are "periodic-x", "periodic-y", "periodic-z", and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        shifted_x_array
            3D array shifted in x by the specified integer amount
        shiftedy_array
            3D array shifted in y by the specified integer amount
        shifted_z_array
            3D array shifted in z by the specified integer amount
    """
    shifted_x_array = np.full(np.shape(input_array), np.nan)
    shifted_y_array = np.full(np.shape(input_array), np.nan)
    shifted_z_array = np.full(np.shape(input_array), np.nan)

    shifted_x_array[:, :, :-shift_x] = input_array[:, :, shift_x:]
    shifted_y_array[:, :-shift_y, :] = input_array[:, shift_y:, :]
    shifted_z_array[:-shift_z, :, :] = input_array[shift_z:, :, :]

    if boundary is not None:
        if "periodic-all" in boundary:
            shifted_x_array[:, :, -shift_x:] = input_array[:, :, :shift_x]
            shifted_y_array[:, -shift_y:, :] = input_array[:, :shift_y, :]
            shifted_z_array[-shift_z:, :, :] = input_array[:shift_z, :, :]

        if any("periodic-x" in b for b in boundary):
            shifted_x_array[:, :, -shift_x:] = input_array[:, :, :shift_x]

        if any("periodic-y" in b for b in boundary):
            shifted_y_array[:, -shift_y:, :] = input_array[:, :shift_y, :]

        if any("periodic-z" in b for b in boundary):
            shifted_z_array[-shift_z:, :, :] = input_array[:shift_z, :, :]

    return shifted_x_array, shifted_y_array, shifted_z_array
