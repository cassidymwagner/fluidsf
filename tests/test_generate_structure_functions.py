import numpy as np
import pytest
from geopy.distance import great_circle

from fluidsf.generate_structure_functions import generate_structure_functions


@pytest.mark.parametrize(
    "u, v, x, y, skip_velocity_sf, scalar, traditional_type, dx, dy, boundary, "
    "grid_type, nbins, expected_dict",
    [
        # Test 1: linear velocities all SFs no scalar non-periodic
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            False,  # skip_velocity_sf
            None,  # scalar
            ["LLL", "LL", "LTT"],  # traditional_type
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": (5 / 4) * np.linspace(0, 8, 9) ** 2,
                "SF_advection_velocity_y": 0 * np.linspace(0, 8, 9),
                "SF_LLL_x": np.linspace(0, 8, 9) ** 3,
                "SF_LLL_y": 0 * np.linspace(0, 8, 9),
                "SF_LTT_x": (1 / 4) * np.linspace(0, 8, 9) ** 3,
                "SF_LTT_y": 0 * np.linspace(0, 8, 9),
                "SF_LL_x": np.linspace(0, 8, 9) ** 2,
                "SF_LL_y": 0 * np.linspace(0, 8, 9),
                "x-diffs": np.linspace(0, 8, 9),
                "y-diffs": np.linspace(0, 8, 9),
            },
        ),
        # Test 2: linear velocities all SFs no scalar non-periodic latlon grid
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            False,  # skip_velocity_sf
            None,  # scalar
            ["LLL", "LL", "LTT"],  # traditional_type
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            "latlon",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": (5 / 4) * np.linspace(0, 8, 9) ** 2,
                "SF_advection_velocity_y": 0 * np.linspace(0, 8, 9),
                "SF_LLL_x": np.linspace(0, 8, 9) ** 3,
                "SF_LLL_y": 0 * np.linspace(0, 8, 9),
                "SF_LTT_x": (1 / 4) * np.linspace(0, 8, 9) ** 3,
                "SF_LTT_y": 0 * np.linspace(0, 8, 9),
                "SF_LL_x": np.linspace(0, 8, 9) ** 2,
                "SF_LL_y": 0 * np.linspace(0, 8, 9),
                "x-diffs": np.array(
                    [great_circle((i, 0), (0, 0)).meters for i in range(9)]
                ),
                "y-diffs": np.array(
                    [great_circle((0, i), (0, 0)).meters for i in range(9)]
                ),
            },
        ),
    ],
)
def test_generate_structure_functions_parameterized(
    u,
    v,
    x,
    y,
    skip_velocity_sf,
    scalar,
    traditional_type,
    dx,
    dy,
    boundary,
    grid_type,
    nbins,
    expected_dict,
):
    """Test generate_structure_functions produces expected results."""
    output_dict = generate_structure_functions(
        u,
        v,
        x,
        y,
        skip_velocity_sf,
        scalar,
        traditional_type,
        dx,
        dy,
        boundary,
        grid_type,
        nbins,
    )
    for key, value in expected_dict.items():
        if key in output_dict:
            if not np.allclose(output_dict[key], value, equal_nan=True):
                print(output_dict[key])
                print(expected_dict[key])
                print(type(output_dict[key]), type(expected_dict[key]))
                print(len(output_dict[key]), len(expected_dict[key]))
                raise AssertionError(
                    f"Output dict value for key '{key}' does not match "
                    f"expected value '{output_dict[key]}'."
                )
        else:
            raise AssertionError(f"Output dict does not contain key '{key}'.")
