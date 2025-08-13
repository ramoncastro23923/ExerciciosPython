#index      0       1       2
lista = ["carro","barco","avião"]
print(lista)

lista.insert(0, "bicicleta")

print(lista)

lista.append(["bicicleta","navio"]) #
lista

print(lista)
print(len(lista))

for x in range(len(lista)):
    print(x, lista[x])
