# t,n,d,k = map(int,input().split())
d,k = map(int,input().split())
container = list(map(int,input().split()))
container.sort()
print(container)
minus = []
for i in range(len(container)-1) :
    minus.append(container[i+1] - container[i])
print(minus)
a = []
for i in range(len(minus)-1) :
    z,plus,l = 0,minus[i],i+1
    while plus < d :
        plus += minus[l]
        z += 1
        if l == len(minus)-1 :
            if minus[l] < d-minus[i] :
                z += 1
            break
        else:
            l += 1    
    a.append(z)
y = sorted(a)
print(a)
# for i in range(len(y)- k) :
del y[ : len(y)- k]
print(y)
b = []
for z in range(len(y)) :
    b.append(list(i for i, ele in enumerate(a) if ele == y[z]))
print(b)