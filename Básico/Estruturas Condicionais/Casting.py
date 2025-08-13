#int

# fazer isso acaba tirando a precisão dos dados, transformando um float e um string em simplesmente 2.
x = int(2)
y = int(2.8)
z = int('2')

print(x, y, z)

#forçar todos a serem float

a = float(2)
b = float(2.8)
c = float('2')

print(a, b, c)

t = str('s1')
r = str(2)
z = str(2.3)

print("A variavel t eh do tipo: ", type(t))
print("A variavel r eh do tipo: ", type(r))
print("A variavel z eh do tipo: ", type(z))