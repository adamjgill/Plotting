import matplotlib.pyplot as plt
import matplotlib.mlab as ml
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas as pd
import numpy as np

f = 'lat_log_hieght.csv'

top_map = pd.read_csv(f, delimiter=',',header=1, names=['Latitude','Longitude','Elevation'])

#top_map.index = top_map['Elevation']

x = np.array(top_map['Latitude'])
y = np.array(top_map['Longitude'])
z = np.array(top_map['Elevation'] * 3.28)

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))

X, Y = np.meshgrid(xi, yi)

Z = ml.griddata(x, y, z, xi, yi, interp='linear')

#Z = np.array[[z,x],[z,y]]

fig = plt.figure()
ax = fig.gca(projection='3d')
#cs = plt.contourf(X, Y, Z, 500)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()
