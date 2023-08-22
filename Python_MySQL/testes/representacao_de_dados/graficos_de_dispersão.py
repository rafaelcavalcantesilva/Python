import matplotlib.pyplot as plt

plt.title("Gráfico de dispersão")#Função que dá um título para o gráfico

plt.xlabel("Eixo X")#Função de legenda do eixo x
plt.ylabel("Eixo Y")#Função de legenda do eixo y

x = [1, 3, 5, 7, 9]
y = [3, 7, 13, 10, 5]

plt.scatter(x, y, label="Meus Pontos", color="Red")#Função que cria o gráfico de dispersão, os argumentos representam as posições dos pontos. Label vai criar uma legenda para esses pontos e color vai selecionar uma cor específica para os pontos
plt.plot(x, y, color="Red")#Os gráficos de disperção podem ser criados juntamente com os de linha de forma que os pontos serão destacados e as linha ligarão esses pontos
plt.legend()#Adiciona as labels
# plt.show()
plt.savefig("figura1.png")#Função que salva o gráfico no formato desejado e na pasta onde o programa está sendo executado.Obs: Possui um parâmetro opcional chamado DPI que pode ser aumentado seu valor para melhorar a resolução da figura, sendo recomendado um valor de 300