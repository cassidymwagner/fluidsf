import numpy as np
import pytest

from oceans_sf.calculate_advection_3d import calculate_advection_3d


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
                np.zeros((3, 3, 3)),  # expected u_advection
                np.zeros((3, 3, 3)),  # expected v_advection
                np.zeros((3, 3, 3)),  # expected w_advection
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
                8 * np.arange(1, 28).reshape((3, 3, 3))
                - 6 * np.arange(1, 28).reshape((3, 3, 3)),  # expected u_advection
                8 * np.arange(1, 28).reshape((3, 3, 3))
                - 6 * np.arange(1, 28).reshape((3, 3, 3)),  # expected v_advection
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
                -6 * np.arange(1, 28).reshape((3, 3, 3))
                - 2 * np.arange(1, 28).reshape((3, 3, 3)),  # expected u_advection
                np.zeros((3, 3, 3)),  # expected v_advection
                -6 * np.arange(1, 28).reshape((3, 3, 3))
                - 2 * np.arange(1, 28).reshape((3, 3, 3)),  # expected w_advection
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
                -6 * np.arange(1, 28).reshape((3, 3, 3))
                + 8 * 2 * np.arange(1, 28).reshape((3, 3, 3))
                - 2 * 3 * np.arange(1, 28).reshape((3, 3, 3)),  # expected u_advection
                -12 * np.arange(1, 28).reshape((3, 3, 3))
                + 16 * 2 * np.arange(1, 28).reshape((3, 3, 3))
                - 4 * 3 * np.arange(1, 28).reshape((3, 3, 3)),  # expected v_advection
                -18 * np.arange(1, 28).reshape((3, 3, 3))
                + 24 * 2 * np.arange(1, 28).reshape((3, 3, 3))
                - 6 * 3 * np.arange(1, 28).reshape((3, 3, 3)),  # expected w_advection
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
            -6 * np.arange(1, 28).reshape((3, 3, 3))
            + 8 * 2 * np.arange(1, 28).reshape((3, 3, 3))
            - 2 * 3 * np.arange(1, 28).reshape((3, 3, 3)),  # expected scalar advection
        ),
    ],
)
def test_calculate_advection_3d(u, v, w, x, y, z, scalar, expected_advection_result):
    """Test that calculate_advection works correctly for multiple cases."""
    output_advection = calculate_advection_3d(u, v, w, x, y, z, scalar)
    np.testing.assert_allclose(output_advection, expected_advection_result)
