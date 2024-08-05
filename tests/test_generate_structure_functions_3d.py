import numpy as np
import pytest
from fluidsf.generate_structure_functions_3d import generate_structure_functions_3d


@pytest.mark.parametrize(
    "u, v, w, x, y, z, sf_type, scalar," "boundary, nbins, expected_dict",
    [
        # Test 1: all with zero values and periodic
        (
            np.zeros((3, 3, 3)),  # u
            np.zeros((3, 3, 3)),  # v
            np.zeros((3, 3, 3)),  # w
            np.linspace(1, 3, 3),  # x
            np.linspace(1, 3, 3),  # y
            np.linspace(1, 3, 3),  # z
            ["ASF_V", "ASF_S", "LL", "LLL", "LTT", "LSS"],  # sf_type
            np.zeros((3, 3, 3)),  # scalar
            "periodic-all",  # boundary
            None,  # nbins
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
            ["ASF_V", "ASF_S", "LL", "LLL", "LTT", "LSS"],  # sf_type
            np.zeros((3, 3, 3)),  # scalar
            None,  # boundary
            None,  # nbins
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
        # Test 3: linear velocities all SFs no scalar non-periodic no bins
        (
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # u
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # v
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # w
            np.arange(10),  # x
            np.arange(10),  # y
            np.arange(10),  # z
            ["ASF_V", "ASF_S", "LL", "LLL", "LTT", "LSS"],  # sf_type
            np.meshgrid(np.arange(10), np.arange(10), np.arange(10))[0],  # scalar
            None,  # boundary
            None,  # nbins
            {
                "SF_advection_velocity_x": 0 * np.linspace(0, 8, 9),
                "SF_advection_velocity_y": 3 * np.linspace(0, 8, 9) ** 2,
                "SF_advection_velocity_z": 0 * np.linspace(0, 8, 9),
                "SF_advection_scalar_x": 0 * np.linspace(0, 8, 9),
                "SF_advection_scalar_y": 1 * np.linspace(0, 8, 9) ** 2,
                "SF_advection_scalar_z": 0 * np.linspace(0, 8, 9),
                "SF_LL_x": 0 * np.linspace(0, 8, 9),
                "SF_LL_y": 1 * np.linspace(0, 8, 9) ** 2,
                "SF_LL_z": 0 * np.linspace(0, 8, 9),
                "SF_LLL_x": 0 * np.linspace(0, 8, 9),
                "SF_LLL_y": 1 * np.linspace(0, 8, 9) ** 3,
                "SF_LLL_z": 0 * np.linspace(0, 8, 9),
                "SF_LSS_x": 0 * np.linspace(0, 8, 9),
                "SF_LSS_y": 1 * np.linspace(0, 8, 9) ** 3,
                "SF_LSS_z": 0 * np.linspace(0, 8, 9),
                "SF_LTT_x": 0 * np.linspace(0, 8, 9),
                "SF_LTT_y": 2 * np.linspace(0, 8, 9) ** 3,
                "SF_LTT_z": 0 * np.linspace(0, 8, 9),
                "x-diffs": np.linspace(0, 8, 9),
                "y-diffs": np.linspace(0, 8, 9),
                "z-diffs": np.linspace(0, 8, 9),
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
    sf_type,
    scalar,
    boundary,
    nbins,
    expected_dict,
):
    """Test generate_structure_functions produces expected results."""
    output_dict = generate_structure_functions_3d(
        u, v, w, x, y, z, sf_type, scalar, boundary, nbins
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
