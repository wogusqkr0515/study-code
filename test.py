# aa = [3,3,2,3]
# i = 0
# # while i < len(aa) :
# #     if aa.count(3) >= 2 :
# #         print(aa.index(3,i,len(aa) + 1))
# #         print(i)
# #         i = aa.index(3) + 1
# #     else :
# #         print(aa.index(3))
# #         break
# # # print(aa.index(,4,len(aa) + 1))
# for k in range(aa.count(3)) :
#     print(aa.index(3,i,len(aa) + 1))
#     i = aa.index(3,i,len(aa) + 1) + 1
'''
comp = [6, 3, 5, 6, 7]
compSort = [6]
indexComp = []
minC = [30, 20, 0, 20, 0, 40]
z = 0
for k in range(comp.count(compSort[0])) :
    indexComp.append(comp.index(compSort[0], z, len(comp) + 1))
    z = comp.index(compSort[0], z, len(comp) + 1) + 1
print(indexComp)
# if minC[indexComp[0]] >= minC[indexComp[1]] :
#     indexW = indexComp[0]
# else :
#     indexW = indexComp[1]
# print(indexW)

# print(min(minC[i] * len(indexComp) for i in indexComp))
# a= [minC[i] * len(indexComp) for i in indexComp]
# print(a)
a = []
for i in indexComp :
    # print(minC[i])
    a.append(minC[i])
b = min(a)
print(b)
'''

# a = [10, 10, 40]
# temp = None
# for i in range(len(a)-1) :
#     if a[i] != a[i+1] :
#         print('yes')

# def sol() :
#     print(i)

# for i in range(3) :
#     sol()


def sol(x,y,cost) :
    global visted, minCost
    if len(visted) == n :
        minCost = min(minCost,cost)

    if x >=n or y >= n :
        return
        
    if W[x][y] != 0 and y not in visted :
        visted.append(y)
        sol(x+1,0,cost + W[x][y])
        visted.pop()
    sol(x,y+1,cost)
    


n = int(input())
W = []
for i in range(n) :
    ww = list(map(int,input().split()))
    W.append(ww)

costBox = []
minCost = 10**7
visted = []
box = []
sol(0,0,0)
print(minCost)