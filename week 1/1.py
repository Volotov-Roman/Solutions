A=list(map(int, input().split()))
s=1
for i in A:
    s=s*i
print(s**(1/len(A)))