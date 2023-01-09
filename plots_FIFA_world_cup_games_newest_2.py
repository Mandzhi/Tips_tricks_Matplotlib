import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

plt.xkcd()

# Four axes, returned as a 2d-array
fig, ax = plt.subplots(2,2, figsize=(18, 12))

## Line plot with colored markers "Number of attendees" ##
time = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
numbers = [48411, 68626, 44676, 42571, 52609, 49499, 53772, 47371]
mydata = ax[0,0].plot(time, numbers, color='black', linewidth=1, alpha=0.5, linestyle = '--')
markers = ['*', 'x', 'v', '+', '^', 's', 'o', '<']
labels = ['Italy', 'USA', 'France', 'Japan / South Korea', 'Germany', 'South Africa', 'Brazil', 'Russia']

# get rid of the frame
for spine in ax[0,0].spines.values():
    spine.set_visible(False)

# remove y-label ticks
ax[0,0].set_yticks([])

# labels
for bar_i in ax[0,0].bar(time, numbers, color ='none'):
    ax[0,0].text(bar_i.get_x() + bar_i.get_width()/20, bar_i.get_height()-0.8, str(int(bar_i.get_height())), ha='right', color='black', fontsize=12)

#data  
for i in range(len(time)):
    ax[0,0].scatter(time[i], numbers[i], label=labels[i], marker=markers[i])
ax[0,0].set_title('Average number of attendees per game in 1990-2018')
ax[0,0].legend(loc='lower center', shadow=False, ncol=4)
# data from https://www.statista.com/statistics/264441/number-of-spectators-at-football-world-cups-since-1930/

## Pie chart "Coutries with the most FIFA World Cup titles" ##
label_list = ('Brazil','Germany','Italy','Argentina','Uruguay','France','England','Spain')
freq = [5, 4, 4, 3, 2, 2, 1, 1]
colors = ['darkorchid', 'royalblue', 'lightsteelblue', 'silver', 'sandybrown', 'lightcoral', 'seagreen', 'salmon']
explode = (0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1)
ax[0,1].pie(freq, explode=explode, labels=label_list, colors=colors, autopct= lambda p : '{:,.0f} ({:.2f}%)'.format(p * sum(freq)/100, p), textprops={'fontsize': 12}) 
ax[0,1].set_title('Countries with the most FIFA World Cup titles')

## Bar chart horizontal "Top-8 stadiums on capacity" ##
labels = ['Estádio do Maracanã', 'Camp Nou', 'Estadio Azteca', 'Wembley Stadium', 'Rose Bowl', 'Estadio Santiago Bernabéu', 'Estadio Centenario', 'Olympiastadion']
capacity = [200, 121, 115, 99, 94, 90, 90, 86]
mybars = ax[1,0].barh(np.arange(len(capacity)), capacity)

# make labels for each bar
for i, v in enumerate(capacity):
    ax[1,0].text(v, i, " "+str(v), color='black', va='center', fontweight='bold')
ax[1,0].set_title('Top-8 stadiums on capacity (in thousands)')
ax[1,0].set_yticks(np.arange(len(capacity)))
ax[1,0].set_yticklabels(labels, fontsize = 10)

# get rid of the frame
for spine in ax[1,0].spines.values():
    spine.set_visible(False)

# remove x-label ticks
ax[1,0].set_xticks([])

## Map with labels ##
ax[1,1].set_title('Geography of the FIFA World Cups')
map = Basemap(projection='robin', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lon_0 = 0, lat_0 = 0)

# draw coastlines, country boundaries, fill continents
map.drawmapboundary(fill_color='#85A6D9')
map.drawcoastlines(color='#6D5F47', linewidth=.4)
map.drawcountries(color='#6D5F47', linewidth=.4)

# draw lat/lon grid lines every 30 degrees
map.drawmeridians(np.arange(-180, 180, 30), color='#bbbbbb')
map.drawparallels(np.arange(-90, 90, 30), color='#bbbbbb')

shapefile = 'ne_110m_admin_0_countries'
cols = ['team_name', 'team_code', 'count']

df = pd.read_csv('data_football.csv', usecols=cols)
df.set_index('team_code', inplace=True)
df = df.dropna()
print(df)

cm = plt.get_cmap('Reds')
scheme = [cm(i/df['count'].nunique()) for i in range(df['count'].nunique()+1)]
print(df.sort_values('count', ascending=False))

map.readshapefile(shapefile, 'units', color='red', linewidth=.2)
for info, shape in zip(map.units_info, map.units):
    iso3 = info['ADM0_A3']
    if iso3 not in df.index:
        color = 'rosybrown'
    else:
        color = scheme[int(df.loc[iso3]['count'])]
    patches = [Polygon(np.array(shape), True)]
    pc = PatchCollection(patches)
    pc.set_facecolor(color)
    ax[1,1].add_collection(pc)

plt.savefig('cover_figure_draw.jpeg', dpi=1200) #, bbox_inches='tight')            
plt.show()
