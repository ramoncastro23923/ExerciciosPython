dicionario = {
    "nome": "Bruna",
    "idade": 27,
    "nacionalidade": "brasileira",
}

print(dicionario)

# print(dicionario("idade"))           Esse print não funciona (erro object is not callable) por ser um dicionario
print(dicionario.get("idade"))         #Portanto, precisamos usar um GET

#Métodos utilizados apenas para dicionário

#Dunder Methods:

#__contains__: Verifica se uma chave existe no dicionário (usado pelo operador in).
#__delitem__: Remove um item com uma chave específica (usado pelo comando del).
#__getitem__: Acessa um valor pela chave (usado pela notação dicio[chave]).
#__iter__: Retorna um iterador sobre as chaves do dicionário.
#__len__: Retorna o número de itens no dicionário (usado pela função len()).
#__repr__: Retorna uma representação em string do dicionário (usado pela função repr()).

#Métodos de dicionário

#clear: Remove todos os itens do dicionário.
#copy: Retorna uma cópia superficial do dicionário.
#fromkeys: Cria um novo dicionário com chaves de uma sequência e valores padrão.
#get: Retorna o valor associado a uma chave, ou um valor padrão se a chave não existir.
#items: Retorna uma visão dos pares (chave, valor) do dicionário.
#keys: Retorna uma visão das chaves do dicionário.
#pop: Remove e retorna o valor associado a uma chave.
#popitem: Remove e retorna um par (chave, valor) arbitrário.
#setdefault: Retorna o valor associado a uma chave, ou insere a chave com um valor padrão se ela não existir.
#update: Atualiza o dicionário com pares (chave, valor) de outro dicionário ou iterável.
#values: Retorna uma visão dos valores do dicionário.


print(dicionario.keys())
print(len(dicionario))
print(dicionario.values())

