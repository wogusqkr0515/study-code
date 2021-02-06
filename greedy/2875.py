##  대회 or 인턴 

n,m,k = map(int,input().split())

team = (n+m-k) // 3
while team > 0 :
    if n >= 2*team and m >= team and (n+m)-(team+k) >= 0 :
        break
    else : 
        team -= 1
print(team)