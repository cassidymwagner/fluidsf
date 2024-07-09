import numpy as np
import pytest

from fluidsf.generate_structure_functions_1d import generate_structure_functions_1d


@pytest.mark.parametrize(
    "u, x, v, y, scalar, traditional_type, dx, boundary, even, grid_type, "
    "nbins, expected_dict",
    [
        # Test 1: all traditional structure functions for a uniform even grid
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
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
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # dx
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
        ),
        # Test 3: grid_type is 'non-uniform' and ValueError is raised
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # dx
            None,  # boundary
            True,  # even
            "non-uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 4: boundary is 'periodic-x' and ValueError is raised
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # dx
            "periodic-x",  # boundary
            True,  # even
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 5: grid_type is 'latlon', y is None, and ValueError is raised
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT", "LSS"],  # traditional_type
            None,  # dx
            None,  # boundary
            True,  # even
            "latlon",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 6: "LSS" in traditional_type and scalar is None, ValueError is raised
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
            None,  # y
            None,  # scalar
            ["LSS"],  # traditional_type
            None,  # dx
            None,  # boundary
            True,  # even
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 7: "LTT" in traditional_type and v is None, ValueError is raised
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            None,  # v
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LTT"],  # traditional_type
            None,  # dx
            None,  # boundary
            True,  # even
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 8: scalar not None, "LSS" not in traditional_type, ValueError is raised
        (
            np.array([1, 2, 3, 4]),  # u
            np.array([1, 2, 3, 4]),  # x
            np.array([2, 4, 6, 8]),  # v
            None,  # y
            np.array([3, 6, 9, 12]),  # scalar
            ["LL", "LLL", "LTT"],  # traditional_type
            None,  # dx
            None,  # boundary
            True,  # even
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
    ],
)
def test_generate_structure_functions_1d_parameterized(
    u,
    x,
    v,
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
    
    if expected_dict == ValueError:
        with pytest.raises(ValueError):
            generate_structure_functions_1d(
                u, x, v, y, scalar, traditional_type, dx, boundary, even, grid_type, nbins
            )
        return
    else:
        output_dict = generate_structure_functions_1d(
            u, x, v, y, scalar, traditional_type, dx, boundary, even, grid_type, nbins
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
