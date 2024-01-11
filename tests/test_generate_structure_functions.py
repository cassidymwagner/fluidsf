import numpy as np
import pytest

from oceans_sf.generate_structure_functions import generate_structure_functions


@pytest.mark.parametrize(
    "u, v, x, y, skip_velocity_sf, scalar, traditional_order, dx, dy, boundary, even, "
    "grid_type, nbins, expected_dict",
    [
        # Test 1: all with no boundary and uniform grid
        (
            np.array(
                [[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 3,  # scalar
            3,  # traditional_order
            None,  # dx
            None,  # dy
            None,  # boundary
            True,  # even
            "uniform",  # grid_type
            10,  # nbins
            {
                "SF_advection_velocity_zonal": np.array(
                    [0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]
                ),
                "SF_advection_velocity_meridional": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
                ),
                "SF_advection_scalar_zonal": np.array(
                    [0, 189, 756, 1701, 3024, 4725, 6804, 9261, 12096]
                ),
                "SF_advection_scalar_meridional": np.array(
                    [0, 18900, 75600, 170100, 302400, 472500, 680400, 926100, 1209600]
                ),
                "SF_traditional_velocity_zonal": np.array(
                    [0, -1, -8, -27, -64, -125, -216, -343, -512]
                ),
                "SF_traditional_velocity_meridional": np.array(
                    [
                        0,
                        -1000,
                        -8000,
                        -27000,
                        -64000,
                        -125000,
                        -216000,
                        -343000,
                        -512000,
                    ]
                ),
                "SF_traditional_scalar_zonal": np.array(
                    [0, -27, -216, -729, -1728, -3375, -5832, -9261, -13824]
                ),
                "SF_traditional_scalar_meridional": np.array(
                    [
                        0,
                        -27000,
                        -216000,
                        -729000,
                        -1728000,
                        -3375000,
                        -5832000,
                        -9261000,
                        -13824000,
                    ]
                ),
                "x-diffs": np.linspace(0, 8, 9),
                "y-diffs": np.linspace(0, 8, 9),
            },  # expected_dict
        ),
        # Test 2: all with Periodic boundary and uniform grid
        (
            np.array(
                [[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 3,  # scalar
            3,  # traditional_order
            None,  # dx
            None,  # dy
            "Periodic",  # boundary
            True,  # even
            "uniform",  # grid_type
            10,  # nbins
            {
                "SF_advection_velocity_zonal": np.array([0, 945, 1680, 2205, 2520]),
                "SF_advection_velocity_meridional": np.array(
                    [0, 94500, 168000, 220500, 252000]
                ),
                "SF_advection_scalar_zonal": np.array([0, 1701, 3024, 3969, 4536]),
                "SF_advection_scalar_meridional": np.array(
                    [0, 170100, 302400, 396900, 453600]
                ),
                "SF_traditional_velocity_zonal": np.array([0, 72, 96, 84, 48]),
                "SF_traditional_velocity_meridional": np.array(
                    [0, 72000, 96000, 84000, 48000]
                ),
                "SF_traditional_scalar_zonal": np.array([0, 1944, 2592, 2268, 1296]),
                "SF_traditional_scalar_meridional": np.array(
                    [0, 1944000, 2592000, 2268000, 1296000]
                ),
                "x-diffs": np.linspace(0, 4, 5),
                "y-diffs": np.linspace(0, 4, 5),
            },  # expected_dict
        ),
        # Test 3: all with no boundary and latlon grid
        (
            np.array(
                [[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 3,  # scalar
            3,  # traditional_order
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            True,  # even
            "latlon",  # grid_type
            10,  # nbins
            {
                "SF_advection_velocity_zonal": np.array(
                    [0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]
                ),
                "SF_advection_velocity_meridional": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
                ),
                "SF_advection_scalar_zonal": np.array(
                    [0, 189, 756, 1701, 3024, 4725, 6804, 9261, 12096]
                ),
                "SF_advection_scalar_meridional": np.array(
                    [0, 18900, 75600, 170100, 302400, 472500, 680400, 926100, 1209600]
                ),
                "SF_traditional_velocity_zonal": np.array(
                    [0, -1, -8, -27, -64, -125, -216, -343, -512]
                ),
                "SF_traditional_velocity_meridional": np.array(
                    [
                        0,
                        -1000,
                        -8000,
                        -27000,
                        -64000,
                        -125000,
                        -216000,
                        -343000,
                        -512000,
                    ]
                ),
                "SF_traditional_scalar_zonal": np.array(
                    [0, -27, -216, -729, -1728, -3375, -5832, -9261, -13824]
                ),
                "SF_traditional_scalar_meridional": np.array(
                    [
                        0,
                        -27000,
                        -216000,
                        -729000,
                        -1728000,
                        -3375000,
                        -5832000,
                        -9261000,
                        -13824000,
                    ]
                ),
                "x-diffs": np.array(
                    [
                        0.0,
                        111195.08372419,
                        222390.16744838,
                        333585.25117257,
                        444780.33489677,
                        555975.41862096,
                        667170.50234515,
                        778365.58606934,
                        889560.66979353,
                    ]
                ),
                "y-diffs": np.array(
                    [
                        0.0,
                        111127.34496561,
                        222085.35856591,
                        332772.46924562,
                        443087.12759851,
                        552927.80866002,
                        662193.01584979,
                        770781.28701475,
                        878591.20301767,
                    ]
                ),
            },  # expected_dict
        ),
        # Test 4: all with Periodic boundary and latlon grid
        (
            np.array(
                [[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 3,  # scalar
            3,  # traditional_order
            np.ones(10),  # dx
            np.ones(10),  # dy
            "Periodic",  # boundary
            True,  # even
            "latlon",  # grid_type
            10,  # nbins
            {
                "SF_advection_velocity_zonal": np.array([0, 945, 1680, 2205, 2520]),
                "SF_advection_velocity_meridional": np.array(
                    [0, 94500, 168000, 220500, 252000]
                ),
                "SF_advection_scalar_zonal": np.array([0, 1701, 3024, 3969, 4536]),
                "SF_advection_scalar_meridional": np.array(
                    [0, 170100, 302400, 396900, 453600]
                ),
                "SF_traditional_velocity_zonal": np.array([0, 72, 96, 84, 48]),
                "SF_traditional_velocity_meridional": np.array(
                    [0, 72000, 96000, 84000, 48000]
                ),
                "SF_traditional_scalar_zonal": np.array([0, 1944, 2592, 2268, 1296]),
                "SF_traditional_scalar_meridional": np.array(
                    [0, 1944000, 2592000, 2268000, 1296000]
                ),
                "x-diffs": np.array(
                    [
                        0.0,
                        111195.08372419,
                        222390.16744838,
                        333585.25117257,
                        444780.33489677,
                    ]
                ),
                "y-diffs": np.array(
                    [
                        0.0,
                        111127.34496561,
                        222085.35856591,
                        332772.46924562,
                        443087.12759851,
                    ]
                ),
            },  # expected_dict
        ),
        # Test 5: all with no boundary and uniform grid and binning
        (
            np.array(
                [[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 3,  # scalar
            3,  # traditional_order
            None,  # dx
            None,  # dy
            None,  # boundary
            False,  # even
            "uniform",  # grid_type
            3,  # nbins
            {
                "SF_advection_velocity_zonal": np.array([175, 1750, 5215]),
                "SF_advection_velocity_meridional": np.array([17500, 175000, 521500]),
                "SF_advection_scalar_zonal": np.array([315, 3150, 9387]),
                "SF_advection_scalar_meridional": np.array([31500, 315000, 938700]),
                "SF_traditional_velocity_zonal": np.array([-3, -72, -357]),
                "SF_traditional_velocity_meridional": np.array(
                    [-3000, -72000, -357000]
                ),
                "SF_traditional_scalar_zonal": np.array([-81, -1944, -9639]),
                "SF_traditional_scalar_meridional": np.array(
                    [
                        -81000,
                        -1944000,
                        -9639000,
                    ]
                ),
                "x-diffs": np.array([1, 4, 7]),
                "y-diffs": np.array([1, 4, 7]),
            },  # expected_dict
        ),
        # Test 5: all with no boundary and latlon grid and binning
        (
            np.array(
                [[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 3,  # scalar
            3,  # traditional_order
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            False,  # even
            "latlon",  # grid_type
            3,  # nbins
            {
                "SF_advection_velocity_zonal": np.array([175, 1750, 5215]),
                "SF_advection_velocity_meridional": np.array([17500, 175000, 521500]),
                "SF_advection_scalar_zonal": np.array([315, 3150, 9387]),
                "SF_advection_scalar_meridional": np.array([31500, 315000, 938700]),
                "SF_traditional_velocity_zonal": np.array([-3, -72, -357]),
                "SF_traditional_velocity_meridional": np.array(
                    [-3000, -72000, -357000]
                ),
                "SF_traditional_scalar_zonal": np.array([-81, -1944, -9639]),
                "SF_traditional_scalar_meridional": np.array(
                    [
                        -81000,
                        -1944000,
                        -9639000,
                    ]
                ),
                "x-diffs": np.array(
                    [111195.08372419, 444780.33489677, 778365.58606934]
                ),
                "y-diffs": np.array(
                    [111070.90117717, 442929.13516805, 770521.83529407]
                ),
            },  # expected_dict
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
    traditional_order,
    dx,
    dy,
    boundary,
    even,
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
        traditional_order,
        dx,
        dy,
        boundary,
        even,
        grid_type,
        nbins,
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
