from collections import deque

q1 = deque(maxlen=9)
print(q1)

q1.append(1)
print(q1)

q1.appendleft(2)
print(q1)


q1.pop()
print(q1)

q1.append(3)#[2,3]
q1.popleft()
print(q1)


q1.extend([4,5,6])
print(q1)

q1.extendleft([99,12,1])
print(q1)



q1.append(10)
q1.append(11)
q1.appendleft(15)
print(q1)

print(q1.count(10))
print(q1.index(12))
q1.rotate(2)
print(q1)
