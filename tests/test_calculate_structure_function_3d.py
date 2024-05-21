from unittest import TestCase

import numpy as np
import pytest

from oceans_sf.calculate_structure_function_3d import calculate_structure_function_3d


@pytest.mark.parametrize(
    "u, v, w, adv_x, adv_y, adv_z, shift_x, shift_y, shift_z, skip_velocity_sf, scalar,"
    "adv_scalar, traditional_type, boundary, expected_result",
    [
        # Test 1: all with zero values
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.zeros((3, 3, 3)),  # adv_x
            np.zeros((3, 3, 3)),  # adv_y
            np.zeros((3, 3, 3)),  # adv_z
            1,  # shift_x
            1,  # shift_y
            1,  # shift_z
            False,  # skip_velocity_sf
            np.zeros((3, 3, 3)),  # scalar
            np.zeros((3, 3, 3)),  # adv_scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            "periodic-all",  # boundary
            {
                "SF_velocity_x": 0,
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LTT_x": 0,
                "SF_scalar_x": 0,
                "SF_LSS_x": 0,
                "SF_velocity_y": 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
                "SF_LTT_y": 0,
                "SF_scalar_y": 0,
                "SF_LSS_y": 0,
                "SF_velocity_z": 0,
                "SF_LL_z": 0,
                "SF_LLL_z": 0,
                "SF_LTT_z": 0,
                "SF_scalar_z": 0,
                "SF_LSS_z": 0,
            },
        ),
        # Test 2: ones-array velocity and scalar with all traditional
        (
            np.ones((3, 3, 3)),  # u
            np.ones((3, 3, 3)),  # v
            np.ones((3, 3, 3)),  # w
            np.ones((3, 3, 3)),  # adv_x
            np.ones((3, 3, 3)),  # adv_y
            np.ones((3, 3, 3)),  # adv_z
            1,  # shift_x
            1,  # shift_y
            1,  # shift_z
            False,  # skip_velocity_sf
            np.ones((3, 3, 3)),  # scalar
            np.ones((3, 3, 3)),  # adv_scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            "periodic-all",  # boundary
            {
                "SF_velocity_x": 0,
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LTT_x": 0,
                "SF_scalar_x": 0,
                "SF_LSS_x": 0,
                "SF_velocity_y": 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
                "SF_LTT_y": 0,
                "SF_scalar_y": 0,
                "SF_LSS_y": 0,
                "SF_velocity_z": 0,
                "SF_LL_z": 0,
                "SF_LLL_z": 0,
                "SF_LTT_z": 0,
                "SF_scalar_z": 0,
                "SF_LSS_z": 0,
            },
        ),
        # Test 3: all with non-zero values
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.arange(1, 28).reshape((3, 3, 3)),  # v
            np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.arange(1, 28).reshape((3, 3, 3)),  # adv_x
            np.arange(1, 28).reshape((3, 3, 3)),  # adv_y
            np.arange(1, 28).reshape((3, 3, 3)),  # adv_z
            1,  # shift_x
            1,  # shift_y
            1,  # shift_z
            False,  # skip_velocity_sf
            np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            np.arange(1, 28).reshape((3, 3, 3)),  # adv_scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # boundary
            {
                "SF_velocity_x": 12,
                "SF_LL_x": 4,
                "SF_LLL_x": 8,
                "SF_LTT_x": 8,
                "SF_scalar_x": 4,
                "SF_LSS_x": 8,
                "SF_velocity_y": 108,
                "SF_LL_y": 36,
                "SF_LLL_y": 216,
                "SF_LTT_y": 216,
                "SF_scalar_y": 36,
                "SF_LSS_y": 216,
                "SF_velocity_z": 972,
                "SF_LL_z": 324,
                "SF_LLL_z": 5832,
                "SF_LTT_z": 5832,
                "SF_scalar_z": 324,
                "SF_LSS_z": 5832,
            },
        ),
        # Test 4: velocities and advection with different values
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            2 * np.arange(1, 28).reshape((3, 3, 3)),  # v
            3 * np.arange(1, 28).reshape((3, 3, 3)),  # w
            4 * np.arange(1, 28).reshape((3, 3, 3)),  # adv_x
            5 * np.arange(1, 28).reshape((3, 3, 3)),  # adv_y
            6 * np.arange(1, 28).reshape((3, 3, 3)),  # adv_z
            1,  # shift_x
            1,  # shift_y
            1,  # shift_z
            False,  # skip_velocity_sf
            7 * np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            8 * np.arange(1, 28).reshape((3, 3, 3)),  # adv_scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # boundary
            {
                "SF_velocity_x": 128,
                "SF_LL_x": 4,
                "SF_LLL_x": 8,
                "SF_LTT_x": 32,
                "SF_scalar_x": 224,
                "SF_LSS_x": 392,
                "SF_velocity_y": 1152,
                "SF_LL_y": 36,
                "SF_LLL_y": 216,
                "SF_LTT_y": 432,
                "SF_scalar_y": 2016,
                "SF_LSS_y": 10584,
                "SF_velocity_z": 10368,
                "SF_LL_z": 324,
                "SF_LLL_z": 5832,
                "SF_LTT_z": 17496,
                "SF_scalar_z": 18144,
                "SF_LSS_z": 285768,
            },
        ),
    ],
)
def test_calculate_structure_function_3d_parameterized(
    u,
    v,
    w,
    adv_x,
    adv_y,
    adv_z,
    shift_x,
    shift_y,
    shift_z,
    skip_velocity_sf,
    scalar,
    adv_scalar,
    traditional_type,
    boundary,
    expected_result,
):
    """Test that calculate_structure_function works correctly for multiple cases."""
    output_dict = calculate_structure_function_3d(
        u,
        v,
        w,
        adv_x,
        adv_y,
        adv_z,
        shift_x,
        shift_y,
        shift_z,
        skip_velocity_sf,
        scalar,
        adv_scalar,
        traditional_type,
        boundary,
    )

    TestCase().assertDictEqual(output_dict, expected_result)
