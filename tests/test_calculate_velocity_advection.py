import numpy as np
import pytest

from oceans_sf.calculate_velocity_advection import calculate_velocity_advection


@pytest.mark.parametrize(
    "par_u, par_v, x, y, dx, dy, grid_type, expected_advection_result",
    [
        (
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.linspace(0, 3, 4),
            np.linspace(0, 3, 4),
            None,
            None,
            "uniform",
            (
                np.array([[0] * 3 for i in range(3)]),
                np.array([[0] * 3 for i in range(3)]),
            ),
        ),
        (
            np.array([[1] * 3 for i in range(3)]),
            np.array([[1] * 3 for i in range(3)]),
            np.linspace(0, 3, 4),
            np.linspace(0, 3, 4),
            None,
            None,
            "uniform",
            (
                np.array([[0] * 3 for i in range(3)]),
                np.array([[0] * 3 for i in range(3)]),
            ),
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.linspace(0, 2, 3),
            np.linspace(0, 2, 3),
            None,
            None,
            "uniform",
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
    ],
)
def test_calculate_velocity_advection_parameterized(
    par_u, par_v, x, y, dx, dy, grid_type, expected_advection_result
):
    """Test that calculate_velocity_advection works correctly for multiple cases."""
    output_array = calculate_velocity_advection(par_u, par_v, x, y, dx, dy, grid_type)
    np.testing.assert_allclose(output_array, expected_advection_result)
