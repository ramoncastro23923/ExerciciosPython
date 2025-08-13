lista = ["Ana", "Pedro", "Marta", "Clarice", "Beatriz", "Ana Clara"]
print(lista)

lista.sort(reverse = True)#com o sort organizando por ordem alfabetica, o reverse vai inverter
lista.sort(key = str.lower) 

print(lista)