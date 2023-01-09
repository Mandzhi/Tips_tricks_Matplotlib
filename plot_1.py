import matplotlib.pyplot as plt

## Line plot with colored markers "Number of attendees" ##
time = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
numbers = [48411, 68626, 44676, 42571, 52609, 49499, 53772, 47371]
mydata = plt.plot(time, numbers, color='black', linewidth=1)
#markers = ['*', 'x', 'v', '+', '^', 's', 'o', '<']
labels = ['Italy', 'USA', 'France', 'Japan / South Korea', 'Germany', 'South Africa', 'Brazil', 'Russia']

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# remove y-label ticks
plt.yticks([])

# labels
for bar_i in plt.bar(time, numbers, color ='none'):
    plt.text(bar_i.get_x() + bar_i.get_width()/2, bar_i.get_height()-0.5, str(int(bar_i.get_height())), ha='right', color='black', fontweight='bold')

#data  
for i in range(len(time)):
    plt.scatter(time[i], numbers[i], label=labels[i])#, marker=markers[i])
plt.title('Average number of attendees per game in 1990-2018')
plt.legend(loc='lower center', shadow=False, ncol=4)
plt.savefig('figure_1.jpeg', dpi=600, bbox_inches='tight')   
plt.show()
