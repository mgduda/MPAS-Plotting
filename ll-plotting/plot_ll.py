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

''' By default matplotlib will try to open a display windows of the plot, even
though sometimes we just want to save a plot. Somtimes this can cause the
program to crash if the display can't open. The two commands below makes it so
matplotlib doesn't try to open a window
'''
import matplotlib as mpl
mpl.use('Agg')
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


'''  Initialize Basemap

Basemap handles all things map projections. It can translate between one map
projection to another, drawcoastliens, draw latitude liens and a number of map
related things. I encourage you to check out this tutorial here:

    - https://basemaptutorial.readthedocs.io/en/latest/

As well as the official documentation

    - https://matplotlib.org/basemap/index.html
    
'''
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

# This will convert the latitude and longitude from the netCDF dimension type
# to a more managable list of type floats
lats = list(map(float, lats))
lons = list(map(float, lons))

# To make vector fields we need a vectorfield. The meshgrid function will return a
# coordinate matrices from two our two latitude and longitude array!
x, y = np.meshgrid(lons, lats)

'''
If you wish, you can also inspect the metadata surrounding a variable in this
format below such as:

Printing its units:
```
print(grid.variables['pressure'].units)
```

and printing its dimensions:
```
print(grid.variables['pressure'].dimensions)


But, if we just wish to grab the actual values we can do the following:

Pull out all the varibles we desire at the surface level Here we are pulling
out all the times across the whole domain at level vertical level 0.
'''

pressure = grid.variables['pressure'][:,:,:,0]
merdianalWinds = grid.variables['uReconstructMeridional'][:,:,:,0]
zonalWinds = grid.variables['uReconstructZonal'][:,:,:,0]

# Inspect the shapes of our variables if we want to:
print('x: ', type(x), x.shape)
print('y: ', type(y), y.shape)
print('merdinalWinds: ', merdianalWinds.shape)
print('merdinalWinds: ', zonalWinds.shape)

# When plotting a vector field, (ie barbs, quiver, or streamline), we'll need
# to downsample how many data values we actually plot. If not, we will the plot
# will be covered with the said vector field.
downsample_factor = 30

# Convert Pa to KPa
pressure = pressure / 1000.0 

''' Create our own color bar if we choose too. We can choose to create the
upper and the lower limit of what will be colored, with everything above and
below being set to the highest and lowest colors. By setting the 'extend'
keyword equal to 'both'. We also have options to set extend to be 'neither',
'both', 'min', or 'max'.

Color_levels will be the number of color levels between the two values we
choose. So we could have colors for each whole value between a minimum and max
value, or we could even lump ranges into a color. (ie green for 1-10, blue for
10-20, etc.).

color_ticks represent the ticks (or marks) that appear on the color bar that
will show what colors are what values. Note with numpy arrange, you'll need to
go one step *over* the top value, as it is non-inclusive by default.
'''
MAX_PRESSURE = 100.0
MIN_PRESSURE = 70.0
N_COLOR_LEVELS = (MAX_PRESSURE - MIN_PRESSURE) * 5
color_levels = np.linspace(MIN_PRESSURE, MAX_PRESSURE, num=(N_COLOR_LEVELS))
color_ticks = np.arange(MIN_PRESSURE, MAX_PRESSURE+2, 2)



# Using a dictionary, set what type of barb we want for what wind speed.
barb_increments = {'half' : 5,
                   'full' : 10,
                   'flag' : 20}

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

    ''' As mentioned above, we are downsampling the number of barbs we want to
    create on our plot. We can downsample any pyton list by the following
    syntax: 
    ``` 
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    print(a[::2])
    >>[1, 3, 5, 7, 9]
    ```
    i.e. Skip every 2
    '''
    bmap.barbs(x[::downsample_factor, ::downsample_factor],
               y[::downsample_factor, ::downsample_factor],
               merdianalWinds[t,::downsample_factor,::downsample_factor],
               zonalWinds[t,::downsample_factor,::downsample_factor],
               pivot='middle',
               length=4,
               zorder=2,
               barb_increments=barb_increments
               )

    ''' We want the barbs to be on top of the contour plot. So set the zorder
    of the barbs to be 2 and the zorder of the contour plot to be 1.

    Note, that if we plot the barbs *after* we plot the contourf plot. The
    zorder will be correct. However, here it is shown as an introduction to
    zorder.
    '''

    bmap.contourf(x,
                  y,
                  pressure[t,:,:],
                  levels=color_levels,
                  extend='both',
                  cmap=cm.plasma,
                  zorder=1)


    ''' Turn on the colorbar. By default it will go to the veritical
    orientation and be placed to the right. If we want, we can move it to the
    bottom by using the following:

    cbar = plt.colorbar(orientation="horizontal")

    Note: If we remove the next three lines completly, the colorbar will not
    appear, but the colors to the data will still be applied.
    '''
    cbar = plt.colorbar()
    cbar.set_label('Pressure (KPa)')
    cbar.set_ticks(color_ticks)


    filename = 'plot_'+str(t)+'.png'
    plt.savefig(filename)
    plt.close()
