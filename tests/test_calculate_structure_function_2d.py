import numpy as np
import pytest
from fluidsf.calculate_structure_function_2d import calculate_structure_function_2d


@pytest.mark.parametrize(
    "u, v, adv_x, adv_y, shift_x, shift_y, sf_type, scalar, "
    "adv_scalar, boundary, expected_result",
    [
        # # Test 1: velocity and scalar no traditional
        # (
        #     np.array([[1, 2], [3, 4]]),  # u
        #     np.array([[1, -2], [-3, 4]]),  # v
        #     np.array([[3, -2], [-3, 12]]),  # adv_x
        #     np.array([[-7, -18], [33, 52]]),  # adv_y
        #     1,  # x_shift
        #     1,  # y_shift
        #     False,  # skip_velocity_sf
        #     np.array([[1, 2], [3, 4]]),  # scalar
        #     np.array([[3, -2], [-3, 12]]),  # adv_scalar
        #     None,  # traditional_type
        #     "periodic-all",  # boundary
        #     {
        #         "SF_velocity_x": 88,
        #         "SF_velocity_y": 138,
        #         "SF_scalar_x": 5,
        #         "SF_scalar_y": 8,
        #     },
        #     # expected_result
        # ),
        # # Test 2: all
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     False,
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     ["LL"],
        #     "periodic-all",
        #     {
        #         "SF_velocity_x": 88,
        #         "SF_LL_x": 1,
        #         "SF_scalar_x": 5,
        #         "SF_velocity_y": 138,
        #         "SF_LL_y": 26,
        #         "SF_scalar_y": 8,
        #     },
        # ),
        # # Test 3: all but skip velocity and no traditional
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     True,
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     None,
        #     "periodic-all",
        #     {
        #         "SF_scalar_x": 5,
        #         "SF_scalar_y": 8,
        #     },
        # ),
        # # Test 4: velocities with no scalar or traditional
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     False,
        #     None,
        #     None,
        #     None,
        #     "periodic-all",
        #     {
        #         "SF_velocity_x": 88,
        #         "SF_velocity_y": 138,
        #     },
        # ),
        # # Test 5: velocity and scalar no traditional non-periodic
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     False,
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     None,
        #     None,
        #     {
        #         "SF_velocity_x": 88,
        #         "SF_velocity_y": 138,
        #         "SF_scalar_x": 5,
        #         "SF_scalar_y": 8,
        #     },
        # ),
        # # Test 6: all non-periodic
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     False,
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     ["LL"],
        #     None,
        #     {
        #         "SF_velocity_x": 88,
        #         "SF_LL_x": 1,
        #         "SF_scalar_x": 5,
        #         "SF_velocity_y": 138,
        #         "SF_LL_y": 26,
        #         "SF_scalar_y": 8,
        #     },
        # ),
        # # Test 7: all but skip velocity and no traditional non-periodic
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     True,
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     None,
        #     None,
        #     {
        #         "SF_scalar_x": 5,
        #         "SF_scalar_y": 8,
        #     },
        # ),
        # # Test 8: velocities with no scalar or traditional non-periodic
        # (
        #     np.array([[1, 2], [3, 4]]),
        #     np.array([[1, -2], [-3, 4]]),
        #     np.array([[3, -2], [-3, 12]]),
        #     np.array([[-7, -18], [33, 52]]),
        #     1,
        #     1,
        #     False,
        #     None,
        #     None,
        #     None,
        #     None,
        #     {
        #         "SF_velocity_x": 88,
        #         "SF_velocity_y": 138,
        #     },
        # ),
        # Test 9: linear velocities all SFs non-periodic
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_x
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                0.5 * np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                0.5 * np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["ASF_V", "LL", "LLL", "LTT"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            None,  # boundary
            {
                "SF_advection_velocity_x": (5 / 4) * 1,
                "SF_LL_x": 1,
                "SF_LLL_x": 1,
                "SF_LTT_x": (1 / 4) * 1,
                "SF_advection_velocity_y": (5 / 4) * 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
                "SF_LTT_y": (1 / 4) * 0,
            },
        ),
        # Test 10: linear velocities no traditional non-periodic
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_x
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                0.5 * np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                0.5 * np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["ASF_V"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            None,  # boundary
            {
                "SF_advection_velocity_x": (5 / 4) * 1,
                "SF_advection_velocity_y": (5 / 4) * 0,
            },
        ),
        # Test 11: linear velocities and scalar=v non-periodic
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_x
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                0.5 * np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                0.5 * np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["ASF_V", "ASF_S", "LL", "LLL", "LTT", "LSS"],  # sf_type
            np.meshgrid(np.arange(10), np.arange(10))[0],  # scalar
            np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[0]
            + 0.5
            * np.meshgrid(np.arange(10), np.arange(10))[0]
            * np.gradient(
                np.meshgrid(np.arange(10), np.arange(10))[0], 1, 1, axis=(1, 0)
            )[
                1
            ],  # adv_scalar
            None,  # boundary
            {
                "SF_advection_velocity_x": (5 / 4) * 1,
                "SF_LL_x": 1,
                "SF_LLL_x": 1,
                "SF_LTT_x": (1 / 4) * 1,
                "SF_advection_velocity_y": (5 / 4) * 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
                "SF_LTT_y": (1 / 4) * 0,
                "SF_advection_scalar_x": 1,
                "SF_advection_scalar_y": 0,
                "SF_LSS_x": 1,
                "SF_LSS_y": 0,
            },
        ),
        # Test 12: slanted velocities np.arange(5) no scalar only LL,LLL periodic with
        # shift 5
        (
            np.tile(np.tile(np.arange(5), 5), (25, 1)),  # u
            np.tile(np.tile(np.arange(5), 5), (25, 1)),  # v
            None,  # adv_x
            None,  # adv_y
            5,  # shift_x
            5,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
            },
        ),
        # Test 13: slanted velocities np.arange(5) tiled in y no scalar only LL,LLL
        # periodic with shift 1
        (
            np.tile(np.tile(np.arange(5), 5), (25, 1)),  # u
            np.tile(np.tile(np.arange(5), 5), (25, 1)),  # v
            None,  # adv_x
            None,  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_LL_x": 4,
                "SF_LLL_x": -4 * 3,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
            },
        ),
        # Test 14: slanted velocities np.arange(6) tiled in y no scalar only LL,LLL
        # periodic with shift 1
        (
            np.tile(np.tile(np.arange(6), 6), (36, 1)),  # u
            np.tile(np.tile(np.arange(6), 6), (36, 1)),  # v
            None,  # adv_x
            None,  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_LL_x": 5,
                "SF_LLL_x": -5 * 4,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
            },
        ),
        # Test 15: slanted velocities np.arange(5) tiled in x no scalar only LL,LLL
        # periodic with shift 1
        (
            np.tile(np.tile(np.arange(5), 5), (25, 1)).T,  # u
            np.tile(np.tile(np.arange(5), 5), (25, 1)).T,  # v
            None,  # adv_x
            None,  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LL_y": 4,
                "SF_LLL_y": -4 * 3,
            },
        ),
        # Test 16: slanted velocities np.arange(6) tiled in x no scalar only LL,LLL
        # periodic with shift 1
        (
            np.tile(np.tile(np.arange(6), 6), (36, 1)).T,  # u
            np.tile(np.tile(np.arange(6), 6), (36, 1)).T,  # v
            None,  # adv_x
            None,  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_LL_x": 0,
                "SF_LLL_x": 0,
                "SF_LL_y": 5,
                "SF_LLL_y": -5 * 4,
            },
        ),
        # Test 17: slanted velocities np.arange(15) tilted in y no scalar only LL,LLL
        # periodic with shift 1
        (
            np.tile(np.tile(np.arange(15), 15), (225, 1)),  # u
            np.tile(np.tile(np.arange(15), 15), (225, 1)),  # v
            None,  # adv_x
            None,  # adv_y
            1,  # shift_x
            1,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            "periodic-all",  # boundary
            {
                "SF_LL_x": 14,
                "SF_LLL_x": -14 * 13,
                "SF_LL_y": 0,
                "SF_LLL_y": 0,
            },
        ),
    ],
)
def test_calculate_structure_function_parameterized(
    u,
    v,
    adv_x,
    adv_y,
    shift_x,
    shift_y,
    sf_type,
    scalar,
    adv_scalar,
    boundary,
    expected_result,
):
    """Test that calculate_structure_function works correctly for multiple cases."""
    output_dict = calculate_structure_function_2d(
        u,
        v,
        adv_x,
        adv_y,
        shift_x,
        shift_y,
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
