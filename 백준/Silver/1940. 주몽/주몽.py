n = int(input())
m = int(input())
data = list(map(int,input().split()))
data = sorted(data)
s= 0
e= n-1
count = 0

while s < e:
    result = data[s] + data[e]
    if result < m:
        s+=1
    elif result >m:
        e -=1
    else:
        count +=1
        s+=1
        e-=1
print(count)