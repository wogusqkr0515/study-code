## 동전0

n,k = map(int,input().split())
cost = []
for i in range(n) :
    cost.append(int(input()))
count = 0

for i in range(n-1, -1, -1) :
    count += k // cost[i]
    k %= cost[i]
print(count)