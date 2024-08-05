import numpy as np

from .bin_data import bin_data
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function_1d import calculate_structure_function_1d
from .shift_array_1d import shift_array_1d


def generate_structure_functions_1d(  # noqa: C901, D417
    u,
    x,
    sf_type=["LLL"],  # noqa: B006
    v=None,
    y=None,
    scalar=None,
    dx=None,
    boundary="Periodic",
    grid_type="uniform",
    nbins=None,
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
        x: ndarray
            1D array of coordinates. If you have lat-lon data, set x to 1D array of
            latitudes.
        sf_type: list
            List of structure function types to calculate. Accepted types are: "LL",
            "TT", "SS", "LLL", "LTT", "LSS". Defaults to "LLL". If you include "SS" or
            "LSS", you must provide a 1D array for scalar.
        v: ndarray
            1D array of v velocity components. Defaults to None.
        y: ndarray, optional
            1D array of coordinates orthogonal to x. Defaults to None. If you have
            lat-lon data, set y to 1D array of longitudes.
        scalar: ndarray, optional
            1D array of scalar values. Defaults to None.
        dx: float, optional
            Grid spacing along the data track. Defaults to None.
        boundary: str, optional
            Boundary condition of the data. Defaults to "Periodic". Set to None if no
            boundary conditions.
        grid_type:str, optional
            Type of grid, either "uniform" or "latlon". Defaults to "uniform".
        nbins: int, optional
            Number of bins for binning the data. Defaults to None, i.e. does not bin
            data.

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
    if scalar is not None and "SS" not in sf_type and "LSS" not in sf_type:
        raise ValueError(
            "If scalar is provided, you must include 'SS' and/or 'LSS' in sf_type."
        )
    if scalar is None and ("SS" in sf_type or "LSS" in sf_type):
        raise ValueError(
            "If you include 'SS' or 'LSS' in sf_type, you must provide a scalar array."
        )
    if v is None and ("TT" in sf_type or "LTT" in sf_type):
        raise ValueError(
            "If you include 'TT' or 'LTT' in sf_type, you must provide a v array."
        )

    # Initialize variables as NoneType
    SF_LL = None
    SF_TT = None
    SF_SS = None
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
    if "LL" in sf_type:
        SF_LL = np.zeros(len(sep) + 1)
    if "TT" in sf_type:
        SF_TT = np.zeros(len(sep) + 1)
    if "SS" in sf_type:
        SF_SS = np.zeros(len(sep) + 1)
    if "LLL" in sf_type:
        SF_LLL = np.zeros(len(sep) + 1)
    if "LTT" in sf_type:
        SF_LTT = np.zeros(len(sep) + 1)
    if "LSS" in sf_type:
        SF_LSS = np.zeros(len(sep) + 1)

    # Iterate over separations
    for sep_id in sep:
        if boundary == "Periodic":
            xroll = shift_array_1d(x, shift_by=sep_id, boundary="Periodic")
            if y is not None:
                yroll = shift_array_1d(y, shift_by=1, boundary="Periodic")
        else:
            xroll = shift_array_1d(x, shift_by=sep_id, boundary=None)
            if y is not None:
                yroll = shift_array_1d(y, shift_by=1, boundary=None)

        SF_dicts = calculate_structure_function_1d(
            u,
            sep_id,
            sf_type,
            v,
            scalar,
            boundary,
        )

        if "LL" in sf_type:
            SF_LL[sep_id] = SF_dicts["SF_LL"]
        if "TT" in sf_type:
            SF_TT[sep_id] = SF_dicts["SF_TT"]
        if "SS" in sf_type:
            SF_SS[sep_id] = SF_dicts["SF_SS"]
        if "LLL" in sf_type:
            SF_LLL[sep_id] = SF_dicts["SF_LLL"]
        if "LTT" in sf_type:
            SF_LTT[sep_id] = SF_dicts["SF_LTT"]
        if "LSS" in sf_type and scalar is not None:
            SF_LSS[sep_id] = SF_dicts["SF_LSS"]

        # Calculate separation distances along track
        if y is not None:
            xd[sep_id], tmp = calculate_separation_distances(
                x[0], y[0], xroll[0], yroll[0], grid_type
            )
        else:
            xd[sep_id], tmp = calculate_separation_distances(
                x[0], None, xroll[0], None, grid_type
            )

    # Bin the data if requested
    if nbins is not None:
        if "LL" in sf_type:
            xd_bin, SF_LL = bin_data(xd, SF_LL, nbins)
        if "TT" in sf_type:
            xd_bin, SF_TT = bin_data(xd, SF_TT, nbins)
        if "SS" in sf_type:
            xd_bin, SF_SS = bin_data(xd, SF_SS, nbins)
        if "LLL" in sf_type:
            xd_bin, SF_LLL = bin_data(xd, SF_LLL, nbins)
        if "LTT" in sf_type:
            xd_bin, SF_LTT = bin_data(xd, SF_LTT, nbins)
        if "LSS" in sf_type and scalar is not None:
            xd_bin, SF_LSS = bin_data(xd, SF_LSS, nbins)
        xd = xd_bin

    data = {
        "SF_LL": SF_LL,
        "SF_TT": SF_TT,
        "SF_SS": SF_SS,
        "SF_LLL": SF_LLL,
        "SF_LTT": SF_LTT,
        "SF_LSS": SF_LSS,
        "x-diffs": xd,
    }
    return data
