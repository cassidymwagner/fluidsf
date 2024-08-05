import numpy as np
import pytest
from fluidsf.calculate_separation_distances import calculate_separation_distances
from geopy.distance import great_circle


@pytest.mark.parametrize(
    "x, y, x_shift, y_shift, grid_type, expected_distances",
    [
        (0, 0, 1, 1, None, (1, 1)),
        (
            0,
            0,
            1,
            1,
            "latlon",
            (great_circle((1, 0), (0, 0)).meters, great_circle((0, 1), (0, 0)).meters),
        ),
        (0, 0, 0, 0, None, (0, 0)),
        (1, 2, 3, 4, None, (2, 2)),
        (
            1,
            2,
            3,
            4,
            "latlon",
            (great_circle((3, 2), (1, 2)).meters, great_circle((1, 4), (1, 2)).meters),
        ),
        (1, 2, 1, 2, None, (0, 0)),
        (1, 2, 1, 2, "latlon", (0, 0)),
        (1, 1, 0, 0, None, (-1, -1)),
        (
            1,
            1,
            0,
            0,
            "latlon",
            (great_circle((0, 1), (1, 1)).meters, great_circle((1, 0), (1, 1)).meters),
        ),
    ],
)
def test_calculate_separation_distances_parameterized(
    x, y, x_shift, y_shift, grid_type, expected_distances
):
    """Test that calculate_separation_distances works correctly for multiple cases."""
    output_distances = calculate_separation_distances(x, y, x_shift, y_shift, grid_type)
    np.testing.assert_allclose(output_distances, expected_distances)
