import numpy as np


def shift_array_2d(  # noqa: D417
    input_array, shift_x=1, shift_y=1, boundary="periodic-all"
):
    """
    Shifts 2D array in x and y by the specified integer amounts and returns
    the shifted arrays. Either wraps the array or shifts and pads with NaNs.

    Parameters
    ----------
        input_array: array_like
            2-dimensional array to be shifted.
        shift_x: int, optional
            Shift amount in x direction. For periodic data should be less than
            half the row length and less than the row length for other boundary
            conditions. Defaults to 1.
        shift_y: int, optional
            Shift amount in y direction. For periodic data should be less than
            half the column length and less than the column length for other boundary
            conditions. Defaults to 1.
        boundary: str, optional
            Boundary condition for input array. Periodic boundary conditions will wrap
            the array, otherwise the array will be padded with NaNs. Accepted strings
            are "periodic-x", "periodic-y", and "periodic-all".
            Defaults to "periodic-all".

    Returns
    -------
        shifted_x_array
            2D array shifted in x by the specified integer amount
        shifted_y_array
            2D array shifted in y by the specified integer amount
    """
    shifted_x_array = np.full(np.shape(input_array), np.nan)
    shifted_y_array = np.full(np.shape(input_array), np.nan)

    if boundary == "periodic-all":
        shifted_x_array[:, :-shift_x] = input_array[:, shift_x:]
        shifted_x_array[:, -shift_x:] = input_array[:, :shift_x]

        shifted_y_array[:-shift_y, :] = input_array[shift_y:, :]
        shifted_y_array[-shift_y:, :] = input_array[:shift_y, :]

    elif boundary == "periodic-x":
        shifted_x_array[:, :-shift_x] = input_array[:, shift_x:]
        shifted_x_array[:, -shift_x:] = input_array[:, :shift_x]

        shifted_y_array[:-shift_y, :] = input_array[shift_y:, :]

    elif boundary == "periodic-y":
        shifted_x_array[:, :-shift_x] = input_array[:, shift_x:]

        shifted_y_array[:-shift_y, :] = input_array[shift_y:, :]
        shifted_y_array[-shift_y:, :] = input_array[:shift_y, :]

    elif boundary is None:
        shifted_x_array[:, :-shift_x] = input_array[:, shift_x:]
        shifted_y_array[:-shift_y, :] = input_array[shift_y:, :]

    return shifted_x_array, shifted_y_array
