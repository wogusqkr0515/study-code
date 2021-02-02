##  소수 찾기  ##

n = int(input())
num = list(map(int, input().split()))
count = 0

for i in range(n) :
    if num[i] != 1 :
        for k in range(2,num[i] + 1) :
            if k == num[i] :
                count += 1
            elif num[i] % k == 0 :
                break

print(count)