import numpy as np
import pytest
from fluidsf.calculate_structure_function_3d import calculate_structure_function_3d


@pytest.mark.parametrize(
    "u, v, w, adv_x, adv_y, adv_z, shift_x, shift_y, shift_z, sf_type, scalar,"
    "adv_scalar, boundary, expected_result",
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
            ["ASF_V", "ASF_S", "LL", "LLL", "LTT", "LSS"],  # sf_type
            np.zeros((3, 3, 3)),  # scalar
            np.zeros((3, 3, 3)),  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_advection_velocity_x": 0,
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LTT_x": 0,
                "SF_advection_scalar_x": 0,
                "SF_LSS_x": 0,
                "SF_advection_velocity_y": 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
                "SF_LTT_y": 0,
                "SF_advection_scalar_y": 0,
                "SF_LSS_y": 0,
                "SF_advection_velocity_z": 0,
                "SF_LL_z": 0,
                "SF_LLL_z": 0,
                "SF_LTT_z": 0,
                "SF_advection_scalar_z": 0,
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
            ["ASF_V", "ASF_S", "LL", "LLL", "LTT", "LSS"],  # sf_type
            np.ones((3, 3, 3)),  # scalar
            np.ones((3, 3, 3)),  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_advection_velocity_x": 0,
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LTT_x": 0,
                "SF_advection_scalar_x": 0,
                "SF_LSS_x": 0,
                "SF_advection_velocity_y": 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
                "SF_LTT_y": 0,
                "SF_advection_scalar_y": 0,
                "SF_LSS_y": 0,
                "SF_advection_velocity_z": 0,
                "SF_LL_z": 0,
                "SF_LLL_z": 0,
                "SF_LTT_z": 0,
                "SF_advection_scalar_z": 0,
                "SF_LSS_z": 0,
            },
        ),
        # Test 3: linear velocities all SFs non-periodic no scalar
        (
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # u
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # v
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # w
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[0]
            + np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[1]
            + np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[
                2
            ],  # adv_x
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[0]
            + np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[1]
            + np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[
                2
            ],  # adv_y
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[0]
            + np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[1]
            + np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],
                1,
                1,
                1,
                axis=(2, 1, 0),
            )[
                2
            ],  # adv_z
            1,  # shift_x
            1,  # shift_y
            1,  # shift_z
            ["ASF_V", "LL", "LLL", "LTT"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            None,  # boundary
            {
                "SF_advection_velocity_x": 0,
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LTT_x": 0,
                "SF_advection_velocity_y": 3 * (1) ** 2,
                "SF_LL_y": 1 * (1) ** 2,
                "SF_LLL_y": 1 * (1) ** 3,
                "SF_LTT_y": 2 * (1) ** 3,
                "SF_advection_velocity_z": 0,
                "SF_LL_z": 0,
                "SF_LLL_z": 0,
                "SF_LTT_z": 0,
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
    sf_type,
    scalar,
    adv_scalar,
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
        sf_type,
        scalar,
        adv_scalar,
        boundary,
    )

    for key, value in expected_result.items():
        if key in output_dict:
            if not np.allclose(output_dict[key], value):
                print(output_dict[key])
                print(expected_result[key])
                raise AssertionError(
                    f"Output dict value for key '{key}' does not match "
                    f"expected value '{output_dict[key]}'."
                )
        else:
            raise AssertionError(f"Output dict does not contain key '{key}'.")
