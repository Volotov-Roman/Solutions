n=int(input())
a=list(map(int, input().split()))
m=float('inf')
ans=[]
ind=-1
for i in range(n):
    if a[i]<m:
        m=a[i]
        ind=i
ans.append(m)
a.pop(ind)

m=float('inf')
ind=-1
for i in range(n-1):
    if a[i]<m:
        m=a[i]
        ind=i
ans.append(m)

print(*ans)