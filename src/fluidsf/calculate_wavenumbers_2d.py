import numpy as np


def calculate_wavevector_2d(xdiffs, ydiffs):
    """
    Calculate the kr wavevector from the separation distances.
    Assumes a uniform grid with no periodic boundary conditions.

    Parameters
    ----------
    xdiffs: numpy.ndarray
        The x separation distances.
    ydiffs: numpy.ndarray
        The y separation distances.

    Returns
    -------
    numpy.ndarray:
        The kr wavevector.
    """
    nx = len(xdiffs)
    ny = len(ydiffs)
    dx = abs(xdiffs[1] - xdiffs[0])
    dy = abs(ydiffs[1] - ydiffs[0])

    kx_int = 1 / dx
    ky_int = 1 / dy

    kx = 2 * np.py * np.arange(-nx / 2, nx / 2) * (kx_int / nx)
    ky = 2 * np.py * np.arange(-ny / 2, ny / 2) * (ky_int / ny)

    kx_max_mat = max(max(-kx[: nx // 2 + 1]), max(ky))

    dkx = 2 * np.pi / max(xdiffs)
    dky = 2 * np.pi / max(ydiffs)

    dkr_mat = np.sqrt(dkx**2 + dky**2)

    kr = np.arange(dkr_mat / 2, kx_max_mat + dkr_mat, dkr_mat)

    return kr
