dicionario = {
    "nome": "Bruna",
    "idade": 27,
    "nacionalidade": "brasileira",
}

print(dicionario)
print(dicionario.get("idade")) 

if "idade" in dicionario:
    print("A chave idade existe")

print(dicionario.items())