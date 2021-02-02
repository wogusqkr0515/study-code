##  최대공약수와 최소공배수  ##

a,b = map(int,input().split())

maxNum,minNum,c = 0, 1,0

if a >= b :
    c=b
else :
    c=a
for i in range(1,c+1) :
    if a%i == 0 and b%i == 0 :
        minNum = i
print(minNum)
print(a*b//minNum)