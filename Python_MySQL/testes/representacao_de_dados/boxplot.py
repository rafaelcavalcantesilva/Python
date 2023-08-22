import matplotlib.pyplot as plt
import random

array = []

for i in range(100):
    num = random.randint(0, 50)#Seleciona um número aleatório entre 0 e 50
    array.append(num)

plt.boxplot(array)#Função que gera o boxplot a partir de uma linsta de valores
plt.title("Boxplot")
plt.show()