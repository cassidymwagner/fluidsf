FluidSF
=======

.. toctree::
   :hidden:

   sfs
   qs
   examples
   modules
   terms
   supported_data
   fluidsf

.. _Overview:

FluidSF is a Python package for calculating spatial structure functions (SFs) from 1-, 2-, and 3-dimensional fluid data. 
The package can calculate various SFs that utilize velocity and/or scalar fields. These SFs can then be used to quantify various physical properties of fluid systems, including the distribution of energy/variance across scales, the inter-scale transfers of this energy/variance, the intermittency of the fluid flow, and the spatial anisotropy of the flow. 

This package can be applied to data from general fluid flows, although our research motivation for developing this package is to analyze large-scale ocean turbulence from model output and observational (satellite) data.

.. _Installing:

Installing
**********

The easiest method to install FluidSF is with `pip <https://pip.pypa.io/>`_: ::

   $ pip install fluidsf

You can also fork/clone the `FluidSF repository <https://github.com/cassidymwagner/FluidSF>`_ to your local machine and install it locally with pip as well: ::

   $ pip install .

**List of optional dependencies to run example notebooks**: `matplotlib <https://matplotlib.org>`_, `seaborn <https://seaborn.pydata.org>`_, `h5py <https://www.h5py.org>`_, `scipy <https://scipy.org>`_, `xarray <https://xarray.dev>`_


.. _Citing:

Citing
******

If you use FluidSF in your research or educational activities, we would be grateful if you credit FluidSF by name! 

You can cite the specific version of FluidSF with `Zenodo <https://zenodo.org/records/11406185>`_ or use the following citations (replacing your version number): 

   Wagner, C., Pearson, B., & Lee, A. (2024). fluidsf (v0.2.0). Zenodo. https://doi.org/10.5281/zenodo.11406185


.. _Contributing/Developing Guidelines: 

Contributing/Developing Guidelines
**********************************

This project welcomes contributions and suggestions. The following contribution/development guidelines have been modified from those provided with `pyqg <https://github.com/pyqg/pyqg>`_, an open-source software package for simulating geophysical fluids. Feel free to open an issue, submit a pull request, and/or `contact the owner directly <https://github.com/cassidymwagner>`_.

Anyone interested in helping to develop FluidSF needs to create their own fork of our `git repository <https://github.com/cassidymwagner/fluidsf>`_. (Follow the github `forking instructions <https://help.github.com/articles/fork-a-repo/>`_. You will need a github account.)

Clone your fork on your local machine. ::

   $ git clone git@github.com:USERNAME/fluidsf

(In the above, replace USERNAME with your github user name.)

Then set your fork to track the upstream FluidSF repo. ::

   $ cd fluidsf
   $ git remote add upstream git://github.com/fluidsf/fluidsf.git

You will want to periodically sync your main branch with the upstream main. ::

   $ git fetch upstream
   $ git rebase upstream/main

Never make any commits on your local main branch. Instead open a feature branch for every new development task. ::

   $ git checkout -b cool_new_feature

(Replace ``cool_new_feature`` with an appropriate description of your feature.) At this point you work on your new feature, using ``git add`` to add your changes. When your feature is complete and well tested, commit your changes ::

   $ git commit -m 'did a bunch of great work'

and push your branch to github. ::

   $ git push origin cool_new_feature

At this point, you go find your fork on github.com and create a `pull request <https://help.github.com/articles/using-pull-requests/>`_. Clearly describe what you have done in the comments. If your pull request fixes an issue or adds a useful new feature, the team will gladly merge it.

After your pull request is merged, you can switch back to the main branch, rebase, and delete your feature branch. You will find your new feature incorporated into fluidsf. ::

   $ git checkout main
   $ git fetch upstream
   $ git rebase upstream/main
   $ git branch -d cool_new_feature


.. _Pull requests:

Pull requests
-------------

The FluidSF team is happy to help with the pull request process! Here are a few notes to get you started:

1. PR name should include the new feature or bug fix you are addressing.
2. Clearly describe the changes you have made in the comments.
3. If you make additional changes after you first open the PR, update the top comment or add new comments describing your changes.
4. GitHub Actions will run several processes to make sure your PR won't break FluidSF or change code formatting:

   - In your local repository, use `pre-commit <https://pre-commit.com>`_ and `pytest <https://docs.pytest.org/en/stable/>`_ to make sure your changes pass FluidSF's linting check and test suite.
   - After you install `pre-commit` you can run ``pre-commit run --all-files`` (or see `pre-commit` documentation to set it up to run automatically with ``git commit``).
   - See :ref:`Adding tests for new functionality` for details on running `pytest`.
   - Once your local code passes these checks, push your changes to remote and you should see that your PR passes these checks as well! 🎉

Please don't hesitate to reach out to the FluidSF team if you are having trouble -- we are grateful for your contributions!!

.. _Virtual testing environment:

Virtual Testing Environment
---------------------------

This is how to create a virtual environment into which to test-install FluidSF, install it, check the version, and tear down the virtual environment. ::

   $ conda create --yes -n test_env python=3.7 pip [space-separated list of dependencies]
   $ conda activate test_env
   $ pip install fluidsf
   $ python -c 'import fluidsf; print(fluidsf.__version__);'
   $ conda deactivate
   $ conda env remove --yes -n test_env

If you prefer to install your local version of FluidSF, run ``pip install .`` instead of ``pip install fluidsf``.

.. _Installing optional dependencies:

Installing optional dependencies
--------------------------------

Assuming a local version of FluidSF, install optional dependencies with pip: ::

   $ pip install .'[examples]'
   $ pip install .'[test]'

.. _Adding tests for new functionality:

Adding tests for new functionality
----------------------------------

FluidSF contains automatic tests for all its functions. These tests ensure that any commits/code changes do not affect FluidSF's existing computations. If new functionality is added to FluidSF (i.e., computation of an additional structure function) then a test should be added for each of these new functions. The existing tests `can be found here <https://github.com/cassidymwagner/fluidsf/tree/main/tests>`_, and most new structure functions can be tested by simply adding an additional structure function to the existing test code (see `test_calculate_structure_function_1d.py <https://github.com/cassidymwagner/fluidsf/blob/main/tests/test_calculate_structure_function_1d.py>`_ for a simple 1D example that tests second- and third-order structure functions.) If you need help constructing tests, reach out to the FluidSF team!

**pytest**

FluidSF uses `pytest <https://docs.pytest.org/en/stable/>`_ to write and execute tests.

Install ``pytest`` with ``pip`` (also available through conda-forge): ::

   $ pip install -U pytest

You can skip the previous step if you already installed the ``test`` optional dependencies (see :ref:`Installing optional dependencies`).

To run all tests in the ``tests`` directory: ::

   $ pytest tests/*

To run a specific test: ::

   $ pytest tests/test_bin_data.py

``pytest`` provides an output including the number of tests that pass and a traceback of failed tests. It is typically easier to debug one test at a time, so we suggest contributors add one test, ensure the test passes, and then add the next test. 

.. _Example notebooks and scripts:

Example notebooks and scripts
-----------------------------

Example Jupyter notebooks and python scripts can be found in the `examples directory <https://github.com/cassidymwagner/fluidsf/tree/main/examples>`_. If you would like to write a new example, follow the format of the `current Jupyter notebook examples <https://github.com/cassidymwagner/fluidsf/tree/main/examples/jupyter_notebooks>`_ and then create a stripped-down python script to accompany your example, similar to the `current python scripts <https://github.com/cassidymwagner/fluidsf/tree/main/examples/python_scripts>`_. 

Steps for running the examples: ::

   $ cd fluidsf
   $ pip install .'[examples]' #Install optional dependencies
   $ python examples/python_scripts/*.py
   $ jupyter execute examples/jupyter_notebooks/*.ipynb

You can of course open the scripts and notebooks in your development environment of choice.

Notebooks and scripts are executed during deployment, so your new example should run successfully during CI for pull request approval.

`Advanced examples <https://github.com/cassidymwagner/fluidsf/tree/main/examples/advanced_examples>`_ are also available, though they require the user/developer to access datasets separately from FluidSF (e.g. through `PO.DAAC <https://podaac.jpl.nasa.gov/cloud-datasets/dataaccess>`_ and `AVISO <https://www.aviso.altimetry.fr/en/data/products>`_). The data acquisition methods are discussed in the example notebooks.