n=int(input())
a=list(map(int, input().split()))
M=float('-inf')
for i in a:
    if i>M:
        M=i
print(M)