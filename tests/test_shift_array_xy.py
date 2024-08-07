import numpy as np
import pytest
from fluidsf.shift_array_xy import shift_array_xy


@pytest.mark.parametrize(
    "input_array, x_shift, y_shift, expected_shifted_array",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # input_array
            1,  # x_shift
            1,  # y_shift
            np.array([[5, 6, 4], [8, 9, 7], [2, 3, 1]]),  # expected_shifted_array
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # input_array
            2,  # x_shift
            2,  # y_shift
            np.array([[9, 7, 8], [3, 1, 2], [6, 4, 5]]),  # expected_shifted_array
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # input_array
            1,  # x_shift
            2,  # y_shift
            np.array([[8, 9, 7], [2, 3, 1], [5, 6, 4]]),  # expected_shifted_array
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # input_array
            0,  # x_shift
            0,  # y_shift
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # expected_shifted_array
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # input_array
            0,  # x_shift
            1,  # y_shift
            np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]]),  # expected_shifted_array
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # input_array
            1,  # x_shift
            0,  # y_shift
            np.array([[2, 3, 1], [5, 6, 4], [8, 9, 7]]),  # expected_shifted_array
        ),
    ],
)
def test_shift_array_xy(input_array, x_shift, y_shift, expected_shifted_array):
    shifted_array = shift_array_xy(input_array, x_shift, y_shift)

    np.testing.assert_array_equal(shifted_array, expected_shifted_array)
