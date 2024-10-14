t1 = ("ak","mk")
# print(t1)

t2 = tuple()
# print(t2)

t3 = ("Akhilesh",True,1,20)
# print(t3)

t4= 4,
# print(t4)

t5 = (1,2,3)

a,b,c = 1,2,3
# print(a+b+c)

# tuples are immutable but you can change in the following ways

# 1.create a new tuple and use + operator to append it
t6 = t5 + (0,)
# print(t6)

# 2. convert to list and make changes to it
lx = list(t6)
# lx.append(34)
# print(lx)
t7 = tuple(lx)
# print(t7)


# tuple to string
s1 = ('a','k','h','i','l','e','s','h')
s2 = ''.join(s1)
# print(s2)

# print(s1[-4])

t8 = (1,2,3,4,6,3,4)

print(t8.count(3))

print(t8.index(3))

print(t8.index(3,3))

