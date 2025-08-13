"""
Python - Comandos de controle condicional

if, else e elif -> (else if)

"""

x = 20
y = 3

if y > x:
    print("y eh maior do que x")
elif y < x: 
    print("y eh menor do que x")
else:
    print("y nao eh menor nem maior que x")

print("Código fora do bloco condicional")
print(y>x)
print(y<x)

#Código exemplo encurtado

a = 5
b = 8
c = 2

"""if a > b: print("b eh maior que a")
    print("codigo fora do bloco if")"""

print("B") if b < a else print("A")

if a > b:
    if a > c:
        print("A eh maior que b e que c")
        