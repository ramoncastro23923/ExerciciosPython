#index      0      1       2
lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")

#chave:valor

dados = {"nome" : "Gabriel", "ano" : 1993, "valor_logico" : True}
print(dados)

dados["nome"] = "Pedro"
dados["idade"] = "32"

#A função popitem elimina o último item apenas da versão 3.7 e acima
dados.popitem()
print(dados)

# dados.update({"estado", "Rio de Janeiro"})
# dados.update({"Nome", "Ana"})   #Não é possível atualizar com .update por ser um dicionário