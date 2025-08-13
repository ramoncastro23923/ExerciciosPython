lista = ["a", "b", "c"]
lista2 = [1,4,2]

"""lista = lista + lista2 
print(lista)"""

lista.extend(lista2) #Estende a lista acrescentando a lista 2
print(lista)

for x in lista2:
    lista.append(x)  #Adiciona um argumento por vez através do append.

    print(lista)