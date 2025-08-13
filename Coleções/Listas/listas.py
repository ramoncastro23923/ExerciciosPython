lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista4 = [True, False]
print(lista4)

#SLICING:

#index      0       2       3      4       -> 5 elementos       
lista5 = [True, "chicago", 2.5, False, 4]
print(lista5)

print(type(lista5))
print(type(lista4))
print(type(lista3))
print(type(lista2))
print(type(lista))

print(lista[1])

print(lista5[-1])   #aconteceu uma rotação na lista
print(lista5[::])   #imprime tudo

print(lista5[1:]) #retorna do index que destacamos até o fim da lista
print(lista5[2:])
print(lista5[:3]) #retorna do começo da lista até o index -1
print(lista5[:4])
print(lista5[1:4:1])

# FUNÇÕES - COLEÇÕES

lista2 = lista2 + lista3
print(lista2)

