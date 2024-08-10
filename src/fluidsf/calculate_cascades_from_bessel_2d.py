from scipy.integrate import cumulative_trapezoid
from scipy.special import jv
import pandas as pd


def calculate_cascades_from_bessel_2d(
    kr, df, xdiffs, ydiffs, dx, dy, sf_keys=["SF_advection_velocity_x"]
):
    """
    Calculate the cascades from the structure functions using Bessel functions.

    Parameters
    ----------
    kr: numpy.ndarray
        The kr wavevector.
    df: pandas.DataFrame
        The structure functions in a DataFrame.
    xdiffs: numpy.ndarray
        The x separation distances.
    ydiffs: numpy.ndarray
        The y separation distances.
    dx: float
        The x grid spacing.
    dy: float
        The y grid spacing.
    sf_keys: list
        The keys of the structure functions to use. Defaults to
        ["SF_advection_velocity_x"].

    Returns
    -------
    numpy.ndarray:
        The cascades.
    """
    bessels1 = [jv(1, kr[i] * xdiffs) for i in range(kr.shape[0])]
    bessels2 = [jv(2, kr[i] * xdiffs) for i in range(kr.shape[0])]
    bessels3 = [jv(3, kr[i] * xdiffs) for i in range(kr.shape[0])]

    for key in sf_keys:
        df[key] = df[key].fillna(0)

    bessel_energy_integral_asf_v = [
        -0.5 * kr[kk] * cumulative_trapezoid(df[key] * bessels1[kk], dx=dx[kk])
        for kk in range(1, len(kr) + 1)
    ]
