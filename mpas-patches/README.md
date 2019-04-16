MPAS Plotting Examples
======================

Run this script by running:
```
python mpas_plot_pressure.py /path/to/history-file.nc
```

<img src="../data/mpas-patches-example.png" alt="Pathces Example" width="700"/>

These examples will demonstrate how to plot individual polygons of the MPAS
unstructured Voronoi mesh. This method of plotting is very slow, but produces
very high resolution plots.

The example in this section is within the file `mpas_plot_pressure.py`. The
file `mpas_patches.py` is a helper script that is used to create a MatPlotLib
'patch collection' of each of the individual grid cells. 

Depending on the density of your mesh, creating this patch collection will take
some time; however, `mpas_patches.py` uses Python's Pickle module to save the
patch collection for later usages, which greatly increase the speed for future
plots.

Please feel free to use, edit and modify `mpas_patches.py` as you see fit.
