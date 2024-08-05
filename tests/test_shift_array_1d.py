import numpy as np
import pytest
from fluidsf.shift_array_1d import shift_array_1d


@pytest.mark.parametrize(
    "input_array, shift_by, boundary, expected_output",
    [
        (np.array([1, 2, 3, 4, 5]), 1, "Periodic", np.array([2, 3, 4, 5, 1])),
        (np.array([1, 2, 3, 4, 5]), 1, None, np.array([2, 3, 4, 5, np.nan])),
        (
            np.array([1, 2, 3, 4, 5]),
            10,
            None,
            np.array([np.nan, np.nan, np.nan, np.nan, np.nan]),
        ),
        (
            np.array([1, 2, 3, 4, 5]),
            -1,
            None,
            np.array([5, np.nan, np.nan, np.nan, np.nan]),
        ),
        (np.array([]), 1, "Periodic", np.array([])),
        (np.array([1]), 1, "Periodic", np.array([1])),
        (np.array([1, 2, 3, 4, 5]), 3, "Periodic", np.array([4, 5, 1, 2, 3])),
    ],
)
def test_shift_array_1d(input_array, shift_by, boundary, expected_output):
    """Test that shift_array1d works correctly for multiple cases."""
    shifted_array = shift_array_1d(input_array, shift_by, boundary)
    np.testing.assert_array_equal(shifted_array, expected_output)
