import numpy as np


def xy_shift_array(  # noqa: D417
    input_array, x_shift=0, y_shift=0
):
    """
    Wraps 2D array right and down by the specified integer amounts and returns
    the shifted arrays. Only works with 2D, doubly-periodic data on an even grid.

    Parameters
    ----------
        input_array: array_like
            2-dimensional array to be shifted.
        shift_right: int, optional
            Shift amount for rightward shift. For periodic data should be less than
            half the row length and less than the row length for other boundary
            conditions. Defaults to 0.
        shift_down: int, optional
            Shift amount for downward shift. For periodic data should be less than
            half the column length and less than the column length for other boundary
            conditions. Defaults to 0.
        boundary: str, optional
            Boundary condition for input array. Periodic boundary conditions will wrap
            the array, otherwise the array will be padded with NaNs. Accepted strings
            are "periodic-x", "periodic-y", and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        xy_shifted_array
            2D array shifted in the x-y directions by the specified integer amount
    """
    xy_shifted_array = np.full(np.shape(input_array), np.nan)

    if x_shift==0 and y_shift==0:
        xy_shifted_array = input_array
    elif x_shift==0:
        xy_shifted_array[:, :y_shift] = input_array[:, -y_shift:]
        xy_shifted_array[:, y_shift:] = input_array[:, :-y_shift]
    elif y_shift==0:
        xy_shifted_array[:x_shift, :] = input_array[-x_shift:, :]
        xy_shifted_array[:x_shift, :] = input_array[-x_shift:, :]
    else:
        xy_shifted_array[:x_shift, :y_shift] = input_array[-x_shift:, -y_shift:]
        xy_shifted_array[:x_shift, y_shift:] = input_array[-x_shift:, :-y_shift]
        xy_shifted_array[x_shift:, :y_shift] = input_array[:-x_shift, -y_shift:]
        xy_shifted_array[x_shift:, y_shift:] = input_array[:-x_shift, :-y_shift]

    return xy_shifted_array
