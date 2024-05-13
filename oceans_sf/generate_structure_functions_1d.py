import numpy as np

from .bin_data import bin_data
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function_1d import calculate_structure_function_1d
from .shift_array1d import shift_array1d


def generate_structure_functions_1d(  # noqa: C901, D417
    u,
    v,
    x,
    y=None,
    scalar=None,
    traditional_type=["LLL"],  # noqa: B006
    dx=None,
    boundary="Periodic",
    even="True",
    grid_type="uniform",
    nbins=10,
):
    """
    Full method for generating traditional structure functions for 1D data.
    Supports velocity-based and scalar-based structure functions. Defaults to
    calculating the third-order velocity structure function ('LLL') along the
    data track.

    Parameters
    ----------
        u: ndarray
            1D array of u velocity components.
        v: ndarray
            1D array of v velocity components.
        x: ndarray
            1D array of coordinates. If you have lat-lon data, set x to 1D array of
            latitudes.
        y: ndarray, optional
            1D array of coordinates orthogonal to x. Defaults to None. If you have
            lat-lon data, set y to 1D array of longitudes.
        scalar: ndarray, optional
            1D array of scalar values. Defaults to None.
        traditional_type: list, optional
            List of traditional structure function types to calculate.
            Accepted types are: "LL", "LLL", "LTT", "LSS". Defaults to "LLL". If you
            include "LSS", you must provide a 1D array for scalar.
        dx: float, optional
            Grid spacing along the data track. Defaults to None.
        boundary: str, optional
            Boundary condition of the data. Defaults to "Periodic". Set to None if no
            boundary conditions.
        even: bool, optional
            Flag indicating if the grid is evenly spaced. Defaults to True.
        grid_type:str, optional
            Type of grid, either "uniform" or "latlon". Defaults to "uniform".
        nbins: int, optional
            Number of bins for binning the data. Defaults to 10.

    Returns
    -------
        dict:
            Dictionary containing the requested structure functions and separation
            distances along the data track.
    """
    # Error handling
    if boundary not in ["Periodic", None]:
        raise ValueError("Boundary condition must be 'Periodic' or None.")
    if grid_type not in ["uniform", "latlon"]:
        raise ValueError("Grid type must be 'uniform' or 'latlon'.")
    if grid_type == "latlon" and y is None:
        raise ValueError(
            "If grid_type is 'latlon', y must be provided."
            " Ensure x is latitude and y is longitude."
        )
    if scalar is not None and "LSS" not in traditional_type:
        raise ValueError(
            "If scalar is provided, you must include 'LSS' in traditional_type."
        )
    if scalar is None and "LSS" in traditional_type:
        raise ValueError(
            "If you include 'LSS' in traditional_type, you must provide a scalar array."
        )

    # Initialize variables as NoneType
    SF_LL = None
    SF_LLL = None
    SF_LTT = None
    SF_LSS = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    if boundary == "Periodic":
        sep = range(1, int(len(x) / 2))
    else:
        sep = range(1, int(len(x) - 1))

    # Initialize the separation distance arrays
    xd = np.zeros(len(sep) + 1)

    # Initialize the structure function arrays
    if "LL" in traditional_type:
        SF_LL = np.zeros(len(sep) + 1)
    if "LLL" in traditional_type:
        SF_LLL = np.zeros(len(sep) + 1)
    if "LTT" in traditional_type:
        SF_LTT = np.zeros(len(sep) + 1)
    if "LSS" in traditional_type:
        SF_LSS = np.zeros(len(sep) + 1)

    # Iterate over separations
    for sep_id in sep:
        if boundary == "Periodic":
            xroll = shift_array1d(x, shift_by=sep_id, boundary="Periodic")
            if y is not None:
                yroll = shift_array1d(y, shift_by=sep_id, boundary="Periodic")
        else:
            xroll = shift_array1d(x, shift_by=sep_id, boundary=None)
            if y is not None:
                yroll = shift_array1d(y, shift_by=sep_id, boundary=None)

        SF_dicts = calculate_structure_function_1d(
            u,
            v,
            sep_id,
            scalar,
            traditional_type,
            boundary,
        )

        if "LL" in traditional_type:
            SF_LL[sep_id] = SF_dicts["SF_LL"]
        if "LLL" in traditional_type:
            SF_LLL[sep_id] = SF_dicts["SF_LLL"]
        if "LTT" in traditional_type:
            SF_LTT[sep_id] = SF_dicts["SF_LTT"]
        if "LSS" in traditional_type:
            SF_LSS[sep_id] = SF_dicts["SF_LSS"]

        # Calculate separation distances along track
        if y is not None:
            xd[sep_id], tmp = calculate_separation_distances(
                x[sep_id], y[sep_id], xroll[sep_id], yroll[sep_id], grid_type
            )
        else:
            xd[sep_id], tmp = calculate_separation_distances(
                x[sep_id], None, xroll[sep_id], None, grid_type
            )

    # Bin the data if the grid is uneven
    if even is False:
        if "LL" in traditional_type:
            xd_bin, SF_LL = bin_data(xd, SF_LL, nbins)
        if "LLL" in traditional_type:
            xd_bin, SF_LLL = bin_data(xd, SF_LLL, nbins)
        if "LTT" in traditional_type:
            xd_bin, SF_LTT = bin_data(xd, SF_LTT, nbins)
        if "LSS" in traditional_type and scalar is not None:
            xd_bin, SF_LSS = bin_data(xd, SF_LSS, nbins)
        xd = xd_bin

    data = {
        "SF_LL": SF_LL,
        "SF_LLL": SF_LLL,
        "SF_LTT": SF_LTT,
        "SF_LSS": SF_LSS,
        "x-diffs": xd,
    }
    return data
