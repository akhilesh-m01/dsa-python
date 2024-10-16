d1 = dict()
# print(d1)

d1['a'] = 1
print(d1)

d1[1] = 2
d1[0] = 3
# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# print(type(d1.items())) # dict_items

print(d1)
d1.pop(0)
print(d1)

d1.update({'ml':"need"}) #adds at the end
print(d1)

x = d1.setdefault("l","want") #is the value of key exists then it returns that value else it passed value with an update in the dict

print(x)
print(d1)

d2 = d1.copy()
print(d2)

d2.clear()
print(d2)

d1.popitem() # removes the last item 
print(d1)

d1.pop('a')
print(d1)










