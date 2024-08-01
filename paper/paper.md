---
title: 'FluidSF: A Python package for calculating turbulent flow statistics'
tags:
  - Python
  - fluid dynamics
  - turbulence
  - structure functions
authors:
  - name: Cassidy M. Wagner
    orcid: 0000-0002-1186-2082
    corresponding: true
    equal-contrib: false
    affiliation: 1
  - name: Ara Lee
    orcid:
    equal-contrib: false
    affiliation: 1
  - name: Brodie Pearson
    orcid: 0000-0002-0202-0481
    equal-contrib: false # (This is how you can denote equal contributions between multiple authors)
    affiliation: 1
affiliations:
 - name: Oregon State University
date: 01 June 2024
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Fluid systems are everywhere, from small-scale engineering problems to planetary-and-larger-scale systems (atmosphere, ocean, galactic gas clouds). These systems are often turbulent, where motion is chaotic, unpredictable, and can only be characterized through statistical analyses. Spatial structure functions (SFs) are one such statistical analysis technique for turbulence, that require calculation of spatial differences in properties as a function of their separation distance. By combining and then averaging these spatial differences, various types of SF can be constructed to measure physical properties of fluid flow, such as heat and energy transfers, energy density, intermittency etc. However, calculating SFs is often a cumbersome and computationally-intensive task tailored to the specific format of a given fluid dataset. `FluidSF` is a flexible software package that can be used to diagnose and analyze various physically-informative SFs from 1-, 2-, or 3-dimensional fluid data sets.    



# Statement of need

`FluidSF` is a flexible ``Python`` package for calculating spatial structure functions (SFs) from general fluid datasets that describe spatial variations in one-, two-, or three-dimensions. The package can construct an array of traditional and modern SFs, and can be easily modified to calculate user-defined SFs that utilize general fluid properties, including scalars (e.g., vorticity, density) and/or vectors (e.g., velocity, magnetic field). The package also includes several tools to process data and diagnose useful properties. The flexibility of this package enables geophysical, astrophysical, and engineering applications such as; quantifying the energy cycles within Earth's ocean [@pearson2019; @balwada2022], Earth's atmosphere [@lindborg:1999], and Jupiter's atmosphere [@young:2017], diagnosing the intermittency of magnetohydrodynamic plasma turbulence [@wan:2016] and the scaling laws of idealized 3D turbulence [@iyer:2020], or measuring the characteristics of ocean surface temperature [@schloesser:2016] or the anistropy of flow over rough beds [@coscarella:2020].   

Paragraph on package capabilities & limitations. Regularly-gridded data, Lat-lon gridded data, track/directional sampling, 1D-data, evenly-spaced, iregularly-spaced (what are limitations), binning, bootstrapping(?), local advection terms [@pearson:2021], Bessel function examples(?) [@xie:2018] examples of time-averaging, SWOT application. What are limitations (can it take 2D data in a vector rather than array format? Can it calculate 2D or 3D maps of SF rather than just a function of |r| magnitude?). Perhaps these don't need to be mentioned, or can be stated as future developments.

Spatial SFs are constructed by averaging the correlations between spatial differences of properties. For example, given an arbitrary scalar field ($\phi$), we could calculate a structure function,
$$ SF_{\phi \phi}(\mathbf{r}) = \overline{\delta\phi \delta \phi} = \overline{\left[ \phi(\mathbf{x} + \mathbf{r}) - \phi(\mathbf{x})\right] \left[ \phi(\mathbf{x} + \mathbf{r}) - \phi(\mathbf{x})\right] }$$
where $\mathbf{x}$ denotes the position of a data point, $\delta \phi$ denotes the spatial variation of $\phi$, and the overline denotes an average over all positions ($\mathbf{x}$). Structure functions depend on the separation vector ($\mathbf{r}$), and are often analyzed with an assumption of isotropic flow statistics [$SF(\mathbf{r})\rightarrow SF(r=|\mathbf{r}|)$]. There are many types of physically-useful structure functions. The example above is a second-order scalar SF (i.e., it contains 2 $\delta$ terms of the scalar $\phi$), but additional physical insight can be gained from third- \& higher-order SFs (3+ $\delta$ terms), SFs that depend on other scalar or vector fields, and SFs that blend information from various scalar/vector fields. 

![Some basic structure functions from a simulation of anisotropic 2D or QG turbulence: (a) Snapshot of the vorticity field used for SF calculations, (b) various Zonally- and meridionally-separated SFs, including third-order velocity, advective, and vorticity SFs from 2D turbulence simulation, (c) Inter-scale fluxes inferred from structure functions and diagnosed directly from the simulation](path/to/image.png)

![Structure functions calculated from satellite observations of the ocean surface: ](path/to/image.png)

![Map of the 2D spatial variation of the (a) 3rd-order longitudinal and (b) advective velocity SFs from the same data set as Figure 1: ](path/to/image.png)

`FluidSF` can utilize a variety of fluid data, including data sets with 1-, 2-, and 3-dimensional spatial data, and from domains with periodic or non-periodic boundary conditions (Figure 1). In addition to regular Cartesian-gridded data (1D, 2D or 3D), the software also has some support for non-uniform latitude-longitude grids (1D or 2D). Since `FluidSF` is written in `Python`, any fluid data intialized and loaded as `NumPy` arrays can be used to calculate SFs. To demonstrate the flexibility of input data, Figure 1 shows SFs calculated by `FluidSF` for a simulation of quasi-geostrophic turbulence in a periodic domain using `GeophysicalFlows.jl` [@constantinou:2021], while Figure 2 shows SFs calculated from satellite observations of the ocean surface made by the SWOT (Surface Waves and Ocean Topography) mission [@morrow:2018].

`FluidSF` can calculate a wide array of traditional and novel structure functions, including $SF_{\phi \phi}$ (Eq. 1), second- and third-order SFs of longitudinal and transverse velocity, blended velocity-scalar third-order SFs, and advective SFs of velocity, vorticity and scalars [@pearson:2021]. `FluidSF` can calculate these SFs in specific directions (i.e., aligned with the Cartesian co-ordinates), and for 2D data it can diagnose a map showing how the SFs vary with the magnitude and orientation of the separation vector $\mathbf{r}$ (as shown in Figure 3).  `FluidSF` also includes tools to make the calculation and processing of SFs easier, such as array shifting, diagnosis of the advection terms for novel SFs, decomposition of longitudinal (along-$\mathbf{r}$) and transverse (across-$\mathbf{r}) velocities, and bin data based on separation distance.

  <!-- * python
  * pypi installable/importable
  * advective structure functions
  * mixed structure functions
  * 2d maps of structure functions
  * binning
  * lat-lon grid support
  * non-periodic data
  * 1d structure functions -->

## Related Work

`FluidSF` uniquely contributes to the field through a combination of expanded data support, the ability to diagnose a wide array of SF types (including novel and blended SFs), and tools for analyzing spatial variations in SFs. There are several open source software packages available that calculate aspects of spatial SFs. `fastSF` is a parallelized C++ code designed to compute arbitrary-order SFs of velocity or scalars (but not blended) from Cartesian grids of data [@sadhukhan:2021]. @fuchs2022 created an open source `MATLAB` toolkit that performs a variety of turbulence analysis, including arbitrary-order longitudinal-velocity SFs. A complimentary and alternative method to structure functions for analyzing turbulence data is coarse-graining. `FlowSieve` is a primarily C++ package that uses coarse-graining to estimate ocean and atmospheric turbulence properties from Global Climate Model data [@storer2023].

<!-- Contextualize package within other relevant software
* flowsieve
* fuchs 2022: matlab-based GUI package that does third order structure functions among other things
* sadhukhan 2021: fastSF C++ code for parallel computing structure functions
  * n-th order structure functions of either longitudinal, transverse, or scalar, no mixed SFs
  * only works with cartesian 2D or 3D HDF5 files
* Dhruv's group
* a couple of julia repos, not full packages -->

# Acknowledgements

The development of FluidSF was primarily supported by the National Science Foundation (NSF) under Grant No. 2023721 (Wagner \& Pearson) with additional support from the NSF under Grant No. 2146910 (Lee).

# References
