def dd() :
    if 1 == n :
        print(1)
    elif 2 == n :
        print(2)
    else :
        print(3)


n = 2
dd()


''' 
혼자 생각 하고 시도한 코드  
각 줄에서 젤 작은거랑 두번째로 작은거 합이 큰 순으로 순서를 정해서 하나씩 지정하면서 제거
n = int(input())
W = []
for i in range(n) :
    ww = list(map(int,input().split()))
    W.append(ww)
comp = []
for i in range(n) :
    box = sorted(W[i])
    for k in range(1,n) :
        if box[k] != 0 :
            if k == n - 1 :
                comp.append(1000000)
            else :
                comp.append(box[k+1] - box[k])
                break

compSort = sorted(comp, reverse = True)
num, sumCost = [], 0
for k in range(n) :
    # if not(comp.count(compSort[0]) >= 2) :
    if len(num) == n -2 :
        sumCost += W[comp.index(compSort[0])][comp.index(compSort[1])]
        num.append(comp.index(compSort[1])) 
        for i in range(n) :
            if not(i in num) :
                sumCost +=  W[comp.index(compSort[1])][i]
        break
    else :
        z = 0
        while z in num :
            z += 1
        minCost = W[comp.index(compSort[0])][z]
        while minCost == 0 :
            z += 1
            minCostIndex = z
            minCost = W[comp.index(compSort[0])][z]
        minCostIndex = z
        for i in range(z+1, n) :
            if not(i in num) :
                if W[comp.index(compSort[0])][i] > 0 and W[comp.index(compSort[0])][i] <= minCost :
                    minCostIndex = i
                    minCost = W[comp.index(compSort[0])][i]
        num.append(minCostIndex)
        sumCost += minCost
        del(compSort[0])


# print(W)
# print(comp)
# print(compSort)

# print(num)
print(sumCost)
'''