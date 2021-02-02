##  GCD 합  ##

from math import gcd

t = int(input())
li = [[]*t for i in range(t)]
for i in range(t) :
    li[i] = list(map(int, input().split()))

for i in range(t) :
    box = 0
    for k in range(1,li[i][0]) :
        z=k+1
        while z < li[i][0] + 1 :
           box += gcd(li[i][k],li[i][z])  
           z += 1
    print(box)