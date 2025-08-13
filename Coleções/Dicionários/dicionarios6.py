#index      0      1       2
lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")

#chave:valor

dados = {"nome" : "Gabriel", "ano" : 1993, "valor_logico" : True}
print(dados)

dados["nome"] = "Pedro"
dados["idade"] = "32"

#A função popitem elimina o último item apenas da versão 3.7 e acima
# dados.popitem()
print(dados)
# dados.pop("valor_logico")
print(dados)
# del dados["ano"]
print(dados)
# dados.clear()
print(dados)

# dados.update({"estado", "Rio de Janeiro"})
# dados.update({"Nome", "Ana"})   #Não é possível atualizar com .update por ser um dicionário

for x in dados.values():
    print(x)

for x,y in dados.items():
    print(x, y)

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)

dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2)