Examples
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   ex1

.. A sample dataset is provided in ``oceans_sf/examples/sample_data`` which we 
.. use below to demonstrate oceans_sf functionality.

.. Loading and preparing HDF5 data for oceans_sf
.. *********************************************

.. .. code-block:: python
   
..    import h5py
   
..    f = h5py.File('oceans_sf/examples/sample_data/snapshot1.jld2', 'r')
..    grid = f['grid']
..    snapshots = f['snapshots']

..    x = grid['x']
..    y = grid['y']
..    u = snapshots['u']
..    v = snapshots['v']

.. Advective velocity-based structure functions
.. ********************************************

.. This snippet returns a dictionary of advective velocity-based structure functions 
.. for two directions, meridional and zonal. The separation distances in x and y are also returned.

.. .. code-block:: python
   
..    import oceans_sf as ocsf

..    sf = ocsf.generate_structure_functions(u,v,x,y)

..    print(sf)


.. Advective velocity structure functions
.. **************************************

.. .. code-block:: python

..    Z, M, XD, YD = ocsf.advection_velocity(u, v, x, y)

.. Advective vorticity structure functions
.. ***************************************

.. Multiple snapshots of data
.. **************************

.. Plotting cascade rates
.. **********************