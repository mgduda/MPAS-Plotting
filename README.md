MPAS Plotting
=============
This repository contains a number of examples related to plotting MPAS model
output with Python. It contains examples using MatPlotLib and will later
contain examples using NCAR's PyNGO as well as any other NCAR NCL Python
modules that appear.

The goal of this repository is to function as a set of examples and reference
for Python Modules that can be used to create model output plots.

**Contents**
* [Introduction](#Introduction)
    * [Numpy](#Numpy)
    * [MatPlotLib](#MatPlotLib)
    * [Cartopy and Basemap](#Basemap)
    * [Python on Cheyenne and Casper](#venv)
    * [Python 2 and Python 3](#version)
* [Module Reference](#Module-References)
* [References and Credits](#Refs-and-Credits)


# Introduction <a name="Introduction"/>

Plotting Meteorological data in Python is a multi-module endeavour and is
undoubtedly a bit overwhelming. Some modules even contain references to each
other, which can undoubtedly be even more confusing. I hope to break this
process down into more manageable chunks, and also point you in the right
direction to find the information you need.


**Numpy**<a name="Numpy"/>

One feature that Fortran has over Python are its n-dimensional arrays and its
operations around those arrays. Vanilla Python allows you to have
multidimensional 'lists', but these multi-dimensional lists are large and
inefficient for vector and scaler operations. Thus, enters Numpy.

Numpy enables smaller, more efficient n-dimensional arrays in a very similar
approach to Fortran n-d arrays. With useful intrinsics such as `shape`,
`size`, `ndim` and others, which allow you to inspect data as you see fit.

It also enables a load of optimized mathematical functions that are sure to fit
your needs: <https://docs.scipy.org/doc/numpy/reference/routines.math.html>.


**MatPlotLib (MPL)**<a name="MatPlotLib"/>

The free alternative to creating plots in MATLAB, MPL was created by
neurobiologist to plot EEG of his patients, it has perhaps one of the largest
open source python modules in the pythonic world.

It is flexible beyond belief to fit a variety of application and can be used to
create publication-quality figures (though you may disagree coming from NCL) to
real time forecasting plots or overlays.

It has been extended to be used Geogrpahically/Meterographically with Basemap
and Cartopy.


**Basemap and Cartopy**<a name="Basemap"/>

These two modules are built on top of MatPlotLib and allow the complicated (for
me) handling of projections and converting between projections. 

Cartopy is a newer module, but is still in alpha and lacking in features and
documentation which makes it difficult to use, but it appears to be developing
rapidly.

Basemap, the original of the two modules, is much better documented and contains
more features and more examples and is much easier to use at the current
moment. I recommend using Basemap while Cartopy gains documentation and
features.


**Python on Cheyenne and Casper**<a name="venv"/>

To use Python with the modules above on Cheyenne and Casper. We'll need to
create a Python virtual environment that contains these modules. Thankfully,
CISL has created a command that will do that for us: `ncar_pylib`. Once you
have loaded a Python (version >=3.6.4) run `ncar_pylib` in your terminal window
and you'll have access to all the above modules.

**Python 2, Python 3**<a name="version"/>

Python 2 will soon not be maintained. All these examples use Python 3. Use
Python 3.


# Module and other Helpful References<a name="Module-References"/>

* Plotting
    * [MatPlotLib](https://matplotlib.org/)
* Meteorological and Geographic Plotting
    * [Basemap](https://matplotlib.org/basemap/)
    * [Cartopy](https://scitools.org.uk/cartopy/docs/latest/)
* Python NetCDF Tools
    * [Scipy Netcdf](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.io.netcdf.netcdf_file.html)
    * [Unidata's NetCDF4 Dataset](https://unidata.github.io/netcdf4-python/netCDF4/index.html)
    * [xArray](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.to_netcdf.html)
* Numpy
    * [Numpy Basics](https://docs.scipy.org/doc/numpy/user/index.html)
    * [Numpy Reference](https://docs.scipy.org/doc/numpy/reference/)

Other helpful References and Guides
* [MPL Example Gallery](https://matplotlib.org/gallery/index.html)
* [MPL Color Maps](https://matplotlib.org/users/colormaps.html)
* [MPL Styles](https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html)
* [Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html)
* [Axes](https://matplotlib.org/api/axes_api.html)
* [Anatomy Of MatplotLib](https://github.com/matplotlib/AnatomyOfMatplotlib)


# References & Credits<a name="Refs-and-Credits"/>
* [For examples and images describing MPL][1]
* [For help creating mpas_patches][2]

[1]: https://github.com/matplotlib/AnatomyOfMatplotlib
[2]: https://github.com/lmadaus/mpas_python
