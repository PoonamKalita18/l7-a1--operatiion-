L = ['apple', 'banana', 'mango', 'guava', 'pineapple']

print(len(L))
print(L[0])
print(L[-1])

L.append('strawberry')
print(L)

L.remove('guava')
print(L)

L.sort()
print(L)

L.pop(1)
print(L)

L.reverse()
print(L)

print("mutliply the list twice",L*2)

L = L[:4]
print(L)

L.clear()
print(L)
