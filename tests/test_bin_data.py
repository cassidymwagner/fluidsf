import numpy as np
import pytest
from fluidsf.bin_data import bin_data


@pytest.mark.parametrize(
    "dd, sf, nbins, expected_result",
    [
        (
            np.array([1, 2, 3, 4, 5]),
            np.array([10, 20, 30, 40, 50]),
            5,
            (
                np.array([1, 2, 3, 4, 5]),
                np.array([10, 20, 30, 40, 50]),
            ),
        ),
        (
            np.array([1, 2, 3, 4, 5]),
            np.array([10, 20, 30, 40, 50]),
            1,
            (
                np.array([3]),
                np.array([30]),
            ),
        ),
        (
            np.array([1, 2, 3, 4, 5]),
            np.array([10, 20, 30, 40, 50]),
            3,
            (
                np.array([1.5, 3, 4.5]),
                np.array([15, 30, 45]),
            ),
        ),
        (
            np.linspace(1, 24, 24),
            np.linspace(2, 48, 24),
            8,
            (
                np.array([2, 5, 8, 11, 14, 17, 20, 23]),
                np.array([4, 10, 16, 22, 28, 34, 40, 46]),
            ),
        ),
        (
            np.linspace(1, 24, 24),
            np.linspace(2, 48, 24),
            3,
            (
                np.array([4.5, 12.5, 20.5]),
                np.array([9, 25, 41]),
            ),
        ),
        (
            np.linspace(0, 8, 9),
            np.array([0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]),
            3,
            (
                np.array([1, 4, 7]),
                np.array([175, 1750, 5215]),
            ),
        ),
    ],
)
def test_bin_data(dd, sf, nbins, expected_result):
    """Test the bin_data function."""
    result = bin_data(dd, sf, nbins)
    np.testing.assert_allclose(result, expected_result)
