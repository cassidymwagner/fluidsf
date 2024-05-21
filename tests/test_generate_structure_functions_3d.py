import numpy as np
import pytest

from oceans_sf.generate_structure_functions_3d import generate_structure_functions_3d


@pytest.mark.parametrize(
    "u, v, w, x, y, z, skip_velocity_sf, scalar, traditional_type,"
    "boundary, expected_dict",
    [
        # Test 1: all with zero values and periodic
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            False,  # skip_velocity_sf
            np.zeros((3, 3, 3)),  # scalar
            ["LL", "LLL", "LSS", "LTT"],  # traditional_order
            "periodic-all",  # boundary
            {
                "SF_advection_velocity_x": np.zeros(2),
                "SF_advection_velocity_y": np.zeros(2),
                "SF_advection_velocity_z": np.zeros(2),
                "SF_advection_scalar_x": np.zeros(2),
                "SF_advection_scalar_y": np.zeros(2),
                "SF_advection_scalar_z": np.zeros(2),
                "SF_LL_x": np.zeros(2),
                "SF_LL_y": np.zeros(2),
                "SF_LL_z": np.zeros(2),
                "SF_LLL_x": np.zeros(2),
                "SF_LLL_y": np.zeros(2),
                "SF_LLL_z": np.zeros(2),
                "SF_LSS_x": np.zeros(2),
                "SF_LSS_y": np.zeros(2),
                "SF_LSS_z": np.zeros(2),
                "SF_LTT_x": np.zeros(2),
                "SF_LTT_y": np.zeros(2),
                "SF_LTT_z": np.zeros(2),
                "x-diffs": np.zeros(2),
                "y-diffs": np.zeros(2),
                "z-diffs": np.zeros(2),
            },  # expected_dict
        ),
        # Test 2: all with zero values and no boundary
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            False,  # skip_velocity_sf
            np.zeros((3, 3, 3)),  # scalar
            ["LL", "LLL", "LSS", "LTT"],  # traditional_order
            None,  # boundary
            {
                "SF_advection_velocity_x": np.zeros(2),
                "SF_advection_velocity_y": np.zeros(2),
                "SF_advection_velocity_z": np.zeros(2),
                "SF_advection_scalar_x": np.zeros(2),
                "SF_advection_scalar_y": np.zeros(2),
                "SF_advection_scalar_z": np.zeros(2),
                "SF_LL_x": np.zeros(2),
                "SF_LL_y": np.zeros(2),
                "SF_LL_z": np.zeros(2),
                "SF_LLL_x": np.zeros(2),
                "SF_LLL_y": np.zeros(2),
                "SF_LLL_z": np.zeros(2),
                "SF_LSS_x": np.zeros(2),
                "SF_LSS_y": np.zeros(2),
                "SF_LSS_z": np.zeros(2),
                "SF_LTT_x": np.zeros(2),
                "SF_LTT_y": np.zeros(2),
                "SF_LTT_z": np.zeros(2),
                "x-diffs": np.linspace(0, 1, 2),
                "y-diffs": np.linspace(0, 1, 2),
                "z-diffs": np.linspace(0, 1, 2),
            },  # expected_dict
        ),
        # Test 3: all with non-zero values and no boundary
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            np.arange(1, 28).reshape((3, 3, 3)),  # v
            np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            False,  # skip_velocity_sf
            np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            ["LL", "LLL", "LSS", "LTT"],  # traditional_order
            None,  # boundary
            {
                "SF_advection_velocity_x": np.array([0, 0]),
                "SF_advection_velocity_y": np.array([0, 0]),
                "SF_advection_velocity_z": np.array([0, 0]),
                "SF_advection_scalar_x": np.array([0, 0]),
                "SF_advection_scalar_y": np.array([0, 0]),
                "SF_advection_scalar_z": np.array([0, 0]),
                "SF_LL_x": np.array([0, 4]),
                "SF_LL_y": np.array([0, 36]),
                "SF_LL_z": np.array([0, 324]),
                "SF_LLL_x": np.array([0, 8]),
                "SF_LLL_y": np.array([0, 216]),
                "SF_LLL_z": np.array([0, 5832]),
                "SF_LSS_x": np.array([0, 8]),
                "SF_LSS_y": np.array([0, 216]),
                "SF_LSS_z": np.array([0, 5832]),
                "SF_LTT_x": np.array([0, 8]),
                "SF_LTT_y": np.array([0, 216]),
                "SF_LTT_z": np.array([0, 5832]),
                "x-diffs": np.array([0, 1]),
                "y-diffs": np.array([0, 1]),
                "z-diffs": np.array([0, 1]),
            },  # expected_dict
        ),
        # Test 4: all with different values and no boundary
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            2 * np.arange(1, 28).reshape((3, 3, 3)),  # v
            3 * np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            False,  # skip_velocity_sf
            np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            ["LL", "LLL", "LSS", "LTT"],  # traditional_order
            None,  # boundary
            {
                "SF_advection_velocity_x": np.array([0, 224]),
                "SF_advection_velocity_y": np.array([0, 2016]),
                "SF_advection_velocity_z": np.array([0, 18144]),
                "SF_advection_scalar_x": np.array([0, 16]),
                "SF_advection_scalar_y": np.array([0, 144]),
                "SF_advection_scalar_z": np.array([0, 1296]),
                "SF_LL_x": np.array([0, 4]),
                "SF_LL_y": np.array([0, 36]),
                "SF_LL_z": np.array([0, 324]),
                "SF_LLL_x": np.array([0, 8]),
                "SF_LLL_y": np.array([0, 216]),
                "SF_LLL_z": np.array([0, 5832]),
                "SF_LSS_x": np.array([0, 8]),
                "SF_LSS_y": np.array([0, 216]),
                "SF_LSS_z": np.array([0, 5832]),
                "SF_LTT_x": np.array([0, 32]),
                "SF_LTT_y": np.array([0, 432]),
                "SF_LTT_z": np.array([0, 17496]),
                "x-diffs": np.array([0, 1]),
                "y-diffs": np.array([0, 1]),
                "z-diffs": np.array([0, 1]),
            },  # expected_dict
        ),
        # Test 5: advection only with different values and no boundary
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            2 * np.arange(1, 28).reshape((3, 3, 3)),  # v
            3 * np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            False,  # skip_velocity_sf
            None,  # scalar
            None,  # traditional_order
            None,  # boundary
            {
                "SF_advection_velocity_x": np.array([0, 224]),
                "SF_advection_velocity_y": np.array([0, 2016]),
                "SF_advection_velocity_z": np.array([0, 18144]),
                "x-diffs": np.array([0, 1]),
                "y-diffs": np.array([0, 1]),
                "z-diffs": np.array([0, 1]),
            },  # expected_dict
        ),
        # Test 6: traditional only with different values and no boundary
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            2 * np.arange(1, 28).reshape((3, 3, 3)),  # v
            3 * np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            False,  # skip_velocity_sf
            None,  # scalar
            ["LL", "LLL", "LSS", "LTT"],  # traditional_order
            None,  # boundary
            {
                "SF_LL_x": np.array([0, 4]),
                "SF_LL_y": np.array([0, 36]),
                "SF_LL_z": np.array([0, 324]),
                "SF_LLL_x": np.array([0, 8]),
                "SF_LLL_y": np.array([0, 216]),
                "SF_LLL_z": np.array([0, 5832]),
                "SF_LTT_x": np.array([0, 32]),
                "SF_LTT_y": np.array([0, 432]),
                "SF_LTT_z": np.array([0, 17496]),
                "x-diffs": np.array([0, 1]),
                "y-diffs": np.array([0, 1]),
                "z-diffs": np.array([0, 1]),
            },  # expected_dict
        ),
        # Test 7: scalar only with different values and no boundary
        (
            np.arange(1, 28).reshape((3, 3, 3)),  # u
            2 * np.arange(1, 28).reshape((3, 3, 3)),  # v
            3 * np.arange(1, 28).reshape((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            True,  # skip_velocity_sf
            np.arange(1, 28).reshape((3, 3, 3)),  # scalar
            None,  # traditional_order
            None,  # boundary
            {
                "SF_advection_scalar_x": np.array([0, 16]),
                "SF_advection_scalar_y": np.array([0, 144]),
                "SF_advection_scalar_z": np.array([0, 1296]),
                "x-diffs": np.array([0, 1]),
                "y-diffs": np.array([0, 1]),
                "z-diffs": np.array([0, 1]),
            },  # expected_dict
        ),
    ],
)
def test_generate_structure_functions_3d_parameterized(
    u,
    v,
    w,
    x,
    y,
    z,
    skip_velocity_sf,
    scalar,
    traditional_type,
    boundary,
    expected_dict,
):
    """Test generate_structure_functions produces expected results."""
    output_dict = generate_structure_functions_3d(
        u, v, w, x, y, z, skip_velocity_sf, scalar, traditional_type, boundary
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
