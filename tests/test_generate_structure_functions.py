import numpy as np
import pytest
from geopy.distance import great_circle

from fluidsf.generate_structure_functions import generate_structure_functions


@pytest.mark.parametrize(
    "u, v, x, y, sf_type, scalar, dx, dy, boundary, " "grid_type, nbins, expected_dict",
    [
        # Test 1: linear velocities all SFs no scalar non-periodic
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
            None,  # scalar
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
        # and array of dx and dy
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
            None,  # scalar
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
        # Test 3: linear velocities all SFs no scalar non-periodic latlon grid
        # and single dx and dy raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
            None,  # scalar
            1,  # dx
            1,  # dy
            None,  # boundary
            "latlon",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 4: linear velocities all SFs no scalar non-periodic latlon grid no dx and
        # dy
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "latlon",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 5: linear velocities all SFs scalar provided but no LSS in
        # sf_type non-periodic latlon grid
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            np.arange(10),  # scalar
            ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            "latlon",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 6: linear velocities all SFs scalar not provided but LSS in
        # sf_type non-periodic latlon grid
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["LLL", "LL", "LTT", "LSS"],  # sf_type
            None,  # scalar
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            "latlon",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # # Test 7: linear velocities all SFs no scalar periodic uniform grid
        # (
        #     np.meshgrid(np.arange(10), np.arange(10))[0],  # u
        #     0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
        #     np.arange(10),  # x
        #     np.arange(10),  # y
        #     ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
        #     None,  # scalar
        #     None,  # dx
        #     None,  # dy
        #     "periodic-all",  # boundary
        #     "uniform",  # grid_type
        #     None,  # nbins
        #     {
        #         "SF_advection_velocity_x": (5 / 4) * np.linspace(0, 8, 9) ** 2,
        #         "SF_advection_velocity_y": 0 * np.linspace(0, 8, 9),
        #         "SF_LLL_x": np.linspace(0, 8, 9) ** 3,
        #         "SF_LLL_y": 0 * np.linspace(0, 8, 9),
        #         "SF_LTT_x": (1 / 4) * np.linspace(0, 8, 9) ** 3,
        #         "SF_LTT_y": 0 * np.linspace(0, 8, 9),
        #         "SF_LL_x": np.linspace(0, 8, 9) ** 2,
        #         "SF_LL_y": 0 * np.linspace(0, 8, 9),
        #         "x-diffs": np.linspace(0, 8, 9),
        #         "y-diffs": np.linspace(0, 8, 9),
        #     },
        # ),
    ],
)
def test_generate_structure_functions_parameterized(
    u,
    v,
    x,
    y,
    sf_type,
    scalar,
    dx,
    dy,
    boundary,
    grid_type,
    nbins,
    expected_dict,
):
    """Test generate_structure_functions produces expected results."""
    if expected_dict == ValueError:
        with pytest.raises(ValueError):
            generate_structure_functions(
                u,
                v,
                x,
                y,
                sf_type,
                scalar,
                dx,
                dy,
                boundary,
                grid_type,
                nbins,
            )
        return
    else:
        output_dict = generate_structure_functions(
            u,
            v,
            x,
            y,
            sf_type,
            scalar,
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
