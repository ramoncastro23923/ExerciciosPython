#Identificando a tipificação da variavel
uf = ("JAN", "FEV")
print(type(uf))

#Identificando o tipo da variavel 
tupla = ("item 1")
print(tupla)
print(type(tupla))

#identificando uma tupla, ela não é definida unicamente por parênteses mas sim pelas vírgulas.

tupla = "item 1", "item 2", "item 3", "item 4"
print(tupla)
print(type(tupla))

#Adicionando com append um item na tupla

tupla = ("item 1", "item 2", "item 3", "item 4")
lista = list(tupla)
print(tupla)
print(lista)

lista.append("item 5")
print(lista)

tupla = tuple(lista)
print(tupla)

#Removendo um item da tupla

tupla = ("item 1", "item 2", "item 3", "item 4")
lista = list(tupla)
print(tupla)
print(lista)

lista.pop
print(lista)

tupla = tuple(lista)
print(tupla)

#Portanto, só é possível editar um item da tupla atráves de um append ou um pop

