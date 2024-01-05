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
            tuple(
                (
                    np.array([[0] * 3 for i in range(3)]),
                    np.array([[0] * 3 for i in range(3)]),
                ),
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
            tuple(
                (
                    np.array([[0] * 3 for i in range(3)]),
                    np.array([[0] * 3 for i in range(3)]),
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
