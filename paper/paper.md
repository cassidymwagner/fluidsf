---
title: 'TITLE'
tags:
  - Python
  - oceanography
  - turbulence
  - structure functions
authors:
  - name: Cassidy M. Wagner
    orcid: 0000-0002-1186-2082
    corresponding: true
    equal-contrib: true
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

Fluid systems are everywhere, from small-scale engineering problems to planetary-and-larger-scale systems (atmosphere, ocean, galactic gas clouds). These systems are often turbulent, where motion is chaotic, unpredictable, and can only be characterized through statistical analyses. Spatial structure functions (SFs) are one such statistical analysis technique for turbulence, that require calculation of spatial differences in properties as a function of their separation distance. By combining and then averaging these spatial differences, various types of SF can be constructed to measure different critical properties of fluid flow. However, calculating SFs is often a cumbersome and computationally-intensive task tailored to the specific format of a given turbulence dataset.    

non-specialist summary -- accessible to oceanographers, turbulence people, fluids people

<!--below: flesh this out more, i took it from the paper 1 draft word for word -->
Earth’s changing climate is driven by a small energy imbalance that makes up less than 1% of the total energy budget (CITE). Any deviations in the energy budget, no matter how small, may have a large impact on future climate prediction (CITE, maybe scenarios too). To minimize error in climate prediction it is necessary to investigate how ocean turbulence regulates the global energy budget through the transfer, or cascade, of energy across spatial scales and throughout the ocean. 

# Statement of need

``FluidSFs`` is a flexible ``Python`` package for calculating spatial structure functions (SFs) in one, two, or three spatial dimensions from diverse fluid data sets. The package can construct user-defined SFs that utilize any fluid properties (e.g., velocity, vorticity, temperature, magnetic field etc.), including combinations of these properties and structure functions of arbitrary order. The flexibility of this package enables geophysical, astrophysical, and engineering applications.... ADD EXAMPLES OF SF UTILITY BREADTH: e.g., quantifying the energy cycles within Earth's ocean [@pearson2019; @balwada:2022], Earth's atmosphere [@lindborg:1999], and Jupiter's atmosphere [@young:2017], the intermittency of magnetohydrodynamic plasma turbulence [@Wan:2016], the anistropy of flow over rough beds [@coscarella:2020], the characteristics of ocean surface temperature [@schloesser:2016], and the scaling laws of idealized 3D turbulence [@iyer:2020].   

Paragraph on package capabilities & limitations. Regularly-gridded data, Lat-lon gridded data, track/directional sampling, 1D-data, evenly-spaced, iregularly-spaced (what are limitations), binning, bootstrapping(?), local advection terms [@pearson:2021], Bessel function examples(?) [@xie:2018] examples of time-averaging, SWOT application. What are limitations (can it take 2D data in a vector rather than array format? Can it calculate 2D or 3D maps of SF rather than just a function of |r| magnitude?). Perhaps these don't need to be mentioned, or can be stated as future developments.

Contextualize package within other relevant software
* flowsieve
* fuchs 2022: matlab-based GUI package that does third order structure functions among other things

# Acknowledgements

# References
