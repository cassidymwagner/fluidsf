import numpy as np
import pytest

from oceans_sf.advection_velocity import advection_velocity


@pytest.mark.parametrize(
    "u, v, x, y, dx, dy, boundary, even, grid_type, nbins, expected_result",
    [
        (
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]),
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,
            np.linspace(1, 10, 10),
            np.linspace(1, 10, 10),
            None,
            None,
            "Periodic",
            True,
            "uniform",
            10,
            {
                "SF_zonal": np.array([0, 945, 1680, 2205, 2520]),
                "SF_meridional": np.array([0, 94500, 168000, 220500, 252000]),
                "x-diffs": np.array([0, 1, 2, 3, 4]),
                "y-diffs": np.array([0, 1, 2, 3, 4]),
            },
        ),
        (
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]),
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,
            np.linspace(1, 10, 10),
            np.linspace(1, 10, 10),
            None,
            None,
            None,
            True,
            "uniform",
            10,
            {
                "SF_zonal": np.array([0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]),
                "SF_meridional": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
                ),
                "x-diffs": np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]),
                "y-diffs": np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]),
            },
        ),
        (
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]),
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,
            np.linspace(1, 10, 10),
            np.linspace(1, 10, 10),
            np.ones(10),
            np.ones(10),
            "Periodic",
            True,
            "latlon",
            10,
            {
                "SF_zonal": np.array([0, 945, 1680, 2205, 2520]),
                "SF_meridional": np.array([0, 94500, 168000, 220500, 252000]),
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
            },
        ),
        (
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)]),
            np.array([[i + 1 for i in range(j * 10, (j + 1) * 10)] for j in range(10)])
            * 2,
            np.linspace(1, 10, 10),
            np.linspace(1, 10, 10),
            np.ones(10),
            np.ones(10),
            None,
            True,
            "latlon",
            10,
            {
                "SF_zonal": np.array([0, 105, 420, 945, 1680, 2625, 3780, 5145, 6720]),
                "SF_meridional": np.array(
                    [0, 10500, 42000, 94500, 168000, 262500, 378000, 514500, 672000]
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
            },
        ),
    ],
)
def test_advection_velocity(
    u, v, x, y, dx, dy, boundary, even, grid_type, nbins, expected_result
):
    result = advection_velocity(u, v, x, y, dx, dy, boundary, even, grid_type, nbins)
    np.testing.assert_allclose(result["SF_zonal"], expected_result["SF_zonal"])
    np.testing.assert_allclose(
        result["SF_meridional"], expected_result["SF_meridional"]
    )
    np.testing.assert_allclose(result["x-diffs"], expected_result["x-diffs"])
    np.testing.assert_allclose(result["y-diffs"], expected_result["y-diffs"])
