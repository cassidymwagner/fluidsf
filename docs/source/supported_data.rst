Supported data
==============

FluidSF was originally designed to handle uniformly gridded cartesian vector and scalar fields from numerical oceanographic simulations. We have been expanding our support to other data types and structures, prioritizing the most common file types and data structures used in the oceanographic community. We are working to generalize our methods of data handling to ensure that FluidSF remains flexible and user-friendly. 

.. _File Types:

File Types
**********

FluidSF has been used with data from the following file types:

* `NetCDF <https://www.unidata.ucar.edu/software/netcdf/>`_
* `JLD2 <https://github.com/JuliaIO/JLD2.jl>`_

.. note::
    FluidSF expects data in NumPy arrays, so **ideally any file type that can be converted to NumPy arrays can be used with FluidSF**. If you are facing issues with a specific file type, feel free to `create a discussion post <https://github.com/cassidymwagner/fluidsf/discussions>`_ or `open an issue <https://github.com/cassidymwagner/fluidsf/issues>`_ on the FluidSF repository.

.. _Data Structures:

Data Structures
***************

FluidSF supports the following data structures:

* Uniformly gridded cartesian vector & scalar fields (1D, 2D, 3D)
* Latitude-longitude gridded vector & scalar fields (2D)