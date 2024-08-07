import numpy as np
import pytest
from fluidsf.generate_sf_maps_2d import generate_sf_maps_2d


@pytest.mark.parametrize(
    "u, v, x, y, sf_type, scalar, dx, dy, grid_type, expected_sf_maps",
    [
        # Test 1: Test case with all zeros
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            ["ASF_V", "ASF_S", "LLL", "LTT", "LSS", "LL", "TT", "SS"],  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            {
                "SF_advection_velocity_xy": np.zeros((5, 10)),
                "SF_advection_scalar_xy": np.zeros((5, 10)),
                "SF_LL_xy": np.where(
                    np.arange(50).reshape(5, 10) == 5, np.nan, np.zeros((5, 10))
                ),
                "SF_TT_xy": np.where(
                    np.arange(50).reshape(5, 10) == 5, np.nan, np.zeros((5, 10))
                ),
                "SF_SS_xy": np.zeros((5, 10)),
                "SF_LLL_xy": np.where(
                    np.arange(50).reshape(5, 10) == 5, np.nan, np.zeros((5, 10))
                ),
                "SF_LTT_xy": np.where(
                    np.arange(50).reshape(5, 10) == 5, np.nan, np.zeros((5, 10))
                ),
                "SF_LSS_xy": np.where(
                    np.arange(50).reshape(5, 10) == 5, np.nan, np.zeros((5, 10))
                ),
                "separation_distances": np.sqrt(
                    np.tile(np.arange(5).reshape(5, 1), (1, 10)) ** 2
                    + np.tile(np.concatenate((np.arange(-5, 0), np.arange(5))), (5, 1))
                    ** 2
                ),
                "separation_angles": np.concatenate(
                    (
                        (
                            np.sign(np.concatenate((np.arange(-5, 0), np.arange(5))))
                            * np.pi
                            / 2
                        ).reshape(1, -1),
                        np.arctan(
                            np.tile(
                                np.concatenate((np.arange(-5, 0), np.arange(5))), (5, 1)
                            )[:4]
                            / np.tile(np.arange(5).reshape(5, 1), (1, 10))[1:]
                        ),
                    ),
                    axis=0,
                ),
                "x_separations": np.tile(np.arange(5).reshape(5, 1), (1, 10)),
                "y_separations": np.tile(
                    np.concatenate((np.arange(-5, 0), np.arange(5))), (5, 1)
                ),
            },  # expected_sf_maps
        ),
        # Test 2: sf_type not a list raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            None,  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            ValueError,  # expected_sf_maps
        ),
        # Test 3: sf_type is an empty list raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            [],  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            ValueError,  # expected_sf_maps
        ),
        # Test 4: sf_type contains integers raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            [1, 2, 3],  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            ValueError,  # expected_sf_maps
        ),
        # Test 5: sf_type contains strings not in ["ASF_V", "ASF_S", "LLL", "LTT",
        # "LSS", "LL", "TT", "SS"] raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            ["Q"],  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            ValueError,  # expected_sf_maps
        ),
        # Test 6: grid_type is not "uniform" raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            ["ASF_V", "ASF_S", "LLL", "LTT", "LSS", "LL", "TT", "SS"],  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "latlon",  # grid_type
            ValueError,  # expected_sf_maps
        ),
        # Test 7: scalar is None and "ASF_S" in sf_type raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            ["ASF_S"],  # sf_type
            None,  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            ValueError,  # expected_sf_maps
        ),
        # Test 8: scalar is not None and sf_type does not include "ASF_S" and "SS" and
        # "LSS" raises ValueError
        (
            np.zeros((10, 10)),  # u
            np.zeros((10, 10)),  # v
            np.linspace(1, 10, 10),  # x
            np.linspace(1, 10, 10),  # y
            ["ASF_V", "LLL", "LTT", "LL", "TT"],  # sf_type
            np.zeros((10, 10)),  # scalar
            None,  # dx
            None,  # dy
            "uniform",  # grid_type
            ValueError,  # expected_sf_maps
        ),
    ],
)
def test_generate_sf_maps_2d_parameterized(
    u, v, x, y, sf_type, scalar, dx, dy, grid_type, expected_sf_maps
):
    if expected_sf_maps == ValueError:
        with pytest.raises(ValueError):
            generate_sf_maps_2d(
                u,
                v,
                x,
                y,
                sf_type,
                scalar,
                dx,
                dy,
                grid_type,
            )
        return
    else:
        output_sf_maps = generate_sf_maps_2d(
            u,
            v,
            x,
            y,
            sf_type,
            scalar,
            dx,
            dy,
            grid_type,
        )

        for key, value in expected_sf_maps.items():
            if key in output_sf_maps:
                if not np.allclose(output_sf_maps[key], value, equal_nan=True):
                    print(output_sf_maps[key])
                    print(expected_sf_maps[key])
                    raise AssertionError(
                        f"Output dict value for key '{key}' does not match "
                        f"expected value '{output_sf_maps[key]}'."
                    )

            else:
                raise AssertionError(f"Output dict does not contain key '{key}'.")
