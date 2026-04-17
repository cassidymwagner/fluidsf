import numpy as np
import xarray as xr


def compute_LLL(
    ds,
    shiftby,
    U_vec,
    X_vec,
    time_dim="time",
    periodic=False,
):
    """
    Compute the third-order structure function LLL for a given dataset and specified 
    shifts. Dataset should contain the velocity components specified in U_vec and the 
    spatial coordinates specified in X_vec, but can have any dimensionality. The 
    function will compute the LLL structure function for each direction specified in 
    X_vec, using the corresponding velocity component in U_vec. 
    For example, if U_vec = ['u', 'v'] and X_vec = ['x', 'y'], the function will 
    compute the LLL structure function for the u velocity component in the x direction 
    and the v velocity component in the y direction, a total of 2 structure functions.

    Parameters
    ----------
    ...
    shiftby : int or list of int
        The amount by which to shift the fields when computing the structure function.
        If a list is provided, the function computes the structure function for each
        shift value.
    U_vec : list of str
        A list of variable names corresponding to the velocity components in the 
        dataset.
    X_vec : list of str
        A list of variable names corresponding to the spatial coordinates in the 
        dataset.
    periodic : bool, tuple, or list, optional
        Whether to apply periodic boundary conditions when shifting the fields. If a 
        boolean is provided, it will be applied to all directions. If a tuple or list 
        is provided, it should contain n boolean values specifying whether to apply 
        periodic boundary conditions for the n directions. For example, for a 2D 
        dataset, periodic could be (True, False) to apply periodic boundary conditions 
        in the x direction but not in the y direction. Defaults to False.
    ...

    Returns
    -------
        xr.Dataset:
            A dataset containing the computed LLL structure functions for each 
            specified direction, along with coordinates for the shift amounts.
    ...

    """    
    ds_LLL = xr.Dataset()
    shift_values = np.atleast_1d(shiftby)

    for i, (U_i, X_i) in enumerate(zip(U_vec, X_vec, strict=False)):
        
        periodic_i = periodic if isinstance(periodic, bool) else periodic[i]
        avg_dim = [d for d in ds[U_i].dims if d != time_dim] # Average over all spatial dimensions except time

        # The shifting list comp is doing all the heavy lifting in terms of iteration, 
        # so it would also be a bottle neck. Supplying a pre-chunked dataset should help
        # at this point, but there might be better options. 
        LLL_lst = []
        dx_lst = []
        for shift_i in shift_values:
            sf_results = (
                ds[U_i].roll({X_i: int(shift_i)}, roll_coords=False)
                if periodic_i
                else ds[U_i].shift({X_i: int(shift_i)})
            )
            LLL_lst.append(
                ((ds[U_i] - sf_results) ** 3)
                .mean(dim=avg_dim)
                .expand_dims(shiftby=[shift_i])
            )
            dx_lst.append(float(ds[X_i][int(shift_i)] - ds[X_i][0]))
        # Just reformatting the results of the list comp into a dataset with a new 
        # shiftby dimension. Since we call a mean here, this might take longer if 
        # the initial dataset is not already chunked.
        ds_LLL[f"SF_{U_i}{U_i}{U_i}"] = xr.concat(
            LLL_lst,
            dim="shiftby",
        ).assign_coords(shiftby=np.atleast_1d(dx_lst))

    return ds_LLL