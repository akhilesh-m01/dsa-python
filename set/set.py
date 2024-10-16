s1 = set()
print(s1)

s1.add(1)
print(s1)

s2 = s1.copy()
print(s2)

s2.clear()
print(s2)

s11 = {1,2,9,0}
s21 = {3,4,5,1}

x = s11 - s21
print(x)

x2 = s11.difference(s2,s21)
print(x2)

y = s11 & s21
print(y)

y2 = s11.intersection(s21)
print(y2)

s11.discard(9)
print(s11)