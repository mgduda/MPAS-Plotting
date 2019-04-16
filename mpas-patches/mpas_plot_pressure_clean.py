''' 
File - mpas_plot_pressure.py
Author - Miles A. Curry (mcurry@ucar.edu)
Date - April 2019

This python file provides an example of plotting an MPAS field onto an MPAS
mesh. This plot produces pcolor like plots by created a collection of polygons
(MatPltLib patches) of the MPAS mesh. Thus, for large meshes this routine is
very slower.

However, this file has been provided with the `mpas_patches.py` which provides
a function `get_mpas_patches` that will autmoatcially produce such polygons as
a 'patch collection'. For large meshes, producing the patch collection is
costly and timely so `get_mpas_patches` will produce a python 'pickle' file, so
that it will only need to be produced once. This will greatly speed up the time
it takes to on subsequent visualiations.

Note: This 'clean' version of this example contains less comments and documentation,
but is the same as plot_ll.py.

This file was created with great help and reference from:
* https://github.com/lmadaus/mpas_python

'''

import os
import sys
import argparse

from netCDF4 import Dataset

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

from mpas_patches import get_mpas_patches
    
parser = argparse.ArgumentParser()

parser.add_argument('file', 
                    type=str, 
                    help='''File you want to plot from''')
parser.add_argument('-v',
                    '--var', 
                    type=str,
                    default='pressure',
                    help='''Variable you want to plot from that file''')

args = parser.parse_args()
variable = args.var
file = args.file

# Open the NetCDF file and pull out the var at the given levels.
# Check to see if the mesh contains the variable
if not os.path.isfile(file):
    print("That file was not found :(")
    sys.exit(-1)

# Open the mesh using NetCDF4 Dataset.
mesh = Dataset(os.path.join(file), 'r')

# Check to see the variable is in the mesh
if variable not in mesh.variables.keys(): 
    print("That variable was not found in this mpas mesh!")
    sys.exit(-1)

# Pull the variable out of the mesh. Now we can manipulate it any way we choose
# do some 'post-processing' or other meteorological stuff
var = mesh.variables[variable]

# Create or get the patch file for our current mesh
patch_collection = get_mpas_patches(mesh, pickleFile=None)

# Initalize Basemap
bmap = Basemap(projection='cyl', 
               llcrnrlat=-90,
               urcrnrlat=90,
               llcrnrlon=-180,
               urcrnrlon=180,
               resolution='l')


color_map = cm.gist_ncar
style = 'ggplot'

'''
Make plots at vertical levels that is specified the range below, not this will
be vertical plots, 0, 1, 2, 3, and 4 and for all the times in this mesh file
(if there are any).
'''
levels = range(5)
times = [0]
for l in levels:
    for t in times:

        print("Creating a plot of ", variable, " at ", l, " level and time", t)
        fig = plt.figure()
        ax = plt.gca()

        bmap.drawcoastlines()

        bmap.drawparallels(range(-90, 90, 30), 
                           linewidth=1, 
                           labels=[1,0,0,0],
                           color='b')
        bmap.drawmeridians(range(-180, 180, 45),
                          linewidth=1, 
                          labels=[0,0,0,1],
                          color='b',
                          rotation=45)

        patch_collection.set_array(var[t,:,l])
        patch_collection.set_edgecolors('')         # No Edge Colors
        patch_collection.set_antialiaseds(False)    # Blends things a little
        patch_collection.set_cmap(color_map)        # Select our color_map

        # Now apply the patch_collection to our axis (ie plot it)
        ax.add_collection(patch_collection)

        cbar = plt.colorbar(patch_collection)
        cbar.set_label('Pressure (Pa)')
        

        # Create the title as you see fit
        plt.title(variable+' at time '+str(t)+' and at level '+str(l))
        plt.style.use(style) # Set the style that we choose above

        plt.savefig(variable+'_'+str(t)+'_'+str(l)+'.png')
        patch_collection.remove()
        plt.close(fig)
