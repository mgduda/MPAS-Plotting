''' 
File - plot_ll.py
Author - Miles A. Curry (mcurry@ucar.edu)
Date - April 2019

This Python example will demeonstrate how to create a plot on a normal latitude
and longitude grid.

It will create a barbed plot of the surface winds, with a pcolor map of
pressure at the same level behind it.

'''

import os
import sys
import argparse

import numpy as np
from netCDF4 import Dataset

import matplotlib as mpl
mpl.use('Agg') # Tell MPL to not open a display
import matplotlib.pyplot as plt

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

# Initalize a Cyclyndrical Basemap Projection
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

# Convert the latitude and longitude from the netCDF dimension type
# to a more managable list of type floats
lats = list(map(float, lats))
lons = list(map(float, lons))

# To make vector fields we need a vectorfield. The meshgrid function will return a
# coordinate matrices from two our two latitude and longitude array!
x, y = np.meshgrid(lons, lats)

pressure = grid.variables['pressure'][:,:,:,0]
merdianalWinds = grid.variables['uReconstructMeridional'][:,:,:,0]
zonalWinds = grid.variables['uReconstructZonal'][:,:,:,0]

# When plotting a vector field, (ie barbs, quiver, or streamline), we'll need
# to downsample how many data values we actually plot. If not, we will the plot
# will be covered with the said vector field.
downsample_factor = 30

# Inspect the shapes of our variables if we want to:
print('x: ', type(x), x.shape)
print('y: ', type(y), y.shape)
print('merdinalWinds: ', merdianalWinds.shape)
print('merdinalWinds: ', zonalWinds.shape)



# Convert Pa to KPa
pressure = pressure / 1000.0 

# Choose the amount of color levels we want, and the range of pressure we want
# to display on the plot
MAX_PRESSURE = 100.0
MIN_PRESSURE = 70.0
N_COLOR_LEVELS = (MAX_PRESSURE - MIN_PRESSURE) * 5
color_levels = np.linspace(MIN_PRESSURE, MAX_PRESSURE, num=(N_COLOR_LEVELS))
color_ticks = np.arange(MIN_PRESSURE, MAX_PRESSURE+2, 2)


# Using a dictionary, set what type of barb we want for what wind speed.
barb_increments = {'half' : 5,
                   'full' : 10,
                   'flag' : 20}


# Loop through all of the times and create a plot of surface pressure and
# surface winds for each.
for t in range(len(time)):
    fig = plt.figure()
    ax = plt.gca()

    ax.set_title('Surface Winds and Surface Pressure at Time ('+str(t)+')')

    bmap.drawcoastlines()
    bmap.drawparallels(range(-90, 91, 30),
                       linewidth=1,
                       labels=[1,0,0,0],
                       color='b')
    bmap.drawmeridians(range(-180, 180, 45),
                       linewidth=1,
                       labels=[0,0,0,1],
                       color='b',
                       rotation=45) # Rotate the axis text labels by 45 deg

    # Plot barbs, choosing every downsample_factor data point rather then all
    # of them
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
                  levels=color_levels,
                  extend='both',
                  cmap=cm.plasma,
                  zorder=1)

    cbar = plt.colorbar()
    cbar.set_label('Pressure (KPa)')
    cbar.set_ticks(color_ticks)

    filename = 'plot_'+str(t)+'.pdf'
    plt.savefig(filename)
    plt.close()
