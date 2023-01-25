import matplotlib.pyplot as plt
import numpy as np

## Bar chart horizontal "Top-8 stadiums on capacity" ##
labels = ['Estádio do Maracanã', 'Camp Nou', 'Estadio Azteca',
          'Wembley Stadium', 'Rose Bowl', 'Estadio Santiago Bernabéu',
          'Estadio Centenario', 'Lusail Stadium']
capacity = [200, 121, 115, 99, 94, 90, 90, 89]
plt.bar(np.arange(len(capacity)), capacity)

# make labels for each bar
for count, cap_data in enumerate(capacity):
    plt.text(y=cap_data+2,
             x=count-0.15,
             s=f"{cap_data}", color='black',
             va='center', fontweight='bold')
plt.title('Top-8 stadiums on capacity (in thousands)')
plt.xticks(np.arange(len(capacity)), labels = labels, fontsize = 10)

# get rid of the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# remove x-label ticks
plt.yticks([])

plt.savefig('figure_3_2.jpeg', dpi=600, bbox_inches='tight')   
plt.show()
