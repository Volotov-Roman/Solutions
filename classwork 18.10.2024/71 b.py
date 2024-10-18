n=int(input())
a=list(map(int, input().split()))
a.insert(0,a[-1])
a.append(0)
for i in range(1,n):
    a[-i]=a[-(i+2)]
a.pop(1)
a.pop(1)
print(*a)
