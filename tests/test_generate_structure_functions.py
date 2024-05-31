import numpy as np
import pytest

from oceans_sf.generate_structure_functions import generate_structure_functions


@pytest.mark.parametrize(
    "u, v, x, y, skip_velocity_sf, scalar, traditional_type, dx, dy, boundary, "
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
            ["LLL", "LSS", "LTT"],  # traditional_type
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": np.array(
                    [0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]
                ),
                "SF_advection_velocity_y": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
                ),
                "SF_advection_scalar_x": np.array(
                    [0, 189, 756, 1701, 3024, 4725, 6804, 9261, 12096]
                ),
                "SF_advection_scalar_y": np.array(
                    [0, 18900, 75600, 170100, 302400, 472500, 680400, 926100, 1209600]
                ),
                "SF_LLL_x": np.array([0, -1, -8, -27, -64, -125, -216, -343, -512]),
                "SF_LLL_y": np.array(
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
                "SF_LTT_x": np.array(
                    [0, -4, -32, -108, -256, -500, -864, -1372, -2048]
                ),
                "SF_LTT_y": np.array(
                    [
                        0,
                        -2000,
                        -16000,
                        -54000,
                        -128000,
                        -250000,
                        -432000,
                        -686000,
                        -1024000,
                    ]
                ),
                "SF_LSS_x": np.array(
                    [0, -9, -72, -243, -576, -1125, -1944, -3087, -4608]
                ),
                "SF_LSS_y": np.array(
                    [
                        0,
                        -9000,
                        -72000,
                        -243000,
                        -576000,
                        -1125000,
                        -1944000,
                        -3087000,
                        -4608000,
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
            ["LLL", "LSS", "LTT"],  # traditional_order
            None,  # dx
            None,  # dy
            "periodic-all",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": np.array([0, 945, 1680, 2205, 2520]),
                "SF_advection_velocity_y": np.array([0, 94500, 168000, 220500, 252000]),
                "SF_advection_scalar_x": np.array([0, 1701, 3024, 3969, 4536]),
                "SF_advection_scalar_y": np.array([0, 170100, 302400, 396900, 453600]),
                "SF_LLL_x": np.array([0, 72, 96, 84, 48]),
                "SF_LLL_y": np.array([0, 72000, 96000, 84000, 48000]),
                "SF_LTT_x": np.array([0, 288, 384, 336, 192]),
                "SF_LTT_y": np.array([0, 144000, 192000, 168000, 96000]),
                "SF_LSS_x": np.array([0, 648, 864, 756, 432]),
                "SF_LSS_y": np.array([0, 648000, 864000, 756000, 432000]),
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
            ["LLL", "LSS", "LTT"],  # traditional_order
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            "latlon",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": np.array(
                    [0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]
                ),
                "SF_advection_velocity_y": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
                ),
                "SF_advection_scalar_x": np.array(
                    [0, 189, 756, 1701, 3024, 4725, 6804, 9261, 12096]
                ),
                "SF_advection_scalar_y": np.array(
                    [0, 18900, 75600, 170100, 302400, 472500, 680400, 926100, 1209600]
                ),
                "SF_LLL_x": np.array([0, -1, -8, -27, -64, -125, -216, -343, -512]),
                "SF_LLL_y": np.array(
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
                "SF_LTT_x": np.array(
                    [0, -4, -32, -108, -256, -500, -864, -1372, -2048]
                ),
                "SF_LTT_y": np.array(
                    [
                        0,
                        -2000,
                        -16000,
                        -54000,
                        -128000,
                        -250000,
                        -432000,
                        -686000,
                        -1024000,
                    ]
                ),
                "SF_LSS_x": np.array(
                    [0, -9, -72, -243, -576, -1125, -1944, -3087, -4608]
                ),
                "SF_LSS_y": np.array(
                    [
                        0,
                        -9000,
                        -72000,
                        -243000,
                        -576000,
                        -1125000,
                        -1944000,
                        -3087000,
                        -4608000,
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
                        222254.67962213,
                        333381.99365421,
                        444509.27673393,
                        555636.51851453,
                        666763.70862407,
                        777890.83665907,
                        889017.89217812,
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
            ["LLL", "LSS"],  # traditional_order
            np.ones(10),  # dx
            np.ones(10),  # dy
            "periodic-all",  # boundary
            "latlon",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": np.array([0, 945, 1680, 2205, 2520]),
                "SF_advection_velocity_y": np.array([0, 94500, 168000, 220500, 252000]),
                "SF_advection_scalar_x": np.array([0, 1701, 3024, 3969, 4536]),
                "SF_advection_scalar_y": np.array([0, 170100, 302400, 396900, 453600]),
                "SF_LLL_x": np.array([0, 72, 96, 84, 48]),
                "SF_LLL_y": np.array([0, 72000, 96000, 84000, 48000]),
                "SF_LSS_x": np.array([0, 648, 864, 756, 432]),
                "SF_LSS_y": np.array([0, 648000, 864000, 756000, 432000]),
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
                        222254.67962213,
                        333381.99365421,
                        444509.27673393,
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
            ["LLL", "LSS"],  # traditional_order
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            3,  # nbins
            {
                "SF_advection_velocity_x": np.array([175, 1750, 5215]),
                "SF_advection_velocity_y": np.array([17500, 175000, 521500]),
                "SF_advection_scalar_x": np.array([315, 3150, 9387]),
                "SF_advection_scalar_y": np.array([31500, 315000, 938700]),
                "SF_LLL_x": np.array([-3, -72, -357]),
                "SF_LLL_y": np.array([-3000, -72000, -357000]),
                "SF_LSS_x": np.array([-27, -648, -3213]),
                "SF_LSS_y": np.array([-27000, -648000, -3213000]),
                "x-diffs": np.array([1, 4, 7]),
                "y-diffs": np.array([1, 4, 7]),
            },  # expected_dict
        ),
        # Test 6: all with no boundary and latlon grid and binning
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
            ["LLL", "LSS"],  # traditional_order
            np.ones(10),  # dx
            np.ones(10),  # dy
            None,  # boundary
            "latlon",  # grid_type
            3,  # nbins
            {
                "SF_advection_velocity_x": np.array([175, 1750, 5215]),
                "SF_advection_velocity_y": np.array([17500, 175000, 521500]),
                "SF_advection_scalar_x": np.array([315, 3150, 9387]),
                "SF_advection_scalar_y": np.array([31500, 315000, 938700]),
                "SF_LLL_x": np.array([-3, -72, -357]),
                "SF_LLL_y": np.array([-3000, -72000, -357000]),
                "SF_LSS_x": np.array([-27, -648, -3213]),
                "SF_LSS_y": np.array(
                    [
                        -27000,
                        -648000,
                        -3213000,
                    ]
                ),
                "x-diffs": np.array(
                    [111195.08372419, 444780.33489677, 778365.58606934]
                ),
                "y-diffs": np.array(
                    [111127.34152924, 444509.26296756, 777890.81248708]
                ),
            },  # expected_dict
        ),
        # Test 7: all with no boundary and 5 bins
        (
            np.array(
                [[i + 1 for i in range(j * 5, (j + 1) * 5)] for j in range(10)]
            ),  # u
            np.array([[i + 1 for i in range(j * 5, (j + 1) * 5)] for j in range(10)])
            * 2,  # v
            np.linspace(1, 5, 5),  # x
            np.linspace(1, 10, 10),  # y
            False,  # skip_velocity_sf
            np.array([[i + 1 for i in range(j * 5, (j + 1) * 5)] for j in range(10)])
            * 3,  # scalar
            ["LLL", "LSS"],  # traditional_order
            None,  # dx
            None,  # dy
            None,  # boundary
            "uniform",  # grid_type
            5,  # nbins
            {
                "SF_advection_velocity_x": np.array([0, 55, 220, 495]),
                "SF_advection_velocity_y": np.array(
                    [687.5, 8937.5, 22000, 41937.5, 77687.5]
                ),
                "SF_advection_scalar_x": np.array([0, 99, 396, 891]),
                "SF_advection_scalar_y": np.array(
                    [1237.5, 16087.5, 39600.0, 75487.5, 139837.5]
                ),
                "SF_LLL_x": np.array([0, -1, -8, -27]),
                "SF_LLL_y": np.array([-62.5, -2187.5, -8000.0, -21312.5, -53437.5]),
                "SF_LSS_x": np.array([0, -9, -72, -243]),
                "SF_LSS_y": np.array([-562.5, -19687.5, -72000, -191812.5, -480937.5]),
                "x-diffs": np.linspace(0, 3, 4),
                "y-diffs": np.array([0.5, 2.5, 4, 5.5, 7.5]),
            },  # expected_dict
        ),
        # Test 8: all with periodic-x boundary
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
            ["LLL", "LSS"],  # traditional_order
            None,  # dx
            None,  # dy
            "periodic-x",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": np.array([0, 945, 1680, 2205, 2520]),
                "SF_advection_velocity_y": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
                ),
                "SF_advection_scalar_x": np.array([0, 1701, 3024, 3969, 4536]),
                "SF_advection_scalar_y": np.array(
                    [0, 18900, 75600, 170100, 302400, 472500, 680400, 926100, 1209600]
                ),
                "SF_LLL_x": np.array([0, 72, 96, 84, 48]),
                "SF_LLL_y": np.array(
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
                "SF_LSS_x": np.array([0, 648, 864, 756, 432]),
                "SF_LSS_y": np.array(
                    [
                        0,
                        -9000,
                        -72000,
                        -243000,
                        -576000,
                        -1125000,
                        -1944000,
                        -3087000,
                        -4608000,
                    ]
                ),
                "x-diffs": np.linspace(0, 4, 5),
                "y-diffs": np.linspace(0, 8, 9),
            },  # expected_dict
        ),
        # Test 9: all with periodic-y boundary
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
            ["LLL", "LSS"],  # traditional_order
            None,  # dx
            None,  # dy
            "periodic-y",  # boundary
            "uniform",  # grid_type
            None,  # nbins
            {
                "SF_advection_velocity_x": np.array(
                    [0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]
                ),
                "SF_advection_velocity_y": np.array([0, 94500, 168000, 220500, 252000]),
                "SF_advection_scalar_x": np.array(
                    [0, 189, 756, 1701, 3024, 4725, 6804, 9261, 12096]
                ),
                "SF_advection_scalar_y": np.array([0, 170100, 302400, 396900, 453600]),
                "SF_LLL_x": np.array([0, -1, -8, -27, -64, -125, -216, -343, -512]),
                "SF_LLL_y": np.array([0, 72000, 96000, 84000, 48000]),
                "SF_LSS_x": np.array(
                    [0, -9, -72, -243, -576, -1125, -1944, -3087, -4608]
                ),
                "SF_LSS_y": np.array([0, 648000, 864000, 756000, 432000]),
                "x-diffs": np.linspace(0, 8, 9),
                "y-diffs": np.linspace(0, 4, 5),
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
            if not np.allclose(output_dict[key], value):
                print(output_dict[key])
                print(expected_dict[key])
                raise AssertionError(
                    f"Output dict value for key '{key}' does not match "
                    f"expected value '{output_dict[key]}'."
                )
        else:
            raise AssertionError(f"Output dict does not contain key '{key}'.")
