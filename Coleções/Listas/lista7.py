lista = ["carro", "barco", "avião"]
print(lista)

#lista.remove("barco")
#del lista[0] deleta item especifico da lista

carrinho_de_compras = ["produto1","produto2","produto3"]
# carrinho_de_compras.clear() #Deleta a lista
carrinho_de_compras.sort() #Enumera os itens em ordem alfabética ou crescente

print(carrinho_de_compras)

for x in range(len(carrinho_de_compras)):
    print(x, carrinho_de_compras[x])
