##  최소공배수  ##

t = int(input())  # 유클리드 호제법 
num = [[]*t for i in range(t)]  

for i in range(t) :
    num[i] = list(map(int,input().split()))

minNum = []
for i in range(t) :
    c = 0
    minNum.append(1)
    if num[i][0] >= num[i][1] :
        c=num[i][1]
    else :
        c=num[i][0]
    for k in range(1,c+1) :
        if num[i][0]%k == 0 and num[i][1]%k == 0 :
            minNum[i] = k
for i in range(t) :
    print(num[i][0]*num[i][1]//minNum[i])



