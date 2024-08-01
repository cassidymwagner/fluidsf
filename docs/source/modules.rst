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
    All the above modules can generate several types of structure functions as a function of separation distance. These are the primary modules that users will interact with. The modules described below are helper modules used by the above modules. 
    
    **Do not get confused between** :code:`generate_()` **and** :code:`calculate_()` ** modules. The latter are used to calculate a single structure function value for a given separation vector, :code:`generate_()` modules then accumulate this information for a range of separation distances.**


Calculate Structure Functions
-----------------------------

This module calculates a single structure function value for a given separation vector.

`calculate_structure_function_1d()`, `calculate_structure_function_2d()`, `calculate_structure_function_3d()`, `calculate_sf_maps_2d()`

Utilities
---------

Shift Arrays
^^^^^^^^^^^^

:code:`shift_array_1d()`, :code:`shift_array_2d()`, and :code:`shift_array_3d()`

- These modules shift data arrays in a specific direction (x, y or z) and by specific number of array elements, to efficiently calculate structure functions. The modules are used for 1D, 2D and 3D data respectively. The :code:`generate_()` modules iterate over the approprite number of dimensions and element-shifts.

:code:`shift_array_xy()`

- This module shifts 2D data arrays in two simultaneous directions (x and y) by a module-specified number of array elements that can differ between the two directions. This module is utilized by :code:`generate_sf_maps_2d()`.

Calculate Separation Distance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Text

Bin Data
^^^^^^^^

Text

Calculate Advection
-------------------

`calculate_advection_2d()`, `calculate_advection_3d()`

These modules process the provided velocity fields and grid information to diagnose the advection (vector) field required to calculate advective structure functions. Since the advective structure functions are supported in 2D and 3D, there are two versions of this module.
