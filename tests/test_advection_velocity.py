from unittest import TestCase

import numpy as np
import pytest

from oceans_sf.advection_velocity import advection_velocity


@pytest.mark.parametrize(
    "u, v, x, y, dx, dy, boundary, even, grid_type, nbins, expected_result",
    [
        # Test case 1
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.linspace(0, 1, 2),
        #     np.linspace(0, 1, 2),
        #     None,
        #     None,
        #     "Periodic",
        #     True,
        #     "uniform",
        #     10,
        #     {
        #         "SF_zonal": np.array([0.0, 0.0]),
        #         "SF_meridional": np.array([0.0, 0.0]),
        #         "x-diffs": np.array([0.0, 1.0]),
        #         "y-diffs": np.array([0.0, 1.0]),
        #     },
        # ),
        # Test case 2
        (
            np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
            np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]),
            np.array([0, 1, 2, 3, 4]),
            np.array([0, 1, 2, 3, 4]),
            None,
            None,
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
        # Add more test cases here...
    ],
)
def test_advection_velocity(
    u, v, x, y, dx, dy, boundary, even, grid_type, nbins, expected_result
):
    result = advection_velocity(u, v, x, y, dx, dy, boundary, even, grid_type, nbins)
    # np.testing.assert_allclose(result["SF_zonal"], expected_result["SF_zonal"])
    # np.testing.assert_allclose(
    #     result["SF_meridional"], expected_result["SF_meridional"]
    # )
    np.testing.assert_allclose(result["x-diffs"], expected_result["x-diffs"])
    # np.testing.assert_allclose(result["y-diffs"], expected_result["y-diffs"])
