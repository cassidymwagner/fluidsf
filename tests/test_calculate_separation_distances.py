import numpy as np
import pytest
from geopy.distance import great_circle

from oceans_sf.calculate_separation_distances import calculate_separation_distances


@pytest.mark.parametrize(
    "x, y, x_shift, y_shift, grid_type, expected_distances",
    [
        (0, 0, 1, 1, "uniform", (1, 1)),
        (
            0,
            0,
            1,
            1,
            "latlon",
            (great_circle((1, 0), (0, 0)).meters, great_circle((0, 1), (0, 0)).meters),
        ),
        (0, 0, 0, 0, "uniform", (0, 0)),
        (1, 2, 3, 4, "uniform", (2, 2)),
        (
            1,
            2,
            3,
            4,
            "latlon",
            (great_circle((3, 2), (1, 2)).meters, great_circle((1, 4), (1, 2)).meters),
        ),
    ],
)
def test_calculate_separation_distances_parameterized(
    x, y, x_shift, y_shift, grid_type, expected_distances
):
    """Test that calculate_separation_distances works correctly for multiple cases."""
    output_distances = calculate_separation_distances(x, y, x_shift, y_shift, grid_type)
    np.testing.assert_allclose(output_distances, expected_distances)
