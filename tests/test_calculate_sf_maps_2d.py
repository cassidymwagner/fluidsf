import numpy as np
import pytest
from fluidsf.calculate_sf_maps_2d import calculate_sf_maps_2d


@pytest.mark.parametrize(
    "u, v, x, y, adv_x, adv_y, shift_in_x, shift_in_y, sf_type, scalar, adv_scalar, "
    "expected_sf_maps",
    [
        # Test 1: Test case with all zeros
        (
            np.zeros((3, 3)),  # u
            np.zeros((3, 3)),  # v
            np.array([0, 1, 2]),  # x
            np.array([0, 1, 2]),  # y
            np.zeros((3, 3)),  # adv_x
            np.zeros((3, 3)),  # adv_y
            1,  # shift_in_x
            1,  # shift_in_y
            ["ASF_V", "LLL", "LTT", "LSS", "LL", "TT", "SS"],  # sf_type
            np.zeros((3, 3)),  # scalar
            np.zeros((3, 3)),  # adv_scalar
            {
                "SF_LL_xy": 0.0,
                "SF_TT_xy": 0.0,
                "SF_SS_xy": 0.0,
                "SF_LLL_xy": 0.0,
                "SF_LTT_xy": 0.0,
                "SF_LSS_xy": 0.0,
            },  # expected_sf_maps
        ),
        # Test 2: Test case with all ones
        (
            np.ones((3, 3)),  # u
            np.ones((3, 3)),  # v
            np.array([0, 1, 2]),  # x
            np.array([0, 1, 2]),  # y
            np.ones((3, 3)),  # adv_x
            np.ones((3, 3)),  # adv_y
            1,  # shift_in_x
            1,  # shift_in_y
            ["ASF_V", "LLL", "LTT", "LSS", "LL", "TT", "SS"],  # sf_type
            np.ones((3, 3)),  # scalar
            np.ones((3, 3)),  # adv_scalar
            {
                "SF_LL_xy": 0.0,
                "SF_TT_xy": 0.0,
                "SF_SS_xy": 0.0,
                "SF_LLL_xy": 0.0,
                "SF_LTT_xy": 0.0,
                "SF_LSS_xy": 0.0,
            },  # expected_sf_maps
        ),
        # Test 3: slanted velocities np.arange(10) tiled in y no scalar only LL, LLL
        # with shift 5
        (
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # u
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # v
            np.linspace(0, 10**2, 10**2),  # x
            np.linspace(0, 10**2, 10**2),  # y
            None,  # adv_x
            None,  # adv_y
            5,  # shift_x
            5,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            {
                "SF_LL_xy": 10 * (10 / 2),
                "SF_LLL_xy": 0,
            },
        ),
        # Test 4: slanted velocities np.arange(12) tiled in y no scalar only LL, LLL
        # with shift 6
        (
            np.tile(np.tile(np.arange(12), 12), (12**2, 1)),  # u
            np.tile(np.tile(np.arange(12), 12), (12**2, 1)),  # v
            np.linspace(0, 12**2, 12**2),  # x
            np.linspace(0, 12**2, 12**2),  # y
            None,  # adv_x
            None,  # adv_y
            6,  # shift_x
            6,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            {
                "SF_LL_xy": 12 * (12 / 2),
                "SF_LLL_xy": 0,
            },
        ),
        # Test 5: slanted velocities np.arange(10) tiled in y no scalar only LL, LLL
        # with shift 10
        (
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # u
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # v
            np.linspace(0, 10**2, 10**2),  # x
            np.linspace(0, 10**2, 10**2),  # y
            None,  # adv_x
            None,  # adv_y
            10,  # shift_x
            10,  # shift_y
            ["LL", "LLL"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            {
                "SF_LL_xy": 0,
                "SF_LLL_xy": 0,
            },
        ),
        # Test 6: slanted velocities np.arange(10) tiled in y no scalar only LL, LLL
        # TT, LTT with shift 5
        (
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # u
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # v
            np.linspace(0, 10**2, 10**2),  # x
            np.linspace(0, 10**2, 10**2),  # y
            None,  # adv_x
            None,  # adv_y
            5,  # shift_x
            5,  # shift_y
            ["LL", "LLL", "TT", "LTT"],  # sf_type
            None,  # scalar
            None,  # adv_scalar
            {
                "SF_LL_xy": 10 * (10 / 2),
                "SF_TT_xy": 0,
                "SF_LTT_xy": 0,
                "SF_LLL_xy": 0,
            },
        ),
    ],
)
def test_calculate_sf_maps_2d(
    u,
    v,
    x,
    y,
    adv_x,
    adv_y,
    shift_in_x,
    shift_in_y,
    sf_type,
    scalar,
    adv_scalar,
    expected_sf_maps,
):
    output_sf_maps = calculate_sf_maps_2d(
        u, v, x, y, adv_x, adv_y, shift_in_x, shift_in_y, sf_type, scalar, adv_scalar
    )

    for key, value in expected_sf_maps.items():
        if key in output_sf_maps:
            if not np.allclose(output_sf_maps[key], value):
                print(output_sf_maps[key])
                print(expected_sf_maps[key])
                raise AssertionError(
                    f"Output dict value for key '{key}' does not match "
                    f"expected value '{output_sf_maps[key]}'."
                )
        else:
            raise AssertionError(f"Output dict does not contain key '{key}'.")
