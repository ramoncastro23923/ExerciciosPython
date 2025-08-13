lista = ["a", "b", "c"]
print(lista)

lista2 = lista
print(lista2)

#adicionando o "d" em ambas as listas

lista2.append("d")

print(lista)
print(lista2)

lista2 = lista.copy #faz o mesmo que o anterior.
print(lista2)

print(lista)
print(lista2)