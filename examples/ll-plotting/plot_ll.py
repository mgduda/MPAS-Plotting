''' 
File - plot_ll.py
Author - Miles A. Curry (mcurry@ucar.edu)
Date - April 2019

This Python example will demeonstrate how to create a plot on a normal latitude
and longitude grid.

It will create a barbed plot of the surface winds, with a pcolor map of
pressure at the same level.

'''

import os
import sys
import argparse

import numpy as np
from netCDF4 import Dataset

''' By default matplotlib will try to open a display windows of the plot, even
though sometimes we just want to save a plot. Somtimes this can cause the
program to crash if the display can't open. The two commands below makes it so
matplotlib doesn't try to open a window
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

'''
cm = Color Map. Within the matplotlib.cm module will contain access to a number
of colormaps for a plot. A reference to colormaps can be found at:

    - https://matplotlib.org/examples/color/colormaps_reference.html
'''
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

parser = argparse.ArgumentParser()
parser.add_argument('file', 
                    type=str, 
                    help='''File you want to plot from''')

args = parser.parse_args()
file = args.file

if not os.path.isfile(file):
    print("That file was not found :(")
    sys.exit(-1)


# Open the mesh using NetCDF4 Dataset.
grid = Dataset(os.path.join(file), 'r')

'''
Now that we have the NetCDF Variable, we can insepct its contents in Python by
printing out a number of its features.

Dimensions:
print(grid.dimsensions.keys())

Variables:
print(grid.variables.keys())


'''

for attr in grid.ncattrs():
    print(attr)


bmap = Basemap(projection='cyl', 
               llcrnrlat=-90,
               urcrnrlat=90,
               llcrnrlon=-180,
               urcrnrlon=180,
               resolution='l')
    
# Pull out our dimensions
time = grid.dimensions['Time']
lats = grid.variables['latitude']
lons = grid.variables['longitude']

lats = list(map(float, lats))
lons = list(map(float, lons))

x, y = np.meshgrid(lons, lats)


# Pull out all the varibles we desire at the surface level
# Here we are pulling out all the times across the whole domain at level
# vertical level 0.
pressure = grid.variables['pressure'][:,:,:,0]
merdianalWinds = grid.variables['uReconstructMeridional'][:,:,:,0]
zonalWinds = grid.variables['uReconstructZonal'][:,:,:,0]

print('x: ', type(x), x.shape)
print('y: ', type(y), y.shape)
print('merdinalWinds: ', merdianalWinds.shape)
print('merdinalWinds: ', zonalWinds.shape)


downsample_factor = 30

# Convert Pa to KPa
pressure = pressure / 1000.0 

# Choose our Own Color Levels
MAX_PRESSURE = 105
MIN_PRESSURE = 60
NUM_COLOR_LEVELS = (MAX_PRESSURE - MIN_PRESSURE) * 4
contour_level_dif = (MAX_PRESSURE - MIN_PRESSURE) / NUM_COLOR_LEVELS
color_levels = []

for i in range(NUM_COLOR_LEVELS):
    color_levels.append(MIN_PRESSURE + i * contour_level_dif)

barb_increments = {'half' : 5,
                   'full' : 10,
                   'flag' : 40}

for t in range(len(time)):
    fig = plt.figure()
    ax = plt.gca()

    ax.set_title('Surface Winds and Surface Pressure')

    bmap.drawcoastlines()
    bmap.drawlsmask()
    bmap.drawparallels(range(-90, 91, 30), 
                       linewidth=1, 
                       labels=[1,0,0,0],
                       color='b')
    bmap.drawmeridians(range(-180, 180, 45),
                      linewidth=1, 
                      labels=[0,0,0,1],
                      color='b',
                      rotation=45)

    bmap.barbs(x[::downsample_factor, ::downsample_factor], 
               y[::downsample_factor, ::downsample_factor], 
               merdianalWinds[t,::downsample_factor,::downsample_factor], 
               zonalWinds[t,::downsample_factor,::downsample_factor],
               pivot='middle',
               length=4,
               zorder=2,
               barb_increments=barb_increments
               )

    bmap.contourf(x,
                  y,
                  pressure[t,:,:],
                  color_levels,
                  cmap=cm.plasma,
                  zorder=1)

    cbar = plt.colorbar()
    cbar.set_label('Pressure (KPa)')
     

    filename = 'plot_'+str(t)+'.pdf'
    plt.savefig(filename)
    plt.close()


