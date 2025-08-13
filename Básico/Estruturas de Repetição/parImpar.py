"""
Como descobrir se um número é impar ou par
"""

#0,2,4,6,8,10,12,14...

#0/2. 2/2. 4/2... divisão inteira, 1, 0.

print(130 * "-")
numero = int(input("Insira um numero para saber se o mesmo é par: "))
if (numero % 2) == 0:
    print(f"{numero} é um número par")
else:
    print(f"{numero} é um número impar")
print(130 * "-")