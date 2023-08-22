import matplotlib.pyplot as plt

data = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in data:
    try:
        x.append(int(i.split(";")[0]))
        y.append(int(i.split(";")[1].replace("\n", "")) / 100000000)
    except:
        continue

plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.bar(x, y, color="#d3d3d3")
plt.plot(x, y, linestyle="--", color="k")
#plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)