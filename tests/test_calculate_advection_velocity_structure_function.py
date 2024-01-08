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
            np.array([[1, 2], [3, 4]]),
            np.array([[1, -2], [-3, 4]]),
            np.array([[3, -2], [-3, 12]]),
            np.array([[-7, -18], [33, 52]]),
            np.array([[2, 1], [4, 3]]),
            np.array([[-2, 1], [4, -3]]),
            np.array([[-2, 3], [12, -3]]),
            np.array([[-18, -7], [52, 33]]),
            88,
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
