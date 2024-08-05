Key terms and definitions
=========================

When you generate structure functions with FluidSF, you are returned a dictionary with the keys provided below. Each key corresponds to a structure function that can be calculated from the data, except for the key :code:`dir-diffs`, which provides the separation distances in each direction. To learn more about the structure functions, see `What are structure functions? <sfs.html>`_

.. glossary::
   :sorted:
   
   :code:`SF_advection_velocity_dir`: Advective velocity structure function in the direction of the separation vector :code:`(dir = x, y, z)`. 
   :code:`SF_advection_scalar_dir`: Advective scalar structure function in the direction of the separation vector :code:`(dir = x, y, z)`.
   :code:`SF_LL_dir`: Longitudinal second order velocity structure function in the direction of the separation vector :code:`(dir = x, y, z)`.
   :code:`SF_LLL_dir`: Longitudinal third order velocity structure function in the direction of the separation vector :code:`(dir = x, y, z)`.
   :code:`SF_LTT_dir`: Longitudinal-transverse-transverse third order velocity structure function in the direction of the separation vector :code:`(dir = x, y, z)`.
   :code:`SF_LSS_dir`: Longitudinal-scalar-scalar third order velocity structure function in the direction of the separation vector :code:`(dir = x, y, z)`.
   :code:`dir-diffs`: Separation distances in each direction :code:`(dir = x, y, z)`. These are calculated as the Euclidean distance between pairs of data points in the flow field. Provided in the same units as the input data.

.. important:: 
    All non-advective structure functions have naming conventions with the subscripts `L`, and `T` to denote the longitudinal and transverse velocities. The longitudinal direction is typically aligned with the flow direction, while the transverse direction is perpendicular to the flow direction.  
    
    For :code:`SF_LL_x`, :code:`SF_LLL_x`, :code:`SF_LTT_x`, and :code:`SF_LSS_x`, `L` denotes the longitudinal velocity differences in the x-direction :math:`v_x(\mathbf{x}) - v_x(\mathbf{x}+\mathbf{r})` and `T` denotes the transverse velocity differences in the x-direction :math:`v_y(\mathbf{x}) - v_y(\mathbf{x}+\mathbf{r})`. `S` denotes the scalar differences :math:`s(\mathbf{x}) - s(\mathbf{x}+\mathbf{r})`.