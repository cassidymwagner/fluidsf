import numpy as np
import pytest

from oceans_sf.generate_structure_functions_1d import generate_structure_functions_1d


@pytest.mark.parametrize(
    "u, v, x, y, scalar, traditional_type, dx, boundary, even, grid_type, "
    "nbins, expected_dict",
    [
        # Test 1: all traditional structure functions for a uniform even grid
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([2, 4, 6, 8]),  # v
            np.array([1, 2, 3, 4]),  # x
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # dx
            None,  # boundary
            True,  # even
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_LL": np.array([0, 1, 4]),
                "SF_LLL": np.array([0, -1, -8]),
                "SF_LTT": np.array([0, -4, -32]),
                "SF_LSS": np.array([0, -9, -72]),
                "x-diffs": np.array([0, 1, 2]),
            },
        ),
        # Test 2: all traditional structure functions for a uniform uneven grid
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([2, 4, 6, 8]),  # v
            np.array([1, 2, 3, 4]),  # x
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None, # dx
            None,  # boundary
            False,  # even
            "uniform",  # grid_type
            3,  # nbins
            {
                "SF_LL": np.array([0, 1, 4]),
                "SF_LLL": np.array([0, -1, -8]),
                "SF_LTT": np.array([0, -4, -32]),
                "SF_LSS": np.array([0, -9, -72]),
                "x-diffs": np.array([0, 1, 2]),
            },
        )
    ],
)
def test_generate_structure_functions_1d_parameterized(
    u,
    v,
    x,
    y,
    scalar,
    traditional_type,
    dx,
    boundary,
    even,
    grid_type,
    nbins,
    expected_dict,
):
    output_dict = generate_structure_functions_1d(
        u, v, x, y, scalar, traditional_type, dx, boundary, even, grid_type, nbins
    )

    for key, value in expected_dict.items():
        if key in output_dict:
            if not np.allclose(output_dict[key], value):
                print(output_dict[key])
                print(expected_dict[key])
                raise AssertionError(
                    f"Output dict value for key '{key}' does not match "
                    f"expected value '{output_dict[key]}'."
                )
        else:
            raise AssertionError(f"Output dict does not contain key '{key}'.")
