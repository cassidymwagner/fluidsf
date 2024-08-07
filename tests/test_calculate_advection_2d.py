import numpy as np
import pytest
from fluidsf.calculate_advection_2d import calculate_advection_2d


@pytest.mark.parametrize(
    "u, v, x, y, dx, dy, grid_type, scalar, expected_advection_result",
    [
        # Test case for velocity field with zero values
        (
            np.array([[0] * 3 for i in range(3)]),  # u
            np.array([[0] * 3 for i in range(3)]),  # v
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            None,  # scalar
            (
                np.array([[0] * 3 for i in range(3)]),  # expected u_advection
                np.array([[0] * 3 for i in range(3)]),  # expected v_advection
            ),
        ),
        # Test case for velocity field with non-zero values
        (
            np.array([[1] * 3 for i in range(3)]),  # u
            np.array([[1] * 3 for i in range(3)]),  # v
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            None,  # scalar
            (
                np.array([[0] * 3 for i in range(3)]),  # expected u_advection
                np.array([[0] * 3 for i in range(3)]),  # expected v_advection
            ),
        ),
        # Test case for velocity field with non-zero values and non-uniform grid
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # u
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # v
            np.linspace(0, 2, 3),  # x
            np.linspace(0, 2, 3),  # y
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            None,  # scalar
            (
                np.array(
                    [
                        [2 * 2, 2 * 4, 2 * 6],
                        [2 * 8, 2 * 10, 2 * 12],
                        [2 * 14, 2 * 16, 2 * 18],
                    ]
                ),  # expected u_advection
                np.array(
                    [
                        [2 * 2, 2 * 4, 2 * 6],
                        [2 * 8, 2 * 10, 2 * 12],
                        [2 * 14, 2 * 16, 2 * 18],
                    ]
                ),  # expected v_advection
            ),
        ),
        # Test case for velocity field with positive and negative values
        (
            np.array([[1, 2], [3, 4]]),  # u
            np.array([[1, -2], [-3, 4]]),  # v
            np.linspace(0, 1, 2),  # x
            np.linspace(0, 1, 2),  # y
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            None,  # scalar
            (
                np.array(
                    [
                        [3, -2],
                        [-3, 12],
                    ]
                ),  # expected u_advection
                np.array(
                    [
                        [-7, -18],
                        [33, 52],
                    ]
                ),  # expected v_advection
            ),
        ),
        # Test case for scalar field with non-zero values and latlon grid
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # u
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # v
            np.array([0, 1, 1]),  # x
            np.array([0, 1, 1]),  # y
            np.array([0, 1, 1]),  # dx
            np.array([0, 1, 1]),  # dy
            "latlon",  # grid_type
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # scalar
            np.array(
                [
                    [2 * 2, 2 * 4, 2 * 6],
                    [2 * 8, 2 * 10, 2 * 12],
                    [2 * 14, 2 * 16, 2 * 18],
                ]
            ),  # expected scalar advection
        ),
        # Test case for scalar field with positive and negative values and latlon grid
        (
            np.array([[1, 2], [3, 4]]),  # u
            np.array([[1, -2], [-3, 4]]),  # v
            np.array([0, 1]),  # x
            np.array([0, 1]),  # y
            np.array([0, 1]),  # dx
            np.array([0, 1]),  # dy
            "latlon",  # grid_type
            np.array([[1, 2], [3, 4]]),  # scalar
            np.array(
                [
                    [3, -2],
                    [-3, 12],
                ]
            ),  # expected scalar advection
        ),
        # Test case for scalar field with non-zero values and uniform grid
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # u
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # v
            np.array([0, 1, 1]),  # x
            np.array([0, 1, 1]),  # y
            np.array([0, 1, 1]),  # dx
            np.array([0, 1, 1]),  # dy
            "uniform",  # grid_type
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # scalar
            np.array(
                [
                    [2 * 2, 2 * 4, 2 * 6],
                    [2 * 8, 2 * 10, 2 * 12],
                    [2 * 14, 2 * 16, 2 * 18],
                ]
            ),  # expected scalar advection
        ),
        # Test case for scalar field with positive and negative values and uniform grid
        (
            np.array([[1, 2], [3, 4]]),  # u
            np.array([[1, -2], [-3, 4]]),  # v
            np.array([0, 1]),  # x
            np.array([0, 1]),  # y
            np.array([0, 1]),  # dx
            np.array([0, 1]),  # dy
            "uniform",  # grid_type
            np.array([[1, 2], [3, 4]]),  # scalar
            np.array(
                [
                    [3, -2],
                    [-3, 12],
                ]
            ),  # expected scalar advection
        ),
    ],
)
def test_calculate_advection(
    u, v, x, y, dx, dy, grid_type, scalar, expected_advection_result
):
    """Test that calculate_advection works correctly for multiple cases."""
    output_advection = calculate_advection_2d(u, v, x, y, dx, dy, grid_type, scalar)
    np.testing.assert_allclose(output_advection, expected_advection_result)
