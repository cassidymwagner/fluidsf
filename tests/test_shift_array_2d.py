import numpy as np
import pytest

from oceans_sf.shift_array_2d import shift_array_2d


@pytest.mark.parametrize(
    "input_array, shift_left, shift_down, boundary, expected_shifted_left_array, \
        expected_shifted_down_array",
    [
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            1,
            1,
            None,
            np.array([[np.nan, 1, 2], [np.nan, 4, 5], [np.nan, 7, 8]]),
            np.array([[np.nan, np.nan, np.nan], [1, 2, 3], [4, 5, 6]]),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            2,
            2,
            None,
            np.array([[np.nan, np.nan, 1], [np.nan, np.nan, 4], [np.nan, np.nan, 7]]),
            np.array([[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [1, 2, 3]]),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            1,
            2,
            None,
            np.array([[np.nan, 1, 2], [np.nan, 4, 5], [np.nan, 7, 8]]),
            np.array([[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [1, 2, 3]]),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            1,
            1,
            "periodic-all",
            np.array([[3, 1, 2], [6, 4, 5], [9, 7, 8]]),
            np.array([[7, 8, 9], [1, 2, 3], [4, 5, 6]]),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            2,
            2,
            "periodic-all",
            np.array([[2, 3, 1], [5, 6, 4], [8, 9, 7]]),
            np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]]),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            1,
            2,
            "periodic-all",
            np.array([[3, 1, 2], [6, 4, 5], [9, 7, 8]]),
            np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]]),
        ),
    ],
)
def test_shift_array_2d(
    input_array,
    shift_left,
    shift_down,
    boundary,
    expected_shifted_left_array,
    expected_shifted_down_array,
):
    shifted_left_array, shifted_down_array = shift_array_2d(
        input_array, shift_left, shift_down, boundary
    )

    np.testing.assert_allclose(shifted_left_array, expected_shifted_left_array)
    np.testing.assert_allclose(shifted_down_array, expected_shifted_down_array)
