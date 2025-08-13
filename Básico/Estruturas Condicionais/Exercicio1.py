idade = input("Quantos anos voce tem? ")
#por estar em "" o valor é em string
if int(idade) < 16:
    print("Menor")
elif int(idade) > 18: 
    print("Maior")
else: print("Emancipado")
