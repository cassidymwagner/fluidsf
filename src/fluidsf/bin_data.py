import pandas as pd


def bin_data(dd, sf, nbins):
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

    Returns
    -------
    tuple:
        A tuple containing the binned separation distances and the bin-averaged
        structure functions.
    """
    tmp = {"dd": dd, "sf": sf}
    df = pd.DataFrame(tmp)
    means = df.groupby(pd.cut(df["dd"], nbins, duplicates="drop"), observed=True).mean()
    dd = means["dd"].values
    sf = means["sf"].values

    return (dd, sf)
