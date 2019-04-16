MPAS Plotting
=============
This repository contains a number of examples related to plotting MPAS model
output with Python. It contains examples using MatPlotLib and will later
contain examples using NCAR's PyNGO as well as any other NCAR NCL Python
modules that appear.

The goal of this repository is to function as a set of examples and reference
for Python Modules that can be used to create model output plots.

**Contents**
* [Introduction to Python Modules](#Introduction)
    * [Numpy](#Numpy)
    * [Python NetCDF Modules and other Met Datatypes](#NetCDF)
    * [Cartopy and Basemap](#Basemap)
    * [Python on Cheyenne and Casper](#venv)
    * [Python 2 and Python 3](#version)
* [Quick Introduction to MatPlotLib](#MPL-Intro)
* [Helpful References and Guides](#Module-References)
<!-- [References and Credits](#Refs-and-Credits) -->


# Introduction to Python Modules<a name="Introduction"/>

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

**Python NetCDF Modules and other Met Datatypes**<a name="NetCDF"/>

There are a few modules out there that can support reading, creating and
manipulating NetCDF. These include: Scipy NetCDF, NetCDF4 Dataset, xArray, as
well as NCAR's PyNIO (which is an NCL wrapper).

You have a multitude of modules to choose from, but I recommend starting with
Scipy's NetCDF module to start. It contains the most examples and is the best
documented; however, it cannot open NetCDF4, but you can use UNIDATA's NetCDF4
Dataset instead, its also easy to use, but its documentation could be better.

If you need to open other Datatypes such as Grib, HDF, etc. PyNIO is currently
your best choice: <https://www.pyngl.ucar.edu/Nio.shtml>. However, with the
shift to Python and PyNIO going into maintenance mode, it may be worth becoming
familiar with Python alternatives. Here is a list of common met datatypes and
modules that can open them:

* GRIB - [cfgrib](https://github.com/ecmwf/cfgrib)
* HDFS - [PyTables](http://www.pytables.org/index.html)
* HDF-EOS - [PyHDF](https://www.hdfeos.org/software/pyhdf.php)

(Note: I don't know how many of these are on cheyenne or capser)

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

Python 2 will soon not be maintained. All of these examples use Python 3. Use
Python 3.

# Quick Introduction to MatPlotLib<a name="MPL-Intro"/>

MatPlotLib can be a confusing module to use and understand at first, but with
practice and understanding of how its mechanisms work, plotting becomes much
easier.

<a href="./data/MatPlotLib-Anatomy1.png"><img src="./data/MatPlotLib-Anatomy1.png" alt="Anatomy1" width="400"/></a>
<a href="./data/MatPlotLib-Anatomy2.png"><img src="./data/MatPlotLib-Anatomy2.png" alt="Anatomy2" width="430"/></a>

Above, are two images that I wish I had when I started using MPL. They both
give an overview of the anatomy of a MPL Figure and its parts.

You'll see on the image on the left, those two main parts are the Figure, and
the Axes/Subplot. The Figure, is highest in the hierarchy of MPL, and it
contains 1 or more Axes/Subplots. An Axes/Subplot represent an individual plot
or graphic.

So, for instance, the plots above contain a single Axes/Subplot, but are both,
separately, their own figure. Often times, it is needed to create multiple
subplots in a single figure, which MPL allows, such as: <a href="./data/MPL-SubPLot.png"><img src="./data/MPL-SubPlot.png" alt=Subplots width="300"/></a>

If you are wanting to create a plot that is not within this tutorial. I
recommend taking a look at the [MPL Example Gallery][MPL Example Gallery] and
the [MPL Tutorial Page][MPL Tutorial Page] for a load of examples and tutorials
on everything MPL.

# Module and other Helpful References<a name="Module-References"/>

* Plotting
    * [MatPlotLib](https://matplotlib.org/)
* Meteorological and Geographic Plotting
    * [Basemap](https://matplotlib.org/basemap/)
    * [Cartopy](https://scitools.org.uk/cartopy/docs/latest/)
    * [Gold-Standard Basemap Tutorial](https://basemaptutorial.readthedocs.io/en/latest/)
* Python NetCDF Tools
    * [Scipy Netcdf](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.io.netcdf.netcdf_file.html)
    * [Unidata's NetCDF4 Dataset](https://unidata.github.io/netcdf4-python/netCDF4/index.html)
    * [xArray](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.to_netcdf.html)
* Numpy
    * [Numpy Basics](https://docs.scipy.org/doc/numpy/user/index.html)
    * [Numpy Reference](https://docs.scipy.org/doc/numpy/reference/)

Helpful References and Guides
* [Anatomy Of MatplotLib](https://github.com/matplotlib/AnatomyOfMatplotlib)
* [MPL Tutorial Page][MPL Tutorial Page]
* [MPL Example Gallery][MPL Example Gallery]
* [MPL Color Maps Reference](https://matplotlib.org/users/colormaps.html)
* [MPL Plot Style Reference](https://matplotlib.org/gallery/style_sheets/style_sheets_reference.html)
* [Figure Documentation](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html)
* [Axes Documentation](https://matplotlib.org/api/axes_api.html)


# References & Credits<a name="Refs-and-Credits"/>
* [For examples and the Antomy of MatPlotLib Image used in and Introduction to MatPlotLib][1]
* [For help creating mpas_patches][2]
* [Anatomy of A Figure Image](https://matplotlib.org/gallery/showcase/anatomy.html)


[1]: https://github.com/matplotlib/AnatomyOfMatplotlib
[2]: https://github.com/lmadaus/mpas_python
[MPL Example Gallery]: https://matplotlib.org/gallery/index.html
[MPL Tutorial Page]: https://matplotlib.org/tutorials/index.html

# Todo:
1. Add more examples (espcially 2D examples)
   * Histogram, Barplots, Scatter Plots etc.
   * Add a Subplot example (possibly using grid spacing)
   * Add an example longitude or latitude 'slize' of a variable or two.
2. Clean up the helpful reference and guide list into one list and not two
