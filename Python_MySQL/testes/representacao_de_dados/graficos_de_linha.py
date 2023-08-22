import matplotlib.pyplot as plt

plt.title("Meu Primeiro Gráfico em Python")#Função que dá um título para o gráfico

plt.xlabel("Eixo X")#Função de legenda do eixo x
plt.ylabel("Eixo Y")#Função de legenda do eixo y

x = [1, 2, 3, 4, 5]
y = [3, 7, 13, 21, 31]
plt.plot(x, y) #Essa é a função que cria o Gráfico de linhas, os dois argumentos que ela aceita são duas listas que serão os pontos presentes no gráfico. A combinação de x e y é feita de acordo com com o índice dos valores nas listas x e y
plt.show()#Essa função exibe o gráfico criado

