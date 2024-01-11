import numpy as np
import pytest

from oceans_sf.calculate_advection import calculate_advection


@pytest.mark.parametrize(
    "u, v, x, y, dx, dy, grid_type, scalar, expected_advection_result",
    [
        # Test case for velocity field with zero values
        (
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.linspace(0, 3, 4),
            np.linspace(0, 3, 4),
            None,
            None,
            "uniform",
            None,
            (
                np.array([[0] * 3 for i in range(3)]),
                np.array([[0] * 3 for i in range(3)]),
            ),
        ),
        # Test case for velocity field with non-zero values
        (
            np.array([[1] * 3 for i in range(3)]),
            np.array([[1] * 3 for i in range(3)]),
            np.linspace(0, 3, 4),
            np.linspace(0, 3, 4),
            None,
            None,
            "uniform",
            None,
            (
                np.array([[0] * 3 for i in range(3)]),
                np.array([[0] * 3 for i in range(3)]),
            ),
        ),
        # Test case for velocity field with non-zero values and non-uniform grid
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.linspace(0, 2, 3),
            np.linspace(0, 2, 3),
            None,
            None,
            "uniform",
            None,
            (
                np.array(
                    [
                        [2 * 2, 2 * 4, 2 * 6],
                        [2 * 8, 2 * 10, 2 * 12],
                        [2 * 14, 2 * 16, 2 * 18],
                    ]
                ),
                np.array(
                    [
                        [2 * 2, 2 * 4, 2 * 6],
                        [2 * 8, 2 * 10, 2 * 12],
                        [2 * 14, 2 * 16, 2 * 18],
                    ]
                ),
            ),
        ),
        # Test case for velocity field with positive and negative values
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.linspace(0, 1, 2),
            np.linspace(0, 1, 2),
            None,
            None,
            "uniform",
            None,
            (
                np.array(
                    [
                        [3, -2],
                        [-3, 12],
                    ]
                ),
                np.array(
                    [
                        [-7, -18],
                        [33, 52],
                    ]
                ),
            ),
        ),
        # Test case for scalar field with non-zero values and latlon grid
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([0, 1, 1]),
            np.array([0, 1, 1]),
            np.array([0, 1, 1]),
            np.array([0, 1, 1]),
            "latlon",
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array(
                [
                    [2 * 2, 2 * 4, 2 * 6],
                    [2 * 8, 2 * 10, 2 * 12],
                    [2 * 14, 2 * 16, 2 * 18],
                ]
            ),
        ),
        # Test case for scalar field with positive and negative values and latlon grid
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([0, 1]),
            np.array([0, 1]),
            np.array([0, 1]),
            np.array([0, 1]),
            "latlon",
            np.array([[1, 2], [3, 4]]),
            np.array(
                [
                    [3, -2],
                    [-3, 12],
                ]
            ),
        ),
        # Test case for scalar field with non-zero values and uniform grid
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([0, 1, 1]),
            np.array([0, 1, 1]),
            np.array([0, 1, 1]),
            np.array([0, 1, 1]),
            "uniform",
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array(
                [
                    [2 * 2, 2 * 4, 2 * 6],
                    [2 * 8, 2 * 10, 2 * 12],
                    [2 * 14, 2 * 16, 2 * 18],
                ]
            ),
        ),
        # Test case for scalar field with positive and negative values and uniform grid
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([0, 1]),
            np.array([0, 1]),
            np.array([0, 1]),
            np.array([0, 1]),
            "uniform",
            np.array([[1, 2], [3, 4]]),
            np.array(
                [
                    [3, -2],
                    [-3, 12],
                ]
            ),
        ),
    ],
)
def test_calculate_advection(
    u, v, x, y, dx, dy, grid_type, scalar, expected_advection_result
):
    """Test that calculate_advection works correctly for multiple cases."""
    output_advection = calculate_advection(u, v, x, y, dx, dy, grid_type, scalar)
    np.testing.assert_allclose(output_advection, expected_advection_result)
