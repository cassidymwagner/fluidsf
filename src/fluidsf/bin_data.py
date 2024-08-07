import numpy as np
import pandas as pd


def bin_data(dd, sf, nbins, grid_type="uniform"):
    """
    Bins the data based on the separation distances and calculates the bin-averaged
    structure functions.

    Parameters
    ----------
    dd: array-like
        The separation distances to be binned.
    sf: array-like
        The structure functions that will be bin-averaged.
    nbins: int
        The number of bins to create.
    grid_type: str
        The type of grid used for the coordinates. A uniform grid uses pandas to
        bin the data, but a latlon grid uses numpy to bin the data. Defaults to
        "uniform".

    Returns
    -------
    tuple:
        A tuple containing the binned separation distances and the bin-averaged
        structure functions.
    """
    if grid_type == "latlon":
        sf_tiled = np.tile(sf, (np.shape(dd)[1], 1)).T

        dd_binned = np.linspace(np.nanmin(dd), np.nanmax(dd), nbins)
        sf_binned = np.zeros(nbins)

        for i in range(nbins):
            sf_binned[i] = np.nanmean(
                sf_tiled[(dd >= dd_binned[i - 1]) & (dd < dd_binned[i])]
            )

        dd = dd_binned
        sf = sf_binned

    else:
        tmp = {"dd": dd, "sf": sf}
        df = pd.DataFrame(tmp)
        means = df.groupby(
            pd.cut(df["dd"], nbins, duplicates="drop"), observed=True
        ).mean()
        dd = means["dd"].values
        sf = means["sf"].values

    return (dd, sf)
