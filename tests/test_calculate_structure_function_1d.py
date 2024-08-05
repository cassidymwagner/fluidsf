from unittest import TestCase

import numpy as np
import pytest
from fluidsf.calculate_structure_function_1d import calculate_structure_function_1d


@pytest.mark.parametrize(
    "u, sep_id, sf_type, v, scalar, boundary, expected_result",
    [
        # Test 1: all traditional structure functions
        (
            np.array([1, 2, 3, 4]),  # u
            1,  # sep_id
            ["LL", "LLL", "LTT", "LSS"],  # sf_type
            np.array([2, 4, 6, 8]),  # v
            np.array([3, 6, 9, 12]),  # scalar
            None,  # boundary
            {
                "SF_LL": 1,
                "SF_LLL": 1,
                "SF_LTT": 4,
                "SF_LSS": 9,
            },
            # expected_result
        ),
        # Test 2: all traditional structure functions and periodic boundary
        (
            np.array([1, 2, 3, 2]),  # u
            1,  # sep_id
            ["LL", "LLL", "LTT", "LSS"],  # sf_type
            np.array([2, 4, 6, 4]),  # v
            np.array([3, 6, 9, 6]),  # scalar
            "Periodic",  # boundary
            {
                "SF_LL": 1,
                "SF_LLL": 0,
                "SF_LTT": 0,
                "SF_LSS": 0,
            },
            # expected_result
        ),
    ],
)
def test_calculate_structure_function_1d_parameterized(
    u, sep_id, sf_type, v, scalar, boundary, expected_result
):
    output_dict = calculate_structure_function_1d(
        u, sep_id, sf_type, v, scalar, boundary
    )

    TestCase().assertDictEqual(output_dict, expected_result)
