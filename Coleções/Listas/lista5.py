#index      0       1       2
lista = ["carro","barco","avião"]
print(lista)

lista.pop() #Semelhante a Append, mas remove elementos, no caso, o último da lista.
lista.remove("barco") #Dentro de uma lista remove um elemento especifico.

print(lista)

for x in range(len(lista)):
    print(x, lista[x])