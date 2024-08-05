import numpy as np


def shift_array_xy(input_array, x_shift=0, y_shift=0):  # noqa: D417
    """
    Wrap 2D array in x and y by the specified integer amounts and returns
    the shifted arrays. Only works with 2D, doubly-periodic data on an even grid.

    Parameters
    ----------
        input_array: array_like
            2-dimensional array to be shifted.
        shift_x: int, optional
            Shift amount for x shift.
        shift_y: int, optional
            Shift amount for y shift.

    Returns
    -------
        shifted_xy_array
            2D array shifted in the x-y directions by the specified integer amount
    """
    shifted_xy_array = np.full(np.shape(input_array), np.nan)

    if x_shift == 0 and y_shift == 0:
        shifted_xy_array = input_array
    elif y_shift == 0:
        shifted_xy_array[:, :-x_shift] = input_array[:, x_shift:]
        shifted_xy_array[:, -x_shift:] = input_array[:, :x_shift]
    elif x_shift == 0:
        shifted_xy_array[:-y_shift, :] = input_array[y_shift:, :]
        shifted_xy_array[-y_shift:, :] = input_array[:y_shift, :]
    else:
        shifted_xy_array[:-y_shift, :-x_shift] = input_array[y_shift:, x_shift:]
        shifted_xy_array[:-y_shift, -x_shift:] = input_array[y_shift:, :x_shift]
        shifted_xy_array[-y_shift:, :-x_shift] = input_array[:y_shift, x_shift:]
        shifted_xy_array[-y_shift:, -x_shift:] = input_array[:y_shift, :x_shift]

    return shifted_xy_array
