"""

do while

Código para adivinhar um número

"""

palpite = 5
numero = 9

while True: #Nós executamos sem verificar
    print("Qual é o número correto? ")
    palpite = int(input())
    if palpite == numero:   # Estamos verificando nosso código
        print("Parabéns você acertou")
        break
    else:
        print("Você errou")
else:
    print("Você errou")
    print(bool(palpite))