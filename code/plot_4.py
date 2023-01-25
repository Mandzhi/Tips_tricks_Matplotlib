import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

## Map with labels ##
fig, ax = plt.subplots(facecolor='white')
ax.set_title('Geography of the FIFA World Cups')
map = Basemap(projection='robin', llcrnrlat=-80,
              urcrnrlat=80,
              llcrnrlon=-180, urcrnrlon=180,
              lon_0 = 0, lat_0 = 0)

# draw coastlines, country boundaries, fill continents
map.drawmapboundary(fill_color='lightsteelblue')
map.drawcoastlines(color='tan', linewidth=0.4)
map.drawcountries(color='tan', linewidth=0.4)

# draw lat/lon grid lines every 30 degrees
map.drawmeridians(np.arange(-180, 180, 30), color='white')
map.drawparallels(np.arange(-90, 90, 30), color='white')

shapefile = 'ne_110m_admin_0_countries'
cols = ['team_name', 'team_code', 'count']

df = pd.read_csv('data_football.csv', usecols=cols)
df.set_index('team_code', inplace=True)
df = df.dropna()
print(df)

cm = plt.get_cmap('Reds')
scheme = [cm(i/df['count'].nunique()) for i in range(df['count'].nunique()+1)]
#print(df.sort_values('count', ascending=False))

map.readshapefile(shapefile, 'units', color='red', linewidth=0.2)
for info, shape in zip(map.units_info, map.units):
    iso3 = info['ADM0_A3']
    if iso3 not in df.index:
        color = 'rosybrown'
    else:
        color = scheme[int(df.loc[iso3]['count'])]
    patches = [Polygon(np.array(shape), True)]
    pc = PatchCollection(patches)
    pc.set_facecolor(color)
    ax.add_collection(pc)

cb = matplotlib.colorbar.ColorbarBase(ax=fig.add_axes([0.35, 0.1, 0.3, 0.05]),
                                      cmap=matplotlib.colors.ListedColormap(['rosybrown',
                                                                             'tomato',
                                                                             'darkred']),
                                      boundaries=range(3), orientation='horizontal')

plt.savefig('figure_4.jpeg', dpi=600, bbox_inches='tight')            
plt.show()
