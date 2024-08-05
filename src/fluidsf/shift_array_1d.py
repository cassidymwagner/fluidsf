import numpy as np


def shift_array_1d(input_array, shift_by=1, boundary="Periodic"):  # noqa: D417
    """
    Shifts 1D array by an integer amount and returns the shifted array.
    Either wraps the array or shifts and pads with NaNs.

    Parameters
    ----------
        input_array: array_like
            1-dimensional array to be shifted.
        shift_by: int, optional
            Shift amount for array. For periodic data should be less than
            len(input_array)/2 and less than len(input_array) for other boundary
            conditions. Defaults to 1.
        boundary: str, optional
            Boundary condition for input array. Periodic boundary conditions will wrap
            the array, otherwise the array will be padded with NaNs.
            Defaults to "Periodic".

    Returns
    -------
        shifted_array:
            1D array shifted by requested integer amount
    """
    shifted_array = np.full(np.shape(input_array), np.nan)

    if boundary == "Periodic":
        shifted_array[:-shift_by] = input_array[shift_by:]
        shifted_array[-shift_by:] = input_array[:shift_by]

    else:
        shifted_array[:-shift_by] = input_array[shift_by:]

    return shifted_array
