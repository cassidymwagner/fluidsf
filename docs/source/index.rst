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

The easiest method to install FluidSF is with `pip <https://pip.pypa.io/>`_:

.. code-block:: bash

   pip install fluidsf

You can also fork/clone the `FluidSF repository <https://github.com/cassidymwagner/FluidSF>`_ to your local machine and install it locally with pip as well:

.. code-block:: bash

   pip install .


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
advised by Brodie Pearson. This software package is based upon work supported 
by the National Science Foundation under Grant No. 2023721.

The developers welcome contributions and suggestions 
through the `FluidSF GitHub repository <https://github.com/cassidymwagner/FluidSF>`_
Feel free to open an issue, submit a pull request, and/or 
`contact the owner directly <https://github.com/cassidymwagner>`_.

Any opinions, findings, and conclusions or recommendations expressed in this package are those of the authors and do not necessarily reflect the views of the National Science Foundation.Any opinions, findings, and conclusions or recommendations expressed in this package are those of the authors and do not necessarily reflect the views of the National Science Foundation.
