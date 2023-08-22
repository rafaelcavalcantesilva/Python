lista = [9,5,7,1,3,2,40]

newLista = list()

while len(newLista) < len(lista):
    prev = max(lista)
    for i in lista:
        if not i in newLista:
            if i < prev:
                prev = i
    newLista.append(prev)
        

print(newLista)