n=int(input())
a=list(map(int, input().split()))
b=[0 for i in range(n)]
b[0]=a[-1]
for i in range(1,n):
    b[i]=a[i-1]
print(*b)