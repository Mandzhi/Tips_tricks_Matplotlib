import matplotlib.pyplot as plt
import numpy as np

## Bar chart horizontal "Top-8 stadiums on capacity" ##
labels = ['Estádio do Maracanã', 'Camp Nou', 'Estadio Azteca',
          'Wembley Stadium', 'Rose Bowl', 'Estadio Santiago Bernabéu',
          'Estadio Centenario', 'Olympiastadion']
capacity = [200, 121, 115, 99, 94, 90, 90, 86]
mybars = plt.barh(np.arange(len(capacity)), capacity)

# make labels for each bar
for i, v in enumerate(capacity):
    plt.text(v, i, " "+str(v), color='black', va='center',
                 fontweight='bold')
plt.title('Top-8 stadiums on capacity (in thousands)')
plt.yticks(np.arange(len(capacity)), labels = labels, fontsize = 10)
#plt.ylabel(labels, fontsize = 10)

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# remove x-label ticks
plt.xticks([])

plt.savefig('figure_3.jpeg', dpi=600, bbox_inches='tight')   
plt.show()
