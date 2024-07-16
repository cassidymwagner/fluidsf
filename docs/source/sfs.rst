What are structure functions?
=============================

.. _Overview:

The structure functions calculated within this package are statistics that describe how fluid properties vary between pairs of points as a function of their separation vector (:math:`\mathbf{r}`), averaged over all pairs of points with the same separation vector. There are numerous structure functions, describing different-order correlations of various variables, that can provide fundamental insights into the physical properties of dynamic fluid systems.

.. _Theory:

Structure functions and how to calculate them
---------------------------------------------------

**Scalar Structure Functions**

When a scalar property, arbitrarily :math:`\phi`, is measured at various locations, we can calculate second-order structure functions that describe the scalar's spatial variations: 

.. math:: 
    SF_{\phi\phi}(\mathbf{r}) = \overline{{\left[\phi(\mathbf{x}+\mathbf{r}) - \phi(\mathbf{x})\right]^2}} = \overline{{\left[\delta \phi \right]^2}}

where :math:`\theta(\mathbf{x})` is the scalar at position :math:`\mathbf{x}`, and  :math:`\mathbf{r}` is the separation vector between pairs of points. The overline represents an average over all pairs of data in the flow field that are separated by :math:`\mathbf{r}`, and :math:`\delta \phi` is a short-hand notation for the spatial difference in the scalar. This second-order (i.e. squared) structure function can be used to characterize the spatial distribution of scalar variance, analogous to the power spectra of the scalar field. Common scalars for fluid systems include temperature, density, and (vertical) vorticity.

**Velocity Structure Functions**

Since velocity is a vector, structure functions often decompose a (two dimensional) velocity field into a longitudinal component (:math:`u_L = \mathbf{u} \cdot \mathbf{\hat{r}}`) and a transverse component (:math:`u_T = \mathbf{u} \times \mathbf{\hat{r}}`). These velocity components can be visualized by considering a pair of velocity observations separated by a vector :math:`r`, as illustrated below. 

.. image:: images/sf_mooring_diagram.png
    :align: center
    :width: 50%
    :alt: A diagram showing two moorings in the ocean separated by a distance r.

There are a variety of physically-useful velocity structure functions including second-order structure functions of both velocity components,

.. math:: 
    SF_{LL}(\mathbf{r}) = \overline{{\left[u_L(\mathbf{x}+\mathbf{r}) - u_L(\mathbf{x})\right]^2}} = \overline{{\left[\delta u_L \right]^2}}

.. math::
    SF_{TT}(\mathbf{r}) = \overline{{\left[\delta u_T \right]^2}}

The spatial variations of :math:`SF_{LL}` and :math:`SF_{TT}`, and their ratio, are often used to explore the distribution of energy across scales, and the relative prevalence of rotational and divergent motions within a fluid.

It is also common to utilize third-order velocity structure functions,

.. math:: 
    SF_{LLL}(\mathbf{r}) = \overline{{\left[\delta u_L \right]^3}}

.. math::
    SF_{LTT}(\mathbf{r}) = \overline{{\left[\delta u_L \right]\left[\delta u_T \right]^2}}

.. math::
    SF_{L\phi \phi}(\mathbf{r}) = \overline{{\left[\delta u_L \right]\left[\delta \phi \right]^2}}

which can provide information about the inter-scale transfers of energy (:math:`SF_{LTT}` and :math:`SF_{LTT}`) or tracer variance (:math:`SF_{L\phi\phi}`) within a fluid flow. Note that :math:`SF_{LTT}` and :math:`SF_{L\phi\phi}` are blended structure functions, in that they utilize the spatial differences of multiple properties. 

Now consider an array of moorings. The structure function is calculated for all pairs of moorings separated by :math:`r`, and the average is taken over all pairs. The diagram below depicts an array of moorings and highlights mooring pairs with separation vectors of :math:`r = 1`, :math:`r = 2`, and :math:`r = 3`.

.. image:: images/sf_grid.png
    :align: center
    :width: 100%
    :alt: 3 figures showing a grid of data points in a flow field. The separation vector r is shown between pairs of data points where the first panel is shows r = 1, the second panel shows r = 2, and the third panel shows r = 3.

.. _Advective structure functions:

Advective structure functions
-----------------------------

Advective structure functions are a particular type of blended structure function, introduced by Pearson et al. (2021). The advective structure functions for velocity and scalars are,

.. math:: 

    ASF_{velocity}(\mathbf{r}) = \overline{\delta \mathbf{u} \cdot \delta \boldsymbol{\mathcal{A}}_{\mathbf{u}}}

.. math::
    ASF_{\phi}(\mathbf{r}) = \overline{\delta \phi \delta \mathcal{A}_{\phi}}

As the name suggests, advective structure functions depend on the advection of scalars (:math:`\mathcal{A}_{\phi}(\mathbf{x}) = \left[\mathbf{u} \cdot \nabla\right] \phi`) or velocity (:math:`\boldsymbol{\mathcal{A}}_{\mathbf{u}}(\mathbf{x}) = \left[\mathbf{u} \cdot \nabla\right] \mathbf{u}`) where :math:`\nabla` is the gradient operator.

Similar to the third-order structure functions above, advective structure functions can provide information about inter-scale transfers of energy, enstrophy, and tracer variance in simple/idealized flows. An advantage of advective structure functions is that can also be used to diagnose these properties to more complex flows (e.g., with strong anisotropy), and have different statisical properties.  

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
