import numpy as np
import pytest

from oceans_sf.calculate_advection_velocity_structure_function import (
    calculate_advection_velocity_structure_function,
)


@pytest.mark.parametrize(
    "u, v, adv_e, adv_n, u_shift, v_shift, adv_e_shift, adv_n_shift, expected_sf",
    [
        (
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            0.0,
        ),
        (
            np.array([[1] * 3 for i in range(3)]),
            np.array([[1] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            np.array([[0] * 3 for i in range(3)]),
            0.0,
        ),
        (
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            0.0,
        ),
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[0, 0], [0, 0]]),
            np.array([[0, 0], [0, 0]]),
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[0, 0], [0, 0]]),
            np.array([[0, 0], [0, 0]]),
            0.0,
        ),
    ],
)
def test_calculate_advection_velocity_structure_function_parameterized(
    u, v, adv_e, adv_n, u_shift, v_shift, adv_e_shift, adv_n_shift, expected_sf
):
    """Test that calculate_advection_velocity_structure_function works correctly
    for multiple cases.
    """
    SF = calculate_advection_velocity_structure_function(
        u, v, adv_e, adv_n, u_shift, v_shift, adv_e_shift, adv_n_shift
    )
    np.testing.assert_allclose(SF, expected_sf)
