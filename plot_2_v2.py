import matplotlib.pyplot as plt

## Pie chart "Coutries with the most FIFA World Cup titles" ##
# data
label_list = ('Brazil','Germany','Italy','Argentina','Uruguay',
              'France','England','Spain')
freq = [5, 4, 4, 3, 2, 2, 1, 1]

# customize colors & gaps between pie parts
#colors = ['darkorchid', 'royalblue', 'lightsteelblue', 'silver', 'sandybrown', 'lightcoral', 'seagreen', 'salmon']
#explode = (0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1)

# building chart
plt.pie(freq,
        #explode=explode,
        labels=label_list, #colors=colors,
        autopct=lambda p : '{:,.0f} ({:.2f}%)'.format(p * sum(freq)/100, p),
        textprops={'fontsize': 12}) 
plt.title('Countries with the most FIFA World Cup titles')
plt.savefig('figure_2_1.jpeg', dpi=600, bbox_inches='tight')   
plt.show()
