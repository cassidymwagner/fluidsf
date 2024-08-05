[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10463864.svg)](https://doi.org/10.5281/zenodo.10463864)
[![documentation](https://img.shields.io/badge/documentation-in%20development-orange?)](https://cassidymwagner.github.io/fluidsf)
[![CI](https://github.com/cassidymwagner/FluidSF/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/cassidymwagner/FluidSF/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/cassidymwagner/fluidsf/graph/badge.svg?token=1ZZ2HUONX4)](https://codecov.io/github/cassidymwagner/fluidsf)


# Overview
FluidSF is a Python package for calculating structure functions from fluid data. These structure functions can be used to estimate turbulence cascade rates without the constraints of spectral methods. This package serves as a useful tool for analyzing turbulent dynamics in the ocean, atmosphere, and beyond.

<p align="center">
<img src="https://github.com/cassidymwagner/fluidsf/blob/main/docs/2d_example.png" alt="Plot of multiple methods to estimate energy flux for 2D fluid simulation" width="400"/>
</p>

<sup>_Note: FluidSF only calculates structure functions, it does not support spectral flux calculations or coarse-graining at this point. This image is an example use-case and demonstrates that advective structure functions agree with other common methods in ocean turbulence analysis._</sup>

**For detailed documentation and examples, see the [FluidSF website](https://cassidymwagner.github.io/fluidsf).**

Installation
---
Fork/clone this repository to your local machine. The easiest method to install FluidSF is with [pip](https://pip.pypa.io/):

```console
$ pip install .
```

Quickstart
---
Once FluidSF is installed, you can load the module into Python and run some basic calculations with any data. Here we'll initialize linearly increasing velocity fields. For more detail on this example, [see the full notebook on the FluidSF website.](https://cassidymwagner.github.io/fluidsf/qs.html)

First we'll initialize a random 2-D field to analyze:
```
import numpy as np

nx, ny = 100, 100
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)
U = X
V = 0.5 * X
```

Next, we'll generate the advective structure functions. 

```
import fluidsf
sf = fluidsf.generate_structure_functions_2d(U, V, x, y, sf_type=["ASF_V"], boundary=None)

```
Since we initialized our data as linearly increasing in x, we expect the advective structure function in x to scale with the squared separation distance $r^2$. Let's plot the structure function and this scaling relationship to show they match.
```

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.loglog(sf["x-diffs"], sf["SF_advection_velocity_x"], label="Advective velocity SF in x", color='tab:red')
ax.loglog(sf["x-diffs"],(5 / 4) * sf["x-diffs"] ** 2,color="k",linestyle=(0, (5, 10)))
ax.set_xlabel("Separation distance")
ax.set_ylabel("Structure function")
ax.legend()
plt.show()
```
<p align="center">
<img src="https://github.com/cassidymwagner/fluidsf/blob/main/docs/quickstart.png" alt="Advective structure function plots" width="400"/>
</p>

"Can I use FluidSF with my data?"
---
Hopefully! FluidSF was initially developed for numerical simulations and satellite data, but there are of course many different types of data. If you are interested in using this package but you are unsure how to use it with your dataset, please reach out and we are happy to assist! 

The best way to communicate about your data needs is to [start a discussion](https://github.com/cassidymwagner/fluidsf/discussions) where you can describe your dataset and what you're hoping to learn with FluidSF. Before starting a discussion you can check through other discussion posts or review the open (and closed) issues to see if any other users have a similar question or dataset. 

We have plans to support many different types of data, especially oceanographic data, but we encourage any users to engage with us so we can make sure we support as many datasets as possible!

Contributing
---
This project welcomes contributions and suggestions. Feel free to open an issue, submit a pull request, and/or [contact the owner directly](https://github.com/cassidymwagner).

References
---
- Pearson, B. et al., 2021: _Advective structure functions in anisotropic two-dimensional turbulence._ Journal of Fluid Mechanics.
- Lindborg, E. 2008: _Third-order structure function relations for quasi-geostrophic turbulence._ Journal of Fluid Mechanics.
