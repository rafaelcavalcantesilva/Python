entrada = open("16s_bacteria.fasta").read()
saida = open("bacteria.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n", "")
for i in range(len(entrada)-1):
    cont[entrada[i] + entrada[i+1]] += 1

saida.write("<div>")

i = 1
for x in cont:
    transparencia = cont[x]/max(cont.values())
    transparencia = str(transparencia)
    saida.write(f"<div style='width:100px; border:1px solid #111; height:100px; float:left; color:#fff; background-color:rgba(0, 0, 0, {transparencia});'>{x}</div>")

    if i % 4 == 0:
        saida.write("<div style='clear:both;'></div>")
    i += 1
saida.close()