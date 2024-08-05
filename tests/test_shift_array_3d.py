import numpy as np
import pytest
from fluidsf.shift_array_3d import shift_array_3d


@pytest.mark.parametrize(
    "input_array, shift_x, shift_y, shift_z, boundary, expected_shifted_x_array, \
        expected_shifted_y_array, expected_shifted_z_array",
    [
        # Test shifting 3D array in all directions by 1 with no boundary conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            None,
            np.array(
                [
                    [
                        [2, 3, np.nan],
                        [5, 6, np.nan],
                        [8, 9, np.nan],
                    ],
                    [
                        [11, 12, np.nan],
                        [14, 15, np.nan],
                        [17, 18, np.nan],
                    ],
                    [
                        [20, 21, np.nan],
                        [23, 24, np.nan],
                        [26, 27, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 2 with no boundary conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            2,
            2,
            2,
            None,
            np.array(
                [
                    [
                        [3, np.nan, np.nan],
                        [6, np.nan, np.nan],
                        [9, np.nan, np.nan],
                    ],
                    [
                        [12, np.nan, np.nan],
                        [15, np.nan, np.nan],
                        [18, np.nan, np.nan],
                    ],
                    [
                        [21, np.nan, np.nan],
                        [24, np.nan, np.nan],
                        [27, np.nan, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [7, 8, 9],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [16, 17, 18],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [25, 26, 27],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic boundary
        # conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            "periodic-all",
            np.array(
                [
                    [
                        [2, 3, 1],
                        [5, 6, 4],
                        [8, 9, 7],
                    ],
                    [
                        [11, 12, 10],
                        [14, 15, 13],
                        [17, 18, 16],
                    ],
                    [
                        [20, 21, 19],
                        [23, 24, 22],
                        [26, 27, 25],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 2, 3],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [10, 11, 12],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [19, 20, 21],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 2 with periodic boundary
        # conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            2,
            2,
            2,
            "periodic-all",
            np.array(
                [
                    [
                        [3, 1, 2],
                        [6, 4, 5],
                        [9, 7, 8],
                    ],
                    [
                        [12, 10, 11],
                        [15, 13, 14],
                        [18, 16, 17],
                    ],
                    [
                        [21, 19, 20],
                        [24, 22, 23],
                        [27, 25, 26],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [7, 8, 9],
                        [1, 2, 3],
                        [4, 5, 6],
                    ],
                    [
                        [16, 17, 18],
                        [10, 11, 12],
                        [13, 14, 15],
                    ],
                    [
                        [25, 26, 27],
                        [19, 20, 21],
                        [22, 23, 24],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-x boundary
        # conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-x"],
            np.array(
                [
                    [
                        [2, 3, 1],
                        [5, 6, 4],
                        [8, 9, 7],
                    ],
                    [
                        [11, 12, 10],
                        [14, 15, 13],
                        [17, 18, 16],
                    ],
                    [
                        [20, 21, 19],
                        [23, 24, 22],
                        [26, 27, 25],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-y boundary
        # conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-y"],
            np.array(
                [
                    [
                        [2, 3, np.nan],
                        [5, 6, np.nan],
                        [8, 9, np.nan],
                    ],
                    [
                        [11, 12, np.nan],
                        [14, 15, np.nan],
                        [17, 18, np.nan],
                    ],
                    [
                        [20, 21, np.nan],
                        [23, 24, np.nan],
                        [26, 27, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 2, 3],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [10, 11, 12],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [19, 20, 21],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-z boundary
        # conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-z"],
            np.array(
                [
                    [
                        [2, 3, np.nan],
                        [5, 6, np.nan],
                        [8, 9, np.nan],
                    ],
                    [
                        [11, 12, np.nan],
                        [14, 15, np.nan],
                        [17, 18, np.nan],
                    ],
                    [
                        [20, 21, np.nan],
                        [23, 24, np.nan],
                        [26, 27, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-x and periodic-y
        # boundary conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-x", "periodic-y"],
            np.array(
                [
                    [
                        [2, 3, 1],
                        [5, 6, 4],
                        [8, 9, 7],
                    ],
                    [
                        [11, 12, 10],
                        [14, 15, 13],
                        [17, 18, 16],
                    ],
                    [
                        [20, 21, 19],
                        [23, 24, 22],
                        [26, 27, 25],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 2, 3],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [10, 11, 12],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [19, 20, 21],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-x and periodic-z
        # boundary conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-x", "periodic-z"],
            np.array(
                [
                    [
                        [2, 3, 1],
                        [5, 6, 4],
                        [8, 9, 7],
                    ],
                    [
                        [11, 12, 10],
                        [14, 15, 13],
                        [17, 18, 16],
                    ],
                    [
                        [20, 21, 19],
                        [23, 24, 22],
                        [26, 27, 25],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [np.nan, np.nan, np.nan],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [np.nan, np.nan, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-y and periodic-z
        # boundary conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-y", "periodic-z"],
            np.array(
                [
                    [
                        [2, 3, np.nan],
                        [5, 6, np.nan],
                        [8, 9, np.nan],
                    ],
                    [
                        [11, 12, np.nan],
                        [14, 15, np.nan],
                        [17, 18, np.nan],
                    ],
                    [
                        [20, 21, np.nan],
                        [23, 24, np.nan],
                        [26, 27, np.nan],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 2, 3],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [10, 11, 12],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [19, 20, 21],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                ]
            ),
        ),
        # Test shifting 3D array in all directions by 1 with periodic-x, periodic-y,
        # and periodic-z boundary conditions
        (
            np.arange(1, 28).reshape((3, 3, 3)),
            1,
            1,
            1,
            ["periodic-x", "periodic-y", "periodic-z"],
            np.array(
                [
                    [
                        [2, 3, 1],
                        [5, 6, 4],
                        [8, 9, 7],
                    ],
                    [
                        [11, 12, 10],
                        [14, 15, 13],
                        [17, 18, 16],
                    ],
                    [
                        [20, 21, 19],
                        [23, 24, 22],
                        [26, 27, 25],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 2, 3],
                    ],
                    [
                        [13, 14, 15],
                        [16, 17, 18],
                        [10, 11, 12],
                    ],
                    [
                        [22, 23, 24],
                        [25, 26, 27],
                        [19, 20, 21],
                    ],
                ]
            ),
            np.array(
                [
                    [
                        [10, 11, 12],
                        [13, 14, 15],
                        [16, 17, 18],
                    ],
                    [
                        [19, 20, 21],
                        [22, 23, 24],
                        [25, 26, 27],
                    ],
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                    ],
                ]
            ),
        ),
    ],
)
def test_shift_array_3d(
    input_array,
    shift_x,
    shift_y,
    shift_z,
    boundary,
    expected_shifted_x_array,
    expected_shifted_y_array,
    expected_shifted_z_array,
):
    shifted_x_array, shifted_y_array, shifted_z_array = shift_array_3d(
        input_array, shift_x, shift_y, shift_z, boundary
    )

    np.testing.assert_allclose(shifted_x_array, expected_shifted_x_array)
    np.testing.assert_allclose(shifted_y_array, expected_shifted_y_array)
    np.testing.assert_allclose(shifted_z_array, expected_shifted_z_array)
