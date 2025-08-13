
lista = ["item 1", "item 2"]
print(lista)
lista[0] = "item 3"

print(lista)

#Agora vamos transformar esse algoritmo em um sistema com tupla

# tupla = ("item 1", "item 2")
# print(tupla)
# tupla[0] = "item 3"
# print(tupla)

#É impossível, porque a tupla é imutável. Para isso, temos que modificar o código desse modo:

tupla = ("item 1", "item 2")
print(tupla)

tupla = ("item 3", "item 4", "verde")
print(tupla)