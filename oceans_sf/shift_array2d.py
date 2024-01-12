import numpy as np


def shift_array2d(input_array, shift_right=1, shift_down=1, boundary="Periodic"):
    """
    Shifts 2D array right and down by the specified integer amounts and returns
    the shifted arrays. Either wraps the array or shifts and pads with NaNs.

    Args:
    ----
        input_array (array_like): 2-dimensional array to be shifted.
        shift_right (int, optional): Shift amount for rightward shift. For periodic data
        should be less than half the row length and less than the row length for
        other boundary conditions. Defaults to 1.
        shift_down (int, optional): Shift amount for downward shift. For periodic data
        should be less than half the column length and less than the column length for
        other boundary conditions. Defaults to 1.
        boundary (str, optional): Boundary condition for input array.
        Periodic boundary conditions will wrap the array, otherwise the array will be
        padded with NaNs. Defaults to "Periodic".

    Returns:
    -------
        shifted_right_array: 2D array shifted to the right by the specified integer
        amount
        shifted_down_array: 2D array shifted down by the specified integer amount
    """
    shifted_right_array = np.full(np.shape(input_array), np.nan)
    shifted_down_array = np.full(np.shape(input_array), np.nan)

    if boundary == "Periodic":
        shifted_right_array[:, :shift_right] = input_array[:, -shift_right:]
        shifted_right_array[:, shift_right:] = input_array[:, :-shift_right]

        shifted_down_array[:shift_down, :] = input_array[-shift_down:, :]
        shifted_down_array[shift_down:, :] = input_array[:-shift_down, :]
    else:
        shifted_right_array[:, shift_right:] = input_array[:, :-shift_right]
        shifted_down_array[shift_down:, :] = input_array[:-shift_down, :]

    return shifted_right_array, shifted_down_array
