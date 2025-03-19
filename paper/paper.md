---
title: '`FluidSF`: A Python package for calculating turbulent flow statistics'
tags:
  - Python
  - fluid dynamics
  - turbulence
  - structure functions
authors:
  - name: Cassidy M. Wagner
    orcid: 0000-0002-1186-2082
    corresponding: true
    affiliation: '1'
  - name: Ara Lee
    orcid:
    affiliation: '1'
  - name: Brodie Pearson
    orcid: 0000-0002-0202-0481
    affiliation: '1'
affiliations:
 - name: Oregon State University
   index: 1
date: 05 August 2024
bibliography: paper.bib
---

# Summary

Fluid systems are everywhere, from small-scale engineering problems to planetary-and-larger-scale systems (atmosphere, ocean, galactic gas clouds). These systems are often turbulent, where motion is chaotic, unpredictable, and can only be characterized through statistical analyses. Structure functions (SFs) are one such statistical analysis technique for turbulence, that require calculation of spatial differences in properties as a function of their separation distance. By combining and then averaging these spatial differences, various types of SF can be constructed to measure physical properties of fluid flow, such as heat and energy transfers, energy density, intermittency etc. However, calculating SFs is often a cumbersome and computationally-intensive task tailored to the specific format of a given fluid dataset. `FluidSF` is a flexible `Python` package that can be used to diagnose and analyze various physically-informative SFs from 1-, 2-, or 3-dimensional fluid data sets.    

# Statement of need

`FluidSF` can construct an array of traditional and modern structure functions (SFs), and can be easily modified to calculate user-defined SFs that utilize general fluid properties, including scalars (e.g., vorticity, density) and vectors (e.g., velocity, magnetic field). `FluidSF` also includes several tools to process data (e.g., array shifting, binning) and diagnose useful properties (e.g., advection) for SF analysis. The flexibility of this package enables geophysical, astrophysical, and engineering applications such as: quantifying the energy cycles within Earth's ocean [@pearson2019; @balwada2022], Earth's atmosphere [@lindborg:1999], and Jupiter's atmosphere [@young:2017], diagnosing the intermittency of magnetohydrodynamic plasma turbulence [@wan:2016] and the scaling laws of idealized 3D turbulence [@iyer:2020], or measuring the characteristics of ocean surface temperature [@schloesser:2016] or the anistropy of flow over rough beds [@coscarella:2020].   

Structure functions are constructed by averaging the correlations between spatial differences of properties. For example, given an arbitrary scalar field ($\phi$), we could calculate SFs such as this,

\begin{equation}\label{eq:eq1}
SF_{\phi \phi}(\mathbf{r}) = \overline{\delta\phi \delta \phi} = \overline{\left[ \phi(\mathbf{x} + \mathbf{r}) - \phi(\mathbf{x})\right] \left[ \phi(\mathbf{x} + \mathbf{r}) - \phi(\mathbf{x})\right] }
\end{equation}

where $\mathbf{x}$ denotes the position of a data point, $\delta \phi$ denotes the spatial variation of $\phi$, and the overline denotes an average over all positions ($\mathbf{x}$). Structure functions depend on the separation vector ($\mathbf{r}$), and are often analyzed with an assumption of isotropic flow statistics [$SF(\mathbf{r})\rightarrow SF(r=|\mathbf{r}|)$]. There are many types of physically-useful structure functions. The example above is a second-order scalar SF (i.e., it contains 2 $\delta$ terms of the scalar $\phi$), but additional physical insight can be gained from third- \& higher-order scalar SFs (3+ $\delta$ terms), SFs that depend on vector fields such as velocity, and SFs that blend information from multiple fields. 

`FluidSF` can utilize a variety of fluid data, including data sets with 1-, 2-, and 3-dimensional spatial data, and from domains with periodic or non-periodic boundary conditions. In addition to regular Cartesian-gridded data, the software also has some support for non-uniform latitude-longitude grids (1D or 2D) but not for general curvilinear coordinates. When computing SFs that blend information from multiple fields `FluidSF` assumes all variables are co-located, so care must be taken with staggered grids. Since `FluidSF` is written in `Python`, any fluid data intialized and loaded as `NumPy` [@harris:2020] arrays can be used to calculate SFs. To demonstrate the flexibility of input data, \autoref{fig:fig1} shows several types of SF calculated using `FluidSF` for a simulation of quasi-geostrophic turbulence in a periodic domain using `GeophysicalFlows.jl` [@constantinou:2021], while \autoref{fig:fig2} shows SFs calculated from satellite observations of the ocean surface made by the NASA SWOT (Surface Waves and Ocean Topography) satellite mission [@morrow:2018].

![Various structure functions (SFs) calculated from a simulated 2D turbulent flow, visualized through snapshots of the vorticity field (top left) and velocity field (bottom left). The right panels show various SFs based on velocity (red lines) and vorticity (blue lines), including third-order and advective SFs (top right) and traditional second-order SFs (bottom right). The results are from the top layer snapshot of an anisotropic 2-layer quasi-geostrophic simulation conducted with GeophysicalFlows.jl. \label{fig:fig1}](figs/fig1.png)

As demonstrated in \autoref{fig:fig1} and \autoref{fig:fig2}, `FluidSF` can calculate a wide array of traditional structure functions, including $SF_{\phi \phi}$ (\autoref{eq:eq1}; where the scalar field in this case is vorticity $\omega$), second- and third-order SFs of longitudinal velocity ($SF_{LL}=\overline{(\delta u_L)^2}$ and $SF_{LLL}=\overline{(\delta u_L)^3}$; where $u_L=\mathbf{u}\cdot\hat{\mathbf{r}}$) and transverse velocity ($SF_{TT}$ and $SF_{TTT}$), and blended velocity-scalar third-order SFs ($SF_{L\omega\omega}=\overline{\delta u_L \delta \omega \delta \omega}$), in addition to novel advective SFs  of velocity ($ASF_{V}$), vorticity ($ASF_{\omega}$) and scalars [@pearson:2021; @pearson:2025]. Advective SFs require fields of the local advection, and `FluidSF` has a built-in function to compute these advection terms. `FluidSF` can calculate SFs in specific separation directions (i.e., aligned with the Cartesian co-ordinates, shown in \autoref{fig:fig2}), and for 2D data it can diagnose maps showing how SFs vary with the magnitude and orientation of the separation vector $\mathbf{r}$ (\autoref{fig:fig3}). `FluidSF` also includes tools to make the calculation and processing of SFs easier, such as array shifting, diagnosis of the advection terms for novel SFs, decomposition of velocity into longitudinal (along-$\mathbf{r}$; $u_L$) and transverse (across-$\mathbf{r}$; $u_T$) components, and data binning based on separation distance.

![Velocity-based SFs calculated from satellite observations of the ocean surface in the North Atlantic. Maps of the inferred surface velocity from a satellite swath are shown in the top left. The region of data used for SF calculations is indicated by the red box and magnified on the top right. The bottom panel shows the advective (red) and third-order (blue) velocity structure functions calculated with separation vectors across the satellite swath (dashed) and along the swath (solid). Note the velocity fields are estimated from satellite sea surface height measurements assuming geostrophic balance. \label{fig:fig2}](figs/fig2.png)

![Maps showing the 2D spatial variation of various velocity structure functions. The left panel shows the advective velocity SF, the middle panel is the third-order velocity SF, and the right panel is the second-order velocity SF. These SFs were calculated from the same data as \autoref{fig:fig1}. \label{fig:fig3}](figs/fig3.png)

## Related Work

`FluidSF` uniquely contributes to the field through a combination of expanded data support, the ability to diagnose a wide array of structure functions (including advective and blended SFs), and tools for analyzing spatial variations in SFs. `FluidSF` was used to develop new methods for estimating inter-scale geophysical energy fluxes [@pearson:2025]. There are several open source software packages available that calculate aspects of spatial SFs. `fastSF` is a parallelized C++ code designed to compute arbitrary-order SFs of velocity or scalars (but not blended) from Cartesian grids of data [@sadhukhan:2021]. @fuchs2022 created an open source `MATLAB` toolkit that performs a variety of turbulence analysis, including arbitrary-order longitudinal-velocity SFs. A complimentary and alternative method to structure functions for analyzing turbulence data is coarse-graining. `FlowSieve` is a primarily C++ package that uses coarse-graining to estimate ocean and atmospheric turbulence properties from Global Climate Model data [@storer2023].

# Acknowledgements

The development of `FluidSF` was primarily supported by the National Science Foundation (NSF) under Grant No. 2023721 (Wagner \& Pearson) with additional support from the NSF under Grant No. 2146910 (Lee).

# References
