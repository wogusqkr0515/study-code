## 30

n = input()
lenN = len(n)
sumNum = 0
num = []

for i in range(lenN) :
    sumNum += int(n[i])
    num.append(n[i])

if sumNum % 3 == 0 and '0' in num:
    num.sort(reverse = True)
    for i in range(lenN) :
        print(num[i],end='')
else :
    print(-1)

