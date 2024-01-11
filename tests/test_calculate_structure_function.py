from unittest import TestCase

import numpy as np
import pytest

from oceans_sf.calculate_structure_function import calculate_structure_function


@pytest.mark.parametrize(
    "u, v, adv_e, adv_n, down, right, skip_velocity_sf, scalar, "
    "adv_scalar, traditional_order, boundary, expected_result",
    [
        # Test 1: velocity and scalar no traditional
        (
            np.array([[1, 2], [3, 4]]),  # u
            np.array([[1, -2], [-3, 4]]),  # v
            np.array([[3, -2], [-3, 12]]),  # adv_e
            np.array([[-7, -18], [33, 52]]),  # adv_n
            1,  # down
            1,  # right
            False,  # skip_velocity_sf
            np.array([[1, 2], [3, 4]]),  # scalar
            np.array([[3, -2], [-3, 12]]),  # adv_scalar
            0,  # traditional_order
            "Periodic",  # boundary
            {
                "SF_velocity_right": 88,
                "SF_velocity_down": 138,
                "SF_scalar_right": 5,
                "SF_scalar_down": 8,
            },
            # expected_result
        ),
        # Test 2: all
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
        # Test 3: all but skip velocity and no traditional
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
        # Test 4: velocities with no scalar or traditional
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
        # Test 5: velocity and scalar no traditional non-periodic
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
            None,
            {
                "SF_velocity_right": 88,
                "SF_velocity_down": 138,
                "SF_scalar_right": 5,
                "SF_scalar_down": 8,
            },
        ),
        # Test 6: all non-periodic
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
            None,
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
        # Test 7: all but skip velocity and no traditional non-periodic
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
            None,
            {
                "SF_scalar_right": 5,
                "SF_scalar_down": 8,
            },
        ),
        # Test 8: velocities with no scalar or traditional non-periodic
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
            None,
            {
                "SF_velocity_right": 88,
                "SF_velocity_down": 138,
            },
        ),
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
