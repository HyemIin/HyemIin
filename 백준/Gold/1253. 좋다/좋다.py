n = int(input())
data = list(map(int,input().split()))
count = 0
data = sorted(data)

# 투 포인터로 탐색
for i in range(n):
    target = data[i]
    s = 0
    e = n-1
    if s == i:
        s+=1
    if e == i:
        e -=1
    while s <e:
        if data[s]+data[e] <target:
            s +=1
            if s == i:
                s +=1
        elif data[s]+data[e] > target:
            e -=1
            if e == i:
                e -=1
        else:
            count +=1
            break
print(count)