import numpy as np

from .bin_data import bin_data
from .calculate_advection_2d import calculate_advection_2d
from .calculate_separation_distances import calculate_separation_distances
from .calculate_structure_function_2d import (
    calculate_structure_function_2d,
)
from .shift_array_1d import shift_array_1d


def generate_structure_functions_2d(  # noqa: C901, D417
    u,
    v,
    x=None,
    y=None,
    lats=None,
    lons=None,
    sf_type=["ASF_V"],  # noqa: B006
    scalar=None,
    dx=None,
    dy=None,
    boundary="periodic-all",
    grid_type="uniform",
    nbins=None,
    radius=None,
    sphere_circumference=40075,
):
    """
    Full method for generating structure functions for 2D data, either advective or
    traditional structure functions. Supports velocity-based and scalar-based structure
    functions. Defaults to calculating the velocity-based advective structure functions
    for the x and y directions.

    Parameters
    ----------
        u: ndarray
            2D array of u velocity components.
        v: ndarray
            2D array of v velocity components.
        x: ndarray, optional
            1D array of x-coordinates. Defaults to None, but must be provided if
            grid_type is not "latlon".
        y: ndarray, optional
            1D array of y-coordinates. Defaults to None, but must be provided if
            grid_type is not "latlon".
        lats: ndarray, optional
            2D array of latitudes. Defaults to None, but must be provided if
            grid_type is "latlon".
        lons: ndarray, optional
            2D array of longitudes. Defaults to None, but must be provided if
            grid_type is "latlon".
        sf_type: list
            List of structure function types to calculate.
            Accepted types are: "ASF_V, "ASF_S", "LL", "LLL", "LTT", "LSS". Defaults to
            "ASF_V".
        scalar: ndarray, optional
            2D array of scalar values. Defaults to None.
        dx: float, optional
            Grid spacing in the x-direction. Defaults to None.
        dy: float, optional
            Grid spacing in the y-direction. Defaults to None.
        boundary: str, optional
            Boundary condition of the data. Accepted strings are "periodic-x",
            "periodic-y", and "periodic-all". Defaults to "periodic-all".
        grid_type:str, optional
            Type of grid, either "uniform" or "latlon". Defaults to "uniform".
        nbins: int, optional
            Number of bins for binning the data. Defaults to None, i.e. does not bin
            data.
        radius: float, optional
            The radius of the sphere for latlon grids. Defaults to None, which will use
            the default value of the Earth's radius. Must be in units of kilometers if
            provided.
        sphere_circumference: float, optional
            The circumference of the sphere for latlon grids in kilometers.
            Defaults to 40075 km for Earth.

    Returns
    -------
        dict:
            Dictionary containing the requested structure functions and separation
            distances for the x- and y-direction.

    """
    # Error handling

    if not isinstance(sf_type, list):
        raise ValueError("sf_type must be a list of strings.")

    if len(sf_type) == 0:
        raise ValueError(
            "sf_type cannot be an empty list. All elements in sf_type must be strings. "
            "Accepted strings are: ASF_V, ASF_S, LL, LLL, LTT, LSS."
        )

    if not all(isinstance(t, str) for t in sf_type):
        raise ValueError(
            "All elements in sf_type must be strings. Accepted strings are: "
            "ASF_V, ASF_S, LL, LLL, LTT, LSS."
        )

    if boundary not in ["periodic-all", "periodic-x", "periodic-y", None]:
        raise ValueError(
            "Boundary must be 'periodic-all', 'periodic-x', 'periodic-y', or None."
        )
    if grid_type not in ["uniform", "latlon", None]:
        raise ValueError("Grid type must be 'uniform', 'latlon', or None.")

    if grid_type == "latlon" and (
        isinstance(lats, int | float | None) or isinstance(lons, int | float | None)
    ):
        raise ValueError(
            "If grid_type is 'latlon', you must provide 2D arrays of latitudes and "
            "longitudes."
        )

    if grid_type == "uniform" and (lats is not None or lons is not None):
        raise ValueError(
            "If grid_type is 'uniform', you cannot provide 2D arrays of latitudes and "
            "longitudes."
        )

    if grid_type != "latlon" and (x is None or y is None):
        raise ValueError(
            "If grid_type is not 'latlon', you must provide 1D arrays of x and y "
            "coordinates."
        )

    if grid_type == "latlon" and (boundary != "periodic-x" and boundary is not None):
        raise ValueError(
            "If grid_type is 'latlon', you must set boundary to 'periodic-x' or None."
        )

    if scalar is not None and (("LSS" not in sf_type) and ("ASF_S" not in sf_type)):
        raise ValueError(
            "If scalar is provided, you must include 'LSS' or 'ASF_S' " "in SF_type."
        )
    if scalar is None and (("LSS" in sf_type) or ("ASF_S" in sf_type)):
        raise ValueError(
            "If you include 'LSS' or 'ASF_S' in SF_type, you must provide "
            "a scalar array."
        )

    # Initialize variables as NoneType
    SF_adv_x = None
    SF_adv_y = None
    SF_x_scalar = None
    SF_y_scalar = None
    adv_x = None
    adv_y = None
    adv_scalar = None
    SF_x_LL = None
    SF_y_LL = None
    SF_x_LLL = None
    SF_y_LLL = None
    SF_x_LTT = None
    SF_y_LTT = None
    SF_x_LSS = None
    SF_y_LSS = None

    # Define a list of separation distances to iterate over.
    # Periodic is half the length since the calculation will wrap the data.
    if boundary == "periodic-all":
        sep_x = range(1, int(len(x) / 2))
        sep_y = range(1, int(len(y) / 2))
    elif boundary == "periodic-x":
        if grid_type == "latlon":
            sep_x = range(1, int(len(lons[0, :]) / 2))
            sep_y = range(1, int(len(lats[:, 0]) - 1))
        else:
            sep_x = range(1, int(len(x) / 2))
            sep_y = range(1, int(len(y) - 1))
    elif boundary == "periodic-y":
        sep_x = range(1, int(len(x) - 1))
        sep_y = range(1, int(len(y) / 2))
    elif boundary is None:
        if grid_type == "latlon":
            sep_x = range(1, int(len(lons[0, :]) - 1))
            sep_y = range(1, int(len(lats[:, 0]) - 1))
        else:
            sep_x = range(1, int(len(x) - 1))
            sep_y = range(1, int(len(y) - 1))

    # Initialize the separation distance arrays
    if grid_type == "latlon":
        xd = np.zeros((len(sep_x) + 1, len(sep_y) + 1))
        yd = np.zeros((len(sep_y) + 1, len(sep_y) + 1))

    else:
        xd = np.zeros(len(sep_x) + 1)
        yd = np.zeros(len(sep_y) + 1)

    # Calculate advection if requested
    if "ASF_V" in sf_type:
        SF_adv_x = np.zeros(len(sep_x) + 1)
        SF_adv_y = np.zeros(len(sep_y) + 1)
        adv_x, adv_y = calculate_advection_2d(
            u,
            v,
            x,
            y,
            lats,
            lons,
            dx,
            dy,
            grid_type,
            scalar=None,
            sphere_circumference=sphere_circumference,
        )
    if "ASF_S" in sf_type:
        SF_x_scalar = np.zeros(len(sep_x) + 1)
        SF_y_scalar = np.zeros(len(sep_y) + 1)
        adv_scalar = calculate_advection_2d(
            u, v, x, y, lats, lons, dx, dy, grid_type, scalar, sphere_circumference
        )
    if "LL" in sf_type:
        SF_x_LL = np.zeros(len(sep_x) + 1)
        SF_y_LL = np.zeros(len(sep_y) + 1)
    if "LLL" in sf_type:
        SF_x_LLL = np.zeros(len(sep_x) + 1)
        SF_y_LLL = np.zeros(len(sep_y) + 1)
    if "LTT" in sf_type:
        SF_x_LTT = np.zeros(len(sep_x) + 1)
        SF_y_LTT = np.zeros(len(sep_y) + 1)
    if "LSS" in sf_type:
        SF_x_LSS = np.zeros(len(sep_x) + 1)
        SF_y_LSS = np.zeros(len(sep_y) + 1)

    # Iterate over separations in x and y
    for x_shift in sep_x:
        y_shift = 1
        if boundary == "periodic-all" or boundary == "periodic-x":
            if grid_type == "latlon":
                lonroll = shift_array_1d(
                    lons[0, :], shift_by=x_shift, boundary="Periodic"
                )
            else:
                xroll = shift_array_1d(x, shift_by=x_shift, boundary="Periodic")
        else:
            if grid_type == "latlon":
                lonroll = shift_array_1d(lons[0, :], shift_by=x_shift, boundary=None)
            else:
                xroll = shift_array_1d(x, shift_by=x_shift, boundary=None)

        SF_dicts = calculate_structure_function_2d(
            u,
            v,
            adv_x,
            adv_y,
            x_shift,
            y_shift,
            sf_type,
            scalar,
            adv_scalar,
            boundary,
        )

        if "ASF_V" in sf_type:
            SF_adv_x[x_shift] = SF_dicts["SF_advection_velocity_x"]
        if "LL" in sf_type:
            SF_x_LL[x_shift] = SF_dicts["SF_LL_x"]
        if "LLL" in sf_type:
            SF_x_LLL[x_shift] = SF_dicts["SF_LLL_x"]
        if "LTT" in sf_type:
            SF_x_LTT[x_shift] = SF_dicts["SF_LTT_x"]
        if "ASF_S" in sf_type:
            SF_x_scalar[x_shift] = SF_dicts["SF_advection_scalar_x"]
        if "LSS" in sf_type:
            SF_x_LSS[x_shift] = SF_dicts["SF_LSS_x"]

        # Calculate separation distances in x
        if grid_type == "latlon":
            for lat in range(len(lats[:, 0]) - 1):
                xd[x_shift][lat], tmp = calculate_separation_distances(
                    lons[0, 0],
                    lats[lat, 0],
                    lonroll[0],
                    lats[lat, 0],
                    grid_type,
                    radius,
                )

        else:
            xd[x_shift], tmp = calculate_separation_distances(
                x[0], y[0], xroll[0], y[0], grid_type
            )

    for y_shift in sep_y:
        x_shift = 1
        if boundary == "periodic-all" or boundary == "periodic-y":
            if grid_type == "latlon":
                latroll = shift_array_1d(
                    lats[:, 0], shift_by=y_shift, boundary="Periodic"
                )
            else:
                yroll = shift_array_1d(y, shift_by=y_shift, boundary="Periodic")
        else:
            if grid_type == "latlon":
                latroll = shift_array_1d(lats[:, 0], shift_by=y_shift, boundary=None)
            else:
                yroll = shift_array_1d(y, shift_by=y_shift, boundary=None)

        SF_dicts = calculate_structure_function_2d(
            u,
            v,
            adv_x,
            adv_y,
            x_shift,
            y_shift,
            sf_type,
            scalar,
            adv_scalar,
            boundary,
        )

        if "ASF_V" in sf_type:
            SF_adv_y[y_shift] = SF_dicts["SF_advection_velocity_y"]
        if "LL" in sf_type:
            SF_y_LL[y_shift] = SF_dicts["SF_LL_y"]
        if "LLL" in sf_type:
            SF_y_LLL[y_shift] = SF_dicts["SF_LLL_y"]
        if "LTT" in sf_type:
            SF_y_LTT[y_shift] = SF_dicts["SF_LTT_y"]
        if "ASF_S" in sf_type:
            SF_y_scalar[y_shift] = SF_dicts["SF_advection_scalar_y"]
        if "LSS" in sf_type:
            SF_y_LSS[y_shift] = SF_dicts["SF_LSS_y"]

        # Calculate separation distances in y
        if grid_type == "latlon":
            for start_lat in range(len(lats[:, 0]) - 1):
                try:
                    tmp, yd[y_shift][start_lat] = calculate_separation_distances(
                        lons[0, 0],
                        lats[start_lat, 0],
                        lons[0, 0],
                        latroll[start_lat],
                        grid_type,
                        radius,
                    )

                except ValueError:
                    yd[y_shift][start_lat] = np.nan

        else:
            tmp, yd[y_shift] = calculate_separation_distances(
                x[0], y[0], x[0], yroll[0], grid_type
            )

    # Bin the data if requested or if grid_type is latlon
    if nbins is not None:
        if "ASF_V" in sf_type:
            xd_bin, SF_adv_x = bin_data(xd, SF_adv_x, nbins, grid_type)
            yd_bin, SF_adv_y = bin_data(yd, SF_adv_y, nbins, grid_type)
        if "ASF_S" in sf_type:
            xd_bin, SF_x_scalar = bin_data(xd, SF_x_scalar, nbins, grid_type)
            yd_bin, SF_y_scalar = bin_data(yd, SF_y_scalar, nbins, grid_type)
        if "LL" in sf_type:
            xd_bin, SF_x_LL = bin_data(xd, SF_x_LL, nbins, grid_type)
            yd_bin, SF_y_LL = bin_data(yd, SF_y_LL, nbins, grid_type)
        if "LLL" in sf_type:
            xd_bin, SF_x_LLL = bin_data(xd, SF_x_LLL, nbins, grid_type)
            yd_bin, SF_y_LLL = bin_data(yd, SF_y_LLL, nbins, grid_type)
        if "LTT" in sf_type:
            xd_bin, SF_x_LTT = bin_data(xd, SF_x_LTT, nbins, grid_type)
            yd_bin, SF_y_LTT = bin_data(yd, SF_y_LTT, nbins, grid_type)
        if "LSS" in sf_type:
            xd_bin, SF_x_LSS = bin_data(xd, SF_x_LSS, nbins, grid_type)
            yd_bin, SF_y_LSS = bin_data(yd, SF_y_LSS, nbins, grid_type)
        xd = xd_bin
        yd = yd_bin

    data = {
        "SF_advection_velocity_x": SF_adv_x,
        "SF_advection_velocity_y": SF_adv_y,
        "SF_advection_scalar_x": SF_x_scalar,
        "SF_advection_scalar_y": SF_y_scalar,
        "SF_LL_x": SF_x_LL,
        "SF_LL_y": SF_y_LL,
        "SF_LLL_x": SF_x_LLL,
        "SF_LLL_y": SF_y_LLL,
        "SF_LTT_x": SF_x_LTT,
        "SF_LTT_y": SF_y_LTT,
        "SF_LSS_x": SF_x_LSS,
        "SF_LSS_y": SF_y_LSS,
        "x-diffs": xd,
        "y-diffs": yd,
    }

    return data
