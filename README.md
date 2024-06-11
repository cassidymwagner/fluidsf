[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10463864.svg)](https://doi.org/10.5281/zenodo.10463864)
[![documentation](https://img.shields.io/badge/documentation-in%20development-orange?)](https://cassidymwagner.github.io/fluidsf)
[![CI](https://github.com/cassidymwagner/FluidSF/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/cassidymwagner/FluidSF/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/cassidymwagner/fluidsf/graph/badge.svg?token=1ZZ2HUONX4)](https://codecov.io/github/cassidymwagner/fluidsf)



# Overview
FluidSF is a Python package for calculating structure functions from fluid data. These structure functions can be used to estimate turbulence cascade rates without the constraints of spectral methods. This package serves as a useful tool for analyzing turbulent dynamics in the ocean.

**For detailed documentation and examples, see the [FluidSF website](https://cassidymwagner.github.io/fluidsf).**

Installation
---
Fork/clone this repository to your local machine. The easiest method to install FluidSF is with [pip](https://pip.pypa.io/):

```console
$ pip install .
```

Quickstart
---
Once FluidSF is installed, you can load the module into Python and run some basic calculations with random data. For more detail on this example, [see the full notebook on the FluidSF website.](https://cassidymwagner.github.io/fluidsf)

First we'll initialize a random 2-D field to analyze:
```
import numpy as np
nx, ny = 100, 100
x = np.linspace(1, nx, nx)
y = np.linspace(1, ny, ny)
U = np.random.rand(nx, ny)
V = np.random.rand(nx, ny)
```

Next, we'll generate the advective structure functions. 
```
import fluidsf
sf = fluidsf.generate_structure_functions(U, V, x, y, boundary=None)
```

Finally, let's plot!
```
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(sf["x-diffs"], sf["SF_advection_velocity_x"], label="Advective velocity SF in x", color='k')
ax.plot(sf["y-diffs"], sf["SF_advection_velocity_y"], label="Advective velocity SF in y", color='k', linestyle='dotted')
ax.set_xlabel("Separation distance")
ax.set_ylabel("Structure function")
ax.legend()
plt.show()
```

"Can I use FluidSF with my data?"
---
Hopefully! FluidSF was initially developed for numerical simulations and satellite data, but there are of course many different types of data. If you are interested in using this package but you are unsure how to use it with your dataset, please reach out and we are happy to assist! 

The best way to communicate about your data needs is to [open an issue](https://github.com/cassidymwagner/fluidsf/issues) where you can describe your dataset and what you're hoping to learn with FluidSF. Before opening an issue you can check through the open (and closed) issues to see if any other users have a similar question or dataset. 

We have plans to support many different types of data, especially oceanographic data, but we encourage any users to engage with us so we can make sure we support as many datasets as possible!

Contributing
---
This project welcomes contributions and suggestions. Feel free to open an issue, submit a pull request, and/or [contact the owner directly](https://github.com/cassidymwagner).
