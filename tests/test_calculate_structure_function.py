from unittest import TestCase

import numpy as np
import pytest

from oceans_sf.calculate_structure_function import calculate_structure_function


@pytest.mark.parametrize(
    "u, v, adv_e, adv_n, down, right, skip_velocity_sf, scalar, "
    "adv_scalar, traditional_order, boundary, expected_result",
    [
        # Test velocity and scalar no traditional
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            np.array([[-7, -18], [33, 52]]),
            1,
            1,
            False,
            np.array([[1, 2], [3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            0,
            "Periodic",
            {
                "SF_velocity_right": 88,
                "SF_velocity_down": 138,
                "SF_scalar_right": 5,
                "SF_scalar_down": 8,
            },
        ),
        # Test all
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            np.array([[-7, -18], [33, 52]]),
            1,
            1,
            False,
            np.array([[1, 2], [3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            2,
            "Periodic",
            {
                "SF_velocity_right": 88,
                "SF_trad_velocity_right": 1,
                "SF_scalar_right": 5,
                "SF_trad_scalar_right": 1,
                "SF_velocity_down": 138,
                "SF_trad_velocity_down": 4,
                "SF_scalar_down": 8,
                "SF_trad_scalar_down": 4,
            },
        ),
        # Test all but skip velocity and no traditional
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            np.array([[-7, -18], [33, 52]]),
            1,
            1,
            True,
            np.array([[1, 2], [3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            0,
            "Periodic",
            {
                "SF_scalar_right": 5,
                "SF_scalar_down": 8,
            },
        ),
        # Test velocities with no scalar or traditional
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            np.array([[-7, -18], [33, 52]]),
            1,
            1,
            False,
            None,
            None,
            0,
            "Periodic",
            {
                "SF_velocity_right": 88,
                "SF_velocity_down": 138,
            },
        ),
        # # Test case 3
        # (
        #     np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        #     np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        #     np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        #     np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        #     2,
        #     2,
        #     False,
        #     np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        #     np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        #     1,
        #     "Periodic",
        #     {
        #         "SF_velocity_right": 0.0,
        #         "SF_velocity_down": 0.0,
        #         "SF_scalar_right": 0.0,
        #         "SF_scalar_down": 0.0,
        #     },
        # ),
    ],
)
def test_calculate_structure_function_parameterized(
    u,
    v,
    adv_e,
    adv_n,
    down,
    right,
    skip_velocity_sf,
    scalar,
    adv_scalar,
    traditional_order,
    boundary,
    expected_result,
):
    """Test that calculate_structure_function works correctly for multiple cases."""
    output_dict = calculate_structure_function(
        u,
        v,
        adv_e,
        adv_n,
        down,
        right,
        skip_velocity_sf,
        scalar,
        adv_scalar,
        traditional_order,
        boundary,
    )

    TestCase().assertDictEqual(output_dict, expected_result)
