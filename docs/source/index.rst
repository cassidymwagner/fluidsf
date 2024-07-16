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

FluidSF is a Python package for calculating structure functions (SFs) from fluid data. 
The package diagnose various SFs that utilize velocity and/or scalar fields. These SFs can then be used to quantify various physical properties of fluid systems, including the distribution of energy/variance across scales, the inter-scale transfers of this energy/variance, the intermittency of the fluid flow, and the spatial anisotropy of the flow. 

This package can be applied to general fluid flow data, although our research motivation for developing this package is to analyze large-scale ocean turbulence from model output and observational (satellite) data.

.. _Installing:

Installing
**********

Fork or clone the `FluidSF repository <https://github.com/cassidymwagner/FluidSF>`_ to your local machine. 
Install FluidSF with pip:

.. code-block:: bash

   pip install . --user

.. _Citing:

Citing
******

If you use FluidSF in your research or educational activities, we would appreciate it if you cite this work.

.. .. code-block:: bibtex

..    WIP

.. _Development and Contributing:

Development and Contributing
****************************

The development of FluidSF started as a Ph.D. project for Cassidy Wagner, 
advised by Brodie Pearson. The developers welcome contributions and suggestions 
through the `FluidSF GitHub repository <https://github.com/cassidymwagner/FluidSF>`_
Feel free to open an issue, submit a pull request, and/or 
`contact the owner directly <https://github.com/cassidymwagner>`_.
