import matplotlib.pyplot as plt

plt.title("Gráfico de Barras")#Função que dá um título para o gráfico

plt.xlabel("Eixo X")#Função de legenda do eixo x
plt.ylabel("Eixo Y")#Função de legenda do eixo y

x1 = [1, 3, 5, 7, 9]
y1 = [3, 7, 13, 21, 31]

x2 =[2, 4, 6, 8, 10]
y2 = [31, 21, 13, 7, 3]
#Função que cria o gráfico de barras, o primeiro argumento representa quais são as barras e o segundo argumento representa  a altura de cada barra
plt.bar(x1, y1, label="Grupo1")
plt.bar(x2, y2, label="Grupo2")
plt.legend()#Adiciona os labels como legendas no gráfico para cada cor
plt.show()