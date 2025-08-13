# Tamanho das listas

lista1 = [2.0, 3.5, 4.7]
print(lista1)

lista2 = [1, 5, 9, 11, 15]
print(lista2)

#index      0       1       2
lista3 = ["Nome", "Nome2", "Nome"]

print(len(lista3))

print(len(lista1))
print(len(lista2))

# Funções que só podem ser utilizadas com tipos de dados numéricos

print(sum(lista1)) #somatório

print(max(lista1)) #printa o maior valor da lista

print(min(lista1)) #printa o menor valor da lista

# FUNÇÕES - LIST

nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

lista7 = list(range(10))
print(lista7)

lista8 = list("Curso de Python")
print(lista8)

elemento = 8

if elemento in lista7:
    print("Este elemento esta dentro da lista")