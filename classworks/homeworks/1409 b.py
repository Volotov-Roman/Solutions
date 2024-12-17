n=int(input())
a=list(map(int, input().split()))
m=[float('inf'), float('inf')]
for i in range(n):
    if i==0:
        m[0]=a[i]
    else:
        if a[i]<m[0] or a[i]<m[1]:
            if m[0]<m[1]:
                m[1]=a[i]
            else:
                m[0]=a[i]
m.sort()
print(*m)