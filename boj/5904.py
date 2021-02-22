# moo = "moomooo"

# n = int(input())
# if n%7 == 0 :
#     print('o')
# else :
#     print(moo[n%7-1])

# def moo(k) :
#     moos = 'moo'
#     if k == 0 :
#         return moos
#     else :
#         moos = moo(k-1) + 'm' + 'o'*(k+2) + moo(k-1)
#         return moos
# def solution(num,ii) :
#     answer = 'm' + 'o' * (ii+2)
#     print(answer[num-1])
#     return 
# n = int(input()) 
# mooStr = moo(0)
# i = 0
# while len(mooStr) <= n :
#     i += 1
#     mooStr = moo(i)
# print(mooStr[n-1])


# if n <= len(moo(i)) - len(moo(i-1)) :
#     solution(n - len(moo(i-1)),i)
# else :
#     solution(n-len(moo(i)) + len(moo(i-1)),i-1)



# print(moo(n))



# a='m'
# print(a+'m'+'o'*3)
# print('m'.join('o'*3))
def solution(num,ii) :
    if ii == 0 :
        if num == 1 :
            print('m')
        else :
            print('o')
    elif num <= data[ii] - data[ii-1] :
        num = num - data[ii-1]
        if num == 1 :
            print('m')
        else :
            print('o')
    else :
        num = num + data[ii-1] - data[ii]
        solution(num,ii-1)


n = int(input()) 

i,lenStr = 0,3
data = [3]
while lenStr < n :
    i += 1
    lenStr = 2*lenStr +i+3
    data.append(lenStr)
solution(n,i)
# print(data)
