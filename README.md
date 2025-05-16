[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10463864.svg)](https://zenodo.org/doi/10.5281/zenodo.10463863)
[![PyPI - Version](https://img.shields.io/pypi/v/fluidsf?color=blue)](https://pypi.org/project/fluidsf)
[![documentation](https://img.shields.io/badge/documentation-stable%20release-blue)](https://cassidymwagner.github.io/fluidsf)
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
The easiest method to install FluidSF is with [pip](https://pip.pypa.io/):

```console
$ pip install fluidsf
```

You can also fork/clone this repository to your local machine and install it locally with pip as well:

```console
$ pip install .
```

**Optional dependencies to run example notebooks**: [matplotlib](https://matplotlib.org), [seaborn](https://seaborn.pydata.org), [h5py](https://www.h5py.org), [scipy](https://scipy.org), [xarray](https://xarray.dev)



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

Contributing/Developing Guidelines
---
This project welcomes contributions and suggestions. The following contribution/development guidelines have been modified from those provided with [pyqg](https://github.com/pyqg/pyqg), an open-source software package for simulating geophysical fluids. Feel free to open an issue, submit a pull request, and/or [contact the owner directly](https://github.com/cassidymwagner).

Anyone interested in helping to develop FluidSF needs to create their own fork of our [git repository](https://github.com/cassidymwagner/fluidsf). (Follow the github [forking instructions](https://help.github.com/articles/fork-a-repo/). You will need a github account.)

Clone your fork on your local machine.

    $ git clone git@github.com:USERNAME/fluidsf

(In the above, replace USERNAME with your github user name.)

Then set your fork to track the upstream FluidSF repo.

    $ cd fluidsf
    $ git remote add upstream git://github.com/fluidsf/fluidsf.git

You will want to periodically sync your main branch with the upstream main.

    $ git fetch upstream
    $ git rebase upstream/main

Never make any commits on your local main branch. Instead open a feature branch for every new development task.

    $ git checkout -b cool_new_feature

(Replace `cool_new_feature` with an appropriate description of your feature.) At this point you work on your new feature, using `git add` to add your changes. When your feature is complete and well tested, commit your changes

    $ git commit -m 'did a bunch of great work'

and push your branch to github.

    $ git push origin cool_new_feature

At this point, you go find your fork on github.com and create a [pull request](https://help.github.com/articles/using-pull-requests/). Clearly describe what you have done in the comments. If your pull request fixes an issue or adds a useful new feature, the team will gladly merge it.

After your pull request is merged, you can switch back to the main branch, rebase, and delete your feature branch. You will find your new feature incorporated into fluidsf.

    $ git checkout main
    $ git fetch upstream
    $ git rebase upstream/main
    $ git branch -d cool_new_feature

### Adding Tests for New Functionality

FluidSF contains automatic tests for all its functions. These tests ensure that any commits/code changes do not affect FluidSF's existing computations. If new functionality is added to FluidSF (i.e., computation of an additional structure function) the a test should be added for each of these new functions. The existing tests [can be found here](https://github.com/cassidymwagner/fluidsf/tree/main/tests), and most new structure functions can be tested by simply adding an additional structure function to the existing test code (see [test_calculate_structure_function_1d.py](https://github.com/cassidymwagner/fluidsf/blob/main/tests/test_calculate_structure_function_1d.py) for a simple 1D example that tests second- and third-order structure functions. If you need help constructing tests, reach out to the FluidSF team!

### Virtual Testing Environment

This is how to create a virtual environment into which to test-install FluidSF,
install it, check the version, and tear down the virtual environment.

    $ conda create --yes -n test_env python=3.9 pip [space-separated list of dependencies]
    $ conda install --yes -n test_env -c conda-forge fluidsf
    $ source activate test_env
    $ pip install fluidsf
    $ python -c 'import fluidsf; print(fluidsf.__version__);'
    $ conda deactivate
    $ conda env remove --yes -n test_env

Funding Acknowledgement
---
This software package is based upon work supported by the National Science Foundation under Grant No. 2023721. 

Any opinions, findings, and conclusions or recommendations expressed in this package are those of the authors and do not necessarily reflect the views of the National Science Foundation.

References
---
- Pearson, B. et al., 2021: _Advective structure functions in anisotropic two-dimensional turbulence._ Journal of Fluid Mechanics.
- Lindborg, E. 2008: _Third-order structure function relations for quasi-geostrophic turbulence._ Journal of Fluid Mechanics.
