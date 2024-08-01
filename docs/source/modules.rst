Modules in FluidSF
==================

Generate Structure Functions
----------------------------

FluidSF supports 1D, 2D, and 3D data, and uses a distinct module to generate (and output) structure functions for each of these systems:

:code:`generate_structure_functions_2d()`

- Generates structure functions from 2D data. It generates two sets of structure functions, one with :math:`x`-directed separation vectors, and the other with :math:`y`-directed separation vectors. It supports the calculation of second- and third-order SFs of velocity and/or scalars, and advective structure functions.

:code:`generate_structure_functions_3d()`

- Generates structure functions from 3D data. Has the same functionality as :code:`generate_structure_functions_2d()`, and generates three sets of SFs (with :math:`x`-, :math:`y`-, and :math:`z`-directed separation vectors).

:code:`generate_structure_functions_1d()`

- Generates structure functions from 1D data. It has the same functionality as :code:`generate_structure_functions_2d()`, except it cannot diagnose advective structure functions, since these require multi-directional information to diagnose the required gradients. It generates one set of SFs (:math:`x`-directed separation vectors).

**Generating 2D Maps of Structure Functions**

There is also a module that calculates the 2D spatial variations of structure functions.

:code:`generate_sf_maps_2d()`

- Generates a 2D field of structure function values as a function of separation distance and direction. This module can only be applied to evenly-spaced data from domains that are periodic in both directions. It supports the calculation of second- and third-order SFs of velocity and/or scalars, and advective structure functions.


.. important:: 
    Any :code:`generate_structure_functions()` module can generate several types of structure functions as a function of separation distance. This is the only module you need to use to generate structure functions from your data. The modules described below are helper modules that are used by the :code:`generate_structure_functions()` modules. 
    
    **Do not get confused between** :code:`generate_structure_functions()` **and** :code:`calculate_structure_function()` **, which is used to calculate a single structure function value for a given separation vector, not a range of separation distances.**


Calculate Structure Functions
-----------------------------

This module calculates a single structure function value for a given separation vector.

`calculate_structure_function_1d()`, `calculate_structure_function_2d()`, `calculate_structure_function_3d()`, `calculate_sf_maps_2d()`

Utilities
---------

Shift Arrays
^^^^^^^^^^^^

Text

Calculate Separation Distance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Text

Bin Data
^^^^^^^^

Text

Calculate Advection
-------------------

`calculate_advection_2d()`, `calculate_advection_3d()`

These modules process the input velocity fields and grid information to diagnose the advection (vector) field required to calculate advective structure functions. Since the advective structure functions are supported in 2D and 3D, there are two versions of this module.
