import numpy as np
import pytest

from fluidsf.shift_array1d import shift_array1d


@pytest.mark.parametrize(
    "input_array, shift_by, boundary, expected_output",
    [
        (np.array([1, 2, 3, 4, 5]), 1, "Periodic", np.array([5, 1, 2, 3, 4])),
        (np.array([1, 2, 3, 4, 5]), 1, "Padded", np.array([np.nan, 1, 2, 3, 4])),
        (
            np.array([1, 2, 3, 4, 5]),
            10,
            "Padded",
            np.array([np.nan, np.nan, np.nan, np.nan, np.nan]),
        ),
        (np.array([1, 2, 3, 4, 5]), -1, "Periodic", np.array([2, 3, 4, 5, 1])),
        (np.array([]), 1, "Periodic", np.array([])),
        (np.array([1]), 1, "Periodic", np.array([1])),
        (np.array([1, 2, 3, 4, 5]), 3, "Periodic", np.array([3, 4, 5, 1, 2])),
    ],
)
def test_shift_array1d(input_array, shift_by, boundary, expected_output):
    """Test that shift_array1d works correctly for multiple cases."""
    shifted_array = shift_array1d(input_array, shift_by, boundary)
    np.testing.assert_array_equal(shifted_array, expected_output)
