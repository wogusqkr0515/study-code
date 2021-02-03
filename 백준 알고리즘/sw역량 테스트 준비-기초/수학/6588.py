##  골드바흐의 추측  ##
import math
from math import gcd

num = []
while True :
    n = int(input())
    if n == 0 :
        break
    num.append(n)

lenNum = len(num)
plus = [[]*lenNum for i in range(lenNum)]

# for i in range(lenNum) :
#     x,k, yesNo = 0,3, False
#     while True :
#         x = num[i] - k
#         for z in range(2,x+1) :
#             if z == x :
#                 yesNo = True
#             elif x % z == 0 :
#                 break
#         if yesNo == True :
#             break
#         k += 2
#     plus[i].append(k)
#     plus[i].append(x)

for i in range(lenNum) :              ## 잘못 생각함 
    num1,num2,box,yesNo = 3,0,0,False
    while True :
        box = num[i] - num1
        if gcd(num1,box) == 1 :
            num2 = box
            yesNo = True
        # print('1== ',box)
        # sqr = int(math.sqrt(box))+1
        # print('2 == ',sqr)
        # for k in range(2,sqr) :
        #     if box % k == 0 :
        #         num2 = box
        #         yesNo = True
        #         break
        if yesNo == True :
            plus[i].append(num1)
            plus[i].append(num2)
            break
        else :
            num1 += 2
            if gcd(1,num1) != 1 :
                while gcd(1,num1) != 1 :
                    num1 += 1



for i in range(lenNum) :
    print(num[i], end=' = ')
    print(plus[i][0],end=' + ')
    print(plus[i][1])

## 시간 초과 소수 판별시 에라토스테네스의 체 사용 ##