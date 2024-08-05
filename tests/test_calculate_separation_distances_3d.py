import numpy as np
import pytest
from fluidsf.calculate_separation_distances_3d import (
    calculate_separation_distances_3d,
)


@pytest.mark.parametrize(
    "x, y, z, x_shift, y_shift, z_shift, expected_distances",
    [
        # Test case where all 3 points are the same
        (0, 0, 0, 0, 0, 0, (0, 0, 0)),
        # Test case where the points are shifted by 1 in each dimension but all equal.
        (0, 0, 0, 1, 1, 1, (1, 1, 1)),
        # Test case where the points are shifted by 3 in each dimension and different.
        (1, 2, 3, 4, 5, 6, (3, 3, 3)),
        # Test case where the points are shifted by different amounts.
        (1, 2, 3, 2, 4, 6, (1, 2, 3)),
    ],
)
def test_calculate_separation_distances_3d_parameterized(
    x, y, z, x_shift, y_shift, z_shift, expected_distances
):
    """Test that calculate_separation_distances works correctly for multiple cases."""
    output_distances = calculate_separation_distances_3d(
        x, y, z, x_shift, y_shift, z_shift
    )
    np.testing.assert_allclose(output_distances, expected_distances)
