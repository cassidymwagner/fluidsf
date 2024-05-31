Getting started
===============

Once FluidSF is installed, you can load the module into Python and run some basic calculations with random data.

.. code-block:: python

   import fluidsf
   import numpy as np

Create a random 2D velocity field
---------------------------------
.. code-block:: python

    nx, ny = 100, 100
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    U = np.random.rand(nx, ny)
    V = np.random.rand(nx, ny)

Generate the advective velocity structure function
---------------------------------------------------
We can generate the advective structure function using the function `generate_structure_functions`. The function returns a dictionary with the all supported structure functions and separation distances in each direction. By default the advective velocity structure functions are calculated and the remaining structure functions are set to `None`. We set the boundary condition to `None` because our random data is non-periodic. If we had periodic data we could set the boundary condition based on the direction of periodicity (i.e. `boundary="periodic-x"` or `boundary="periodic-y"` for 2D data). 

.. code-block:: python
    sf = fluidsf.generate_structure_functions(U, V, x, y, boundary="None")

The keys of the dictionary `sf` are 

- `SF_advection_velocity_dir`: Advective velocity structure function in the direction of the separation vector (`dir` = `x`, `y`, `z`).
- `SF_advection_scalar_dir`: Advective scalar structure function in the direction of the separation vector (`dir` = `x`, `y`, `z`).
- `SF_LL_dir`: Longitudinal second order velocity structure function in the direction of the separation vector (`dir` = `x`, `y`, `z`).
- `SF_LLL_dir`: Longitudinal third order velocity structure function in the direction of the separation vector (`dir` = `x`, `y`, `z`).
- `SF_LTT_dir`: Longitudinal-transverse-transverse third order velocity structure function in the direction of the separation vector (`dir` = `x`, `y`, `z`).
- `SF_LSS_dir`: Longitudinal-scalar-scalar third order velocity structure function in the direction of the separation vector (`dir` = `x`, `y`, `z`).
- `dir-diffs`: Separation distances in each direction (`dir` = `x`, `y`, `z`).

Plot the advective velocity structure function
----------------------------------------------

.. code-block:: python

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(sf["x-diffs"], sf["SF_advection_velocity_x"], label="Advective velocity SF in x")
    ax.plot(sf["y-diffs"], sf["SF_advection_velocity_y"], label="Advective velocity SF in y")
    ax.set_xlabel("Separation distance")
    ax.set_ylabel("Structure function")
    ax.legend()
    plt.show()


