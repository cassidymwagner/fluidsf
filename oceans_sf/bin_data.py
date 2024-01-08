import pandas as pd


def bin_data(dd, sf, nbins):
    """
    Bins the data based on the separation distances and calculates the the bin-averaged
    structure functions.

    Args
    ----
    dd (array-like): The separation distances to be binned.
    sf (array-like): The structure functions that will be bin-averaged.
    nbins (int): The number of bins to create.

    Returns
    -------
    tuple: A tuple containing the binned separation distances and the bin-averaged
    structure functions.
    """
    tmp = {"dd": dd, "sf": sf}
    df = pd.DataFrame(tmp)
    means = df.groupby(pd.qcut(df["dd"], q=nbins, duplicates="drop")).mean()
    dd = means["dd"].values
    sf = means["sf"].values

    return (dd, sf)
