##  골드바흐의 추측  ##

num = []
while True :
    if 0 in num :
        break
    n = int(input())
    num.append(n)
lenNum = len(num) - 1
plus = [[]*lenNum for i in range(lenNum)]

for i in range(lenNum) :
    x,k, yesNo = 0,3, False
    while True :
        x = num[i] - k
        for z in range(2,x+1) :
            if z == x :
                yesNo = True
            elif x % z == 0 :
                break
        if yesNo == True :
            break
        k += 2
    plus[i].append(k)
    plus[i].append(x)

for i in range(lenNum) :
    print(num[i], end=' = ')
    print(plus[i][0],end=' + ')
    print(plus[i][1])

## 시간 초과 소수 판별시 에라토스테네스의 체 사용 ##