import numpy as np
import pytest
from fluidsf.generate_structure_functions_2d import generate_structure_functions_2d
from geopy.distance import great_circle


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
        # Test 7: slanted velocities no scalar periodic uniform grid only LL arange(10)
        (
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # u
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # v
            np.linspace(0, 10**2, 10**2),  # x
            np.linspace(0, 10**2, 10**2),  # y
            ["LL"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            "periodic-all",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_LL_x": np.tile(
                    np.concatenate(
                        (
                            np.asarray((10 / 2) ** 2 - np.arange(int(10 / 2) + 1) ** 2)[
                                ::-1
                            ],
                            np.asarray((10 / 2) ** 2 - np.arange(int(10 / 2) + 1) ** 2)[
                                1:-1
                            ],
                        )
                    ),
                    int(10 / 2),
                ),
                "SF_LL_y": np.zeros(50),
                "x-diffs": np.linspace(0, 10**2, 10**2)[:50],
                "y-diffs": np.linspace(0, 10**2, 10**2)[:50],
            },
        ),
        # Test 8: slanted velocities no scalar periodic uniform grid only LL arange(9)
        (
            np.tile(np.tile(np.arange(9), 9), (9**2, 1)),  # u
            np.tile(np.tile(np.arange(9), 9), (9**2, 1)),  # v
            np.linspace(0, 9**2, 9**2),  # x
            np.linspace(0, 9**2, 9**2),  # y
            ["LL"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            "periodic-all",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_LL_x": np.tile(
                    np.concatenate(
                        (
                            np.asarray(
                                [
                                    sum((9 - 1) - (2 * i) for i in range(j))
                                    for j in range(int((9 + 1) / 2))
                                ]
                            ),
                            np.asarray(
                                [
                                    sum((9 - 1) - (2 * i) for i in range(j))
                                    for j in range(int((9 + 1) / 2))
                                ][::-1][:-1]
                            ),
                        )
                    ),
                    int((9 + 1) / 2),
                )[: -int((9 + 1) / 2)],
                "SF_LL_y": np.zeros(40),
                "x-diffs": np.linspace(0, 9**2, 9**2)[:40],
                "y-diffs": np.linspace(0, 9**2, 9**2)[:40],
            },
        ),
        # Test 9: boundary is 'Periodic' raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "LLL", "LL", "LTT"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            "Periodic",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 10: grid type is 'non-uniform' raises ValueError
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
            "non-uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 11: sf_type is empty raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            [],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 12: sf_type is list with integer values raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            [1],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 13: sf_type is an integer raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            1,  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 14: sf_type is a string raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            "ASF_V",  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 15: scalar is not None and sf_type does not include "LSS" or "ASF_S"
        # raises ValueError
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            np.arange(10),  # scalar
            ["LLL", "LL", "LTT"],  # sf_type
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            ValueError,
        ),
        # Test 16: linear velocities all SFs yes scalar non-periodic uniform grid
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "ASF_S", "LLL", "LL", "LTT", "LSS"],  # sf_type
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": (5 / 4) * np.linspace(0, 8, 9) ** 2,
                "SF_advection_velocity_y": 0 * np.linspace(0, 8, 9),
                "SF_advection_scalar_x": (1 / 4) * np.linspace(0, 8, 9) ** 2,
                "SF_advection_scalar_y": 0 * np.linspace(0, 8, 9),
                "SF_LLL_x": np.linspace(0, 8, 9) ** 3,
                "SF_LLL_y": 0 * np.linspace(0, 8, 9),
                "SF_LTT_x": (1 / 4) * np.linspace(0, 8, 9) ** 3,
                "SF_LTT_y": 0 * np.linspace(0, 8, 9),
                "SF_LL_x": np.linspace(0, 8, 9) ** 2,
                "SF_LL_y": 0 * np.linspace(0, 8, 9),
                "SF_LSS_x": (1 / 4) * np.linspace(0, 8, 9) ** 3,
                "SF_LSS_y": 0 * np.linspace(0, 8, 9),
                "x-diffs": np.linspace(0, 8, 9),
                "y-diffs": np.linspace(0, 8, 9),
            },
        ),
        # Test 17: linear velocities all SFs yes scalar non-periodic uniform grid with
        # nbins 1
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "ASF_S", "LLL", "LL", "LTT", "LSS"],  # sf_type
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            1,  # nbins
            {
                "SF_advection_velocity_x": np.mean((5 / 4) * np.linspace(0, 8, 9) ** 2),
                "SF_advection_velocity_y": np.mean(0 * np.linspace(0, 8, 9)),
                "SF_advection_scalar_x": np.mean((1 / 4) * np.linspace(0, 8, 9) ** 2),
                "SF_advection_scalar_y": np.mean(0 * np.linspace(0, 8, 9)),
                "SF_LLL_x": np.mean(np.linspace(0, 8, 9) ** 3),
                "SF_LLL_y": np.mean(0 * np.linspace(0, 8, 9)),
                "SF_LTT_x": np.mean((1 / 4) * np.linspace(0, 8, 9) ** 3),
                "SF_LTT_y": np.mean(0 * np.linspace(0, 8, 9)),
                "SF_LL_x": np.mean(np.linspace(0, 8, 9) ** 2),
                "SF_LL_y": np.mean(0 * np.linspace(0, 8, 9)),
                "SF_LSS_x": np.mean((1 / 4) * np.linspace(0, 8, 9) ** 3),
                "SF_LSS_y": np.mean(0 * np.linspace(0, 8, 9)),
                "x-diffs": np.mean(np.linspace(0, 8, 9)),
                "y-diffs": np.mean(np.linspace(0, 8, 9)),
            },
        ),
        # Test 18: slanted velocities no scalar periodic-x uniform grid only LL
        # arange(10)
        (
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # u
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)),  # v
            np.linspace(0, 10**2, 10**2),  # x
            np.linspace(0, 10**2, 10**2),  # y
            ["LL"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            "periodic-x",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_LL_x": np.tile(
                    np.concatenate(
                        (
                            np.asarray((10 / 2) ** 2 - np.arange(int(10 / 2) + 1) ** 2)[
                                ::-1
                            ],
                            np.asarray((10 / 2) ** 2 - np.arange(int(10 / 2) + 1) ** 2)[
                                1:-1
                            ],
                        )
                    ),
                    int(10 / 2),
                ),
                "SF_LL_y": np.zeros(99),
                "x-diffs": np.linspace(0, 10**2, 10**2)[:50],
                "y-diffs": np.linspace(0, 10**2, 10**2)[:99],
            },
        ),
        # Test 19: slanted velocities no scalar periodic-y uniform grid only LL
        # arange(10) tilted in x
        (
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)).T,  # u
            np.tile(np.tile(np.arange(10), 10), (10**2, 1)).T,  # v
            np.linspace(0, 10**2, 10**2),  # x
            np.linspace(0, 10**2, 10**2),  # y
            ["LL"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            "periodic-y",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_LL_y": np.tile(
                    np.concatenate(
                        (
                            np.asarray((10 / 2) ** 2 - np.arange(int(10 / 2) + 1) ** 2)[
                                ::-1
                            ],
                            np.asarray((10 / 2) ** 2 - np.arange(int(10 / 2) + 1) ** 2)[
                                1:-1
                            ],
                        )
                    ),
                    int(10 / 2),
                ),
                "SF_LL_x": np.zeros(99),
                "x-diffs": np.linspace(0, 10**2, 10**2)[:99],
                "y-diffs": np.linspace(0, 10**2, 10**2)[:50],
            },
        ),
        # Test 20: linear velocities all SFs yes scalar non-periodic uniform grid and
        # only ASF_S for scalar SFs
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "ASF_S", "LLL", "LL", "LTT"],  # sf_type
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # scalar
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": (5 / 4) * np.linspace(0, 8, 9) ** 2,
                "SF_advection_velocity_y": 0 * np.linspace(0, 8, 9),
                "SF_advection_scalar_x": (1 / 4) * np.linspace(0, 8, 9) ** 2,
                "SF_advection_scalar_y": 0 * np.linspace(0, 8, 9),
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
        # Test 21: linear velocities all SFs yes scalar non-periodic uniform grid and
        # only LSS for scalar SFs
        (
            np.meshgrid(np.arange(10), np.arange(10))[0],  # u
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # v
            np.arange(10),  # x
            np.arange(10),  # y
            ["ASF_V", "LLL", "LL", "LTT", "LSS"],  # sf_type
            0.5 * np.meshgrid(np.arange(10), np.arange(10))[0],  # scalar
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
                "SF_LSS_x": (1 / 4) * np.linspace(0, 8, 9) ** 3,
                "SF_LSS_y": 0 * np.linspace(0, 8, 9),
                "x-diffs": np.linspace(0, 8, 9),
                "y-diffs": np.linspace(0, 8, 9),
            },
        ),
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
            generate_structure_functions_2d(
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
        output_dict = generate_structure_functions_2d(
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
                    raise AssertionError(
                        f"Output dict value for key '{key}' does not match "
                        f"expected value '{output_dict[key]}'."
                    )
            else:
                raise AssertionError(f"Output dict does not contain key '{key}'.")
