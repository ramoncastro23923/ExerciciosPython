
#       0123456
nome = "chicago"

print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6])

for x in range(10,0, -1):
    print(x)

nome = "chicago"
nome2 = "queens"

print(nome, end=" ")
print(nome2)

nome = "chicago \n"
nome2 = "queens"

print(nome)
print(nome2)

nome = "chicago"

for x in nome:
    print(x, end=" ") 

nome = "chicago"

for x in nome:
    print(x, end="#") 

x = 5
y = 0

x, y = y, x

print(x)
print(y)