import matplotlib.pyplot as plt

labels = ['63.29%', '15.21%', '4.89%']
sizes = [63.29, 15.21, 4.89]
colors = ['gold', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)  # destaca o primeiro pedaço

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Assegura que o gráfico seja desenhado como um círculo.
plt.title('Porcentagem dos Valores em Relação a 4.092,00')
plt.show()
