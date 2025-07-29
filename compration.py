# x = [i*2 for i in range(5)]
# print(x)
# x = [i * 2 for i in range(200) if i % 2 == 0]
# print(x)

# for i in range(200):
#     if i % 2 == 0:
#         i *2

# x = [1, 2, 3]
# y = [3, 4, 5]

# z = [(i,j) for i in x for j in y if i != j]
# print(z)


# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9],
#           ]
# v = []
# for i in range(3):
#     c = []
#     for j in matrix:
#         c.append(j[i])
#     v.append(c)
    
# print(v)

# x = ["mehdi", "mohammad", "ghatrani"]
# y = [1, 2, 3]
# x = {key:value for key in x for value in y if x.index(key) == y.index(value)}
# print(x)