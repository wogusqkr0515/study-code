##  회의실 배정

n = int(input())
time = []
timeIndex = []

for i in range(n) :
    # start, end = map(int,input().split())
    # time[i].append(start)
    # time[i].append(end)
    a = list(map(int,input().split()))
    time.append(a)
time.sort()
box = 0
for i in range(n) :
    if time[i][1] <= time[box][1] :
        box = i
    if time[i][0] >= time[box][1] and not(box in timeIndex):
        timeIndex.append(box)
        box = i
if not(box in timeIndex) :
    timeIndex.append(box)

# print(time)
# print(timeIndex)
print(len(timeIndex))