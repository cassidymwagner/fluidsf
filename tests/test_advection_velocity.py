from unittest import TestCase

import numpy as np
import pytest

from oceans_sf.advection_velocity import advection_velocity


@pytest.mark.parametrize(
    "u, v, x, y, dx, dy, boundary, even, grid_type, nbins, expected_result",
    [
        # Test case 1
        (
            np.array([[1, 2, 3], [4, 5, 6]]),
            np.array([[7, 8, 9], [10, 11, 12]]),
            np.array([0, 1, 2]),
            np.array([0, 1, 2]),
            1.0,
            1.0,
            "Periodic",
            True,
            "uniform",
            10,
            {
                "SF_zonal": np.array([0.0, 0.0]),
                "SF_meridional": np.array([0.0, 0.0]),
                "x-diffs": np.array([0.0, 1.0]),
                "y-diffs": np.array([0.0, 1.0]),
            },
        ),
        # # Test case 2
        # (
        #     np.array([[1, 2, 3], [4, 5, 6]]),
        #     np.array([[7, 8, 9], [10, 11, 12]]),
        #     np.array([0, 1, 2]),
        #     np.array([0, 1, 2]),
        #     1.0,
        #     1.0,
        #     "Non-Periodic",
        #     False,
        #     "uniform",
        #     10,
        #     {
        #         "SF_zonal": np.array([0.0, 0.0]),
        #         "SF_meridional": np.array([0.0, 0.0]),
        #         "x-diffs": np.array([0.0, 1.0]),
        #         "y-diffs": np.array([0.0, 1.0]),
        #     },
        # ),
        # Add more test cases here...
    ],
)
def test_advection_velocity(
    u, v, x, y, dx, dy, boundary, even, grid_type, nbins, expected_result
):
    result = advection_velocity(u, v, x, y, dx, dy, boundary, even, grid_type, nbins)
    TestCase().assertDictEqual(expected_result, result)
