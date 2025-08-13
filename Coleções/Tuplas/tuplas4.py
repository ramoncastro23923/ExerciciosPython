tupla = ("item1",)
tupla2 = ("a", "b")

tupla = ("item1", "item2", "item3")
print(tupla)

(x, y, z) = tupla
print("x:",x)
print("y:",y)
print("z:",z)

print(x)


tupla = ("item1", "item2", "item3", "item4", "item5")
print(tupla)

(a, *b, c) = tupla
print("a:",a)
print("b:",b)
print("c:",c)