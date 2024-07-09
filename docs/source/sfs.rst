What are structure functions?
=============================

.. _Overview:

Structure functions are a set of statistics that use the variance, covariance, and difference between variables in a flow field to estimate inter-scale turbulent fluxes. Fundamental fluid dynamics equations have been used to estimate a relationship between structure functions and these turbulent fluxes. For example, a third-order velocity-based structure function can be used to estimate the rate of energy flux between length scales.

.. _Theory:

Structure function theory and how to calculate them
---------------------------------------------------

When a parameter, such as velocity, is measured at many different positions, we can implement a range of statistics to understand these measurements. We can calculate the mean, the variance, the skew, among other properties, which we call moments. Structure functions are these moments, where the :math:`n`-th order velocity-based structure function can be written as

.. math:: 
    SF^n_v(\mathbf{x}) = \overline{{\left[v(\mathbf{x}) - v(\mathbf{x}+\mathbf{r})\right]^n}}

where :math:`v(\mathbf{x})` is the velocity at position :math:`\mathbf{x}` and :math:`\mathbf{r}` is the separation vector between two unique data points in the field. The overline represents an average over all possible pairs of data in the flow field that are separated by :math:`\mathbf{r}`. 

To illustrate this concept, consider a pair of moorings in the ocean that are separated by a distance :math:`r`, as shown in the diagram below.  

.. image:: images/sf_mooring_diagram.png
    :align: center
    :width: 50%
    :alt: A diagram showing two moorings in the ocean separated by a distance r.

Now consider an array of moorings. The structure function is calculated for all pairs of moorings separated by :math:`r`, and the average is taken over all pairs. The diagram below depicts an array of moorings and highlights mooring pairs with separation vectors of :math:`r = 1`, :math:`r = 2`, and :math:`r = 3`.

.. image:: images/sf_grid.png
    :align: center
    :width: 100%
    :alt: 3 figures showing a grid of data points in a flow field. The separation vector r is shown between pairs of data points where the first panel is shows r = 1, the second panel shows r = 2, and the third panel shows r = 3.

The structure function can be calculated for any order :math:`n`, but the most common are the second and third order structure functions. For a velocity field, the second-order structure function is related to the energy spectrum of the flow field, while the third-order structure function is related to the energy flux between length scales.

.. tip:: 
    Structure functions can be calculated for any scalar field, not just velocity. A common scalar field is the temperature field in the ocean, which can be used to estimate the rate of heat flux between length scales. Enstrophy flux can also be estimated from vorticity-based structure functions.

.. _Advective structure functions:

Advective structure functions
-----------------------------

Advective structure functions were introduced by Pearson et al. (2021) to estimate the rate of energy flux between length scales in anisotropic two-dimensional turbulence. As the name suggests, advective structure functions are based on the advection of fluid properties in the flow field. The advective structure function can be written as 

.. math:: 
    ASF_{\mathbf{v}}(\mathbf{x}) = \overline{{\left[\mathbf{v}(\mathbf{x}) - \mathbf{v}(\mathbf{x}+\mathbf{r})\right] \cdot \left[\mathcal{A}_{\mathbf{v}}(\mathbf{x}) - \mathcal{A}_{\mathbf{v}}(\mathbf{x}+\mathbf{r})\right]}}

where :math:`\mathcal{A}_{\mathbf{v}}(\mathbf{x})` is the advection of velocity at position :math:`\mathbf{x}`:

.. math:: 
    \mathcal{A}_{\mathbf{v}}(\mathbf{x}) = \left[\mathbf{v}(\mathbf{x}) \cdot \nabla\right] \mathbf{v}(\mathbf{x})

and :math:`\nabla` is the gradient operator. 

These structure functions have a different relationship to turbulent fluxes than traditional structure functions (above), but they can be compared to third-order structure functions.  

.. _Derived relationships between various structure functions and turbulent properties:

Derived relationships between various structure functions and turbulent properties
----------------------------------------------------------------------------------

As mentioned earlier, fundamental fluid dynamics equations have been used to estimate a relationship between structure functions and turbulent properties. The following table shows the relationships between various velocity-based structure functions and turbulent properties, but the table is not exhaustive. For more information, see the references below.

.. list-table:: 
   :header-rows: 1
   
   * - Structure function
     - Downscale energy flux
     - Energy spectrum
     - Reference
   * - :math:`SF^2_v`
     - N/A
     - ...
     - ...
   * - :math:`SF^3_v`
     - :math:`\epsilon = -2 SF^3_v /3\mathbf{r}`
     - N/A
     - Lindborg (1999)
   * - :math:`ASF_v`
     - :math:`\epsilon = - ASF_v /2`
     - N/A
     - Pearson et al. (2021)


.. _References:

References
----------

- Lindborg, E., 1999: `Can the atmospheric kinetic energy spectrum be explained by two-dimensional turbulence? <https://doi.org/10.1017/S0022112099004851>`_ *Journal of Fluid Mechanics.*
- Pearson, B. et al., 2021: `Advective structure functions in anisotropic two-dimensional turbulence. <https://doi.org/10.1017/jfm.2021.247>`_ *Journal of Fluid Mechanics.*