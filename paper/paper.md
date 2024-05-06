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

``FluidSFs`` is a flexible ``Python`` package that can be used to calculate various spatial structure functions (SFs) in one, two, or three spatial dimensions from diverse fluid data sets. The package can construct structure functions from data on arbitrary fluid properties (e.g., velocity, temperature, magnetic field etc.)

to measure the energy budget of the ocean we need to measure cascade rates 

previous and upcoming publications:
* pearson 2021 [@pearson:2021]
* pearson sqg paper
* wagner paper 1

related software: 
* flowsieve
* fuchs 2022: matlab-based GUI package that does third order structure functions among other things
* 
# Acknowledgements

# References
