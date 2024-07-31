---
title: 'FluidSF: A Python package for calculating turbulent fluid statistics'
tags:
  - Python
  - fluid dynamics
  - turbulence
  - structure functions
authors:
  - name: Cassidy M. Wagner
    orcid: 0000-0002-1186-2082
    corresponding: true
    equal-contrib: true
    affiliation: 1
  - name: Ara Lee
    orcid:
    equal-contrib: false
    affiliation: 1
  - name: Brodie Pearson
    orcid: 0000-0002-0202-0481
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
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

Fluid systems are everywhere, from small-scale engineering problems to planetary-and-larger-scale systems (atmosphere, ocean, galactic gas clouds). These systems are often turbulent, where motion is chaotic, unpredictable, and can only be characterized through statistical analyses. Spatial structure functions (SFs) are one such statistical analysis technique for turbulence, that require calculation of spatial differences in properties as a function of their separation distance. By combining and then averaging these spatial differences, various types of SF can be constructed to measure physical properties of fluid flow, such as heat and energy transfers, energy density, intermittency etc. However, calculating SFs is often a cumbersome and computationally-intensive task tailored to the specific format of a given fluid dataset.    



# Statement of need

`FluidSF` is a flexible ``Python`` package for calculating spatial structure functions (SFs) from general fluid datasets that capture one-, two-, or three-dimensional spatial data. The package can construct an array of traditional and modern SFs, and can be easily modified to calculate user-defined SFs that utilize fluid properties that are scalars (e.g., vorticity, density) and/or vectors (e.g., velocity, magnetic field). The package also includes several tools to process data and diagnose useful properties. The flexibility of this package enables geophysical, astrophysical, and engineering applications such as; quantifying the energy cycles within Earth's ocean [@pearson2019; @balwada2022], Earth's atmosphere [@lindborg:1999], and Jupiter's atmosphere [@young:2017], diagnosing the intermittency of magnetohydrodynamic plasma turbulence [@wan:2016] and the scaling laws of idealized 3D turbulence [@iyer:2020], or measuring the characteristics of ocean surface temperature [@schloesser:2016] or the anistropy of flow over rough beds [@coscarella:2020].   

Paragraph on package capabilities & limitations. Regularly-gridded data, Lat-lon gridded data, track/directional sampling, 1D-data, evenly-spaced, iregularly-spaced (what are limitations), binning, bootstrapping(?), local advection terms [@pearson:2021], Bessel function examples(?) [@xie:2018] examples of time-averaging, SWOT application. What are limitations (can it take 2D data in a vector rather than array format? Can it calculate 2D or 3D maps of SF rather than just a function of |r| magnitude?). Perhaps these don't need to be mentioned, or can be stated as future developments.

FluidSF calculates SFs from 1D, 2D, and 3D data with periodic and non-periodic boundary conditions. Regular Cartesian (1D, 2D, 3D) and non-uniform latitude-longitude gridding (1D, 2D) are supported. Since FluidSF is written in `Python`, any data intialized and loaded as `NumPy` arrays can be used. 

FluidSF is the first software pacakage that calculates novel advective SFs, a type of SF that depends on velocity advection and does not assume an isotropic flow field [@pearson:2021]. Therefor FluidSF also computes advection for 2D and 3D data. It supports blended SFs, i.e. a combination of longitudinal and transverse velocity SFs, whereas other software only supports purely longitudinal or transverse SFs. 

To explore spatial variations in SFs, FluidSF computes 2D polar maps of SFs that vary in separation distance and separation direction.

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

FluidSF uniquely contributes to the field through a combination of expanded data support, the ability to diagnose a wide array of SF types, and tools for analyzing spatial variations in SFs. There are a small number of open source software available that calculate structure functions. `fastSF` is a parallelized C++ code designed to compute structure functions from Cartesian grids of data [@sadhukhan:2021]. @fuchs2022 created an open source `MATLAB` toolkit that performs a variety of turbulence analysis, including structure functions. An complimentary and alternative method to structure functions for analyzing turbulence data is coarse-graining. `FlowSieve` is a primarily C++ package that uses coarse-graining to estimate ocean and atmospheric turbulence properties from Global Climate Model data [@storer2023].

<!-- Contextualize package within other relevant software
* flowsieve
* fuchs 2022: matlab-based GUI package that does third order structure functions among other things
* sadhukhan 2021: fastSF C++ code for parallel computing structure functions
  * n-th order structure functions of either longitudinal, transverse, or scalar, no mixed SFs
  * only works with cartesian 2D or 3D HDF5 files
* Dhruv's group
* a couple of julia repos, not full packages -->

# Acknowledgements

The development of FluidSF was supported by the National Science Foundation under Grant No. 2023721.

# References
