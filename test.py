a = [1, 2,2,1,2]
b = []
b.append(list(i for i, ele in enumerate(a) if ele == 2))
print(b)