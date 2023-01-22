import matplotlib.pyplot as plt
import numpy as np

## Line plot with colored markers "Number of attendees" ##
time = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
numbers = [48411, 68626, 44676, 42571, 52609, 49499, 53772, 47371]
mydata = plt.plot(time, numbers, color='black', linewidth=1)
labels = ['Italy', 'USA', 'France', 'Japan / South Korea', 'Germany', 
'South Africa', 'Brazil', 'Russia']

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# remove y-label ticks & state the limits
plt.yticks([])
plt.ylim(35000,70000)
plt.xticks(np.arange(1990, 2022, 4))

# make labels for each point - trick with bars with none colors
for bar_i in plt.bar(time, numbers, color ='none'):
    plt.text(x=bar_i.get_x(), y=bar_i.get_height(),
             s=f"{bar_i.get_height()}",
             ha='right',
             color='black', fontweight='bold')

# plot scatters above line plot   
for i in range(len(time)):
    plt.scatter(time[i], numbers[i], label=labels[i])

plt.title('Average number of attendees per game in 1990-2018')
plt.legend(loc='lower center', shadow=False, ncol=4)
plt.savefig('figure_1_updated.jpeg', dpi=600, bbox_inches='tight')   
plt.show()

'''
plt.scatter(time[0], numbers[0], label='Italy')
plt.scatter(time[1], numbers[1], label='USA')
plt.scatter(time[2], numbers[2], label='France')
plt.scatter(time[3], numbers[3], label='Japan / South Korea')
plt.scatter(time[4], numbers[4], label='Germany')
plt.scatter(time[5], numbers[5], label='South Africa')
plt.scatter(time[6], numbers[6], label='Brazil')
plt.scatter(time[7], numbers[7], label='Russia')
'''
