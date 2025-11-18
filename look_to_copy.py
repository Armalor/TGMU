import copy

a = 10
b = a

# print(id(a), id(b), id(a) == id(b))

a += 100

# print(a, b, id(a), id(b), id(a) == id(b))


aa = [1, 2, 3]

bb = copy.deepcopy(aa)
print(aa, bb, id(aa) == id(bb))

# bb += [4]
# bb = bb + [4]
# bb.append(4)

print(aa, bb, id(aa) == id(bb))
