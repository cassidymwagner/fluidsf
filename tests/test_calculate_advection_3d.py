import numpy as np
import pytest
from fluidsf.calculate_advection_3d import calculate_advection_3d


@pytest.mark.parametrize(
    "u, v, w, x, y, z, scalar, expected_advection_result",
    [
        # Test case for velocity field with zero values
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            None,  # scalar
            (
                np.zeros((3, 3, 3)),  # expected u_advection
                np.zeros((3, 3, 3)),  # expected v_advection
                np.zeros((3, 3, 3)),  # expected w_advection
            ),
        ),
        # Test case for velocity field with non-zero values
        (
            np.ones((3, 3, 3)),  # u
            np.ones((3, 3, 3)),  # v
            np.ones((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            None,  # scalar
            (
                np.zeros((3, 3, 3)),  # expected u_advection
                np.zeros((3, 3, 3)),  # expected v_advection
                np.zeros((3, 3, 3)),  # expected w_advection
            ),
        ),
        # Test case for velocity field with non-zero values
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.arange(1, 28).reshape((3, 3, 3)),  # v
            np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            None,  # scalar
            (
                np.arange(1, 28).reshape((3, 3, 3)) * 13,  # expected u_advection
                np.arange(1, 28).reshape((3, 3, 3)) * 13,  # expected v_advection
                np.arange(1, 28).reshape((3, 3, 3)) * 13,  # expected w_advection
            ),
        ),
        # Test case for velocity field with non-zero values but zero in w
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.arange(1, 28).reshape((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            None,  # scalar
            (
                np.arange(1, 28).reshape((3, 3, 3)) * 4,  # expected u_advection
                np.arange(1, 28).reshape((3, 3, 3)) * 4,  # expected v_advection
                np.zeros((3, 3, 3)),  # expected w_advection
            ),
        ),
        # Test case for velocity field with non-zero values but zero in v
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            None,  # scalar
            (
                np.arange(1, 28).reshape((3, 3, 3)) * 10,  # expected u_advection
                np.zeros((3, 3, 3)),  # expected v_advection
                np.arange(1, 28).reshape((3, 3, 3)) * 10,  # expected w_advection
            ),
        ),
        # Test case for velocity field with different u, v, w values
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.arange(1, 28).reshape((3, 3, 3)) * 2,  # v
            np.arange(1, 28).reshape((3, 3, 3)) * 3,  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            None,  # scalar
            (
                np.arange(1, 28).reshape((3, 3, 3)) * 34,  # expected u_advection
                np.arange(1, 28).reshape((3, 3, 3)) * 68,  # expected v_advection
                np.arange(1, 28).reshape((3, 3, 3)) * 102,  # expected w_advection
            ),
        ),
        # Test case for scalar field with zero values
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            np.zeros((3, 3, 3)),  # scalar
            np.zeros((3, 3, 3)),  # expected scalar advection
        ),
        # Test case for scalar field with non-zero values but zero velocity
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            np.zeros((3, 3, 3)),  # expected scalar advection
        ),
        # Test case for scalar field with non-zero values
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.arange(1, 28).reshape((3, 3, 3)) * 2,  # v
            np.arange(1, 28).reshape((3, 3, 3)) * 3,  # w
            np.linspace(0, 3, 4),  # x
            np.linspace(0, 3, 4),  # y
            np.linspace(0, 3, 4),  # z
            np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            np.arange(1, 28).reshape((3, 3, 3)) * 34,  # expected scalar advection
        ),
    ],
)
def test_calculate_advection_3d(u, v, w, x, y, z, scalar, expected_advection_result):
    """Test that calculate_advection works correctly for multiple cases."""
    output_advection = calculate_advection_3d(u, v, w, x, y, z, scalar)
    np.testing.assert_allclose(output_advection, expected_advection_result)
