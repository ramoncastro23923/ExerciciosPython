#   index   0           1       2       3       4           5
lista = ["gato", "cachorro", "peixe","cavalo","tubarão","girafa"]
print(lista)

print(type(lista))
print(lista[1])

lista[1] = 'cavalo'
print(lista)

lista[1:4]  = ["águia", "morcego", "elefante"]
print(lista)

lista[1:2]  = ["águia", "elefante"]  
print(lista)

print(lista[1])
print(lista[2])
print(lista[3])

lista[1:5] = ["tubarão"]
print(lista)