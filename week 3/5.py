s=input().split()
n=int(s[0])
m=int(s[1])
w=[]

for i in range(n):
    o = [0 for j in range(m)]
    w.append(o)

x=0
y=0
a=0
b=1
w[0][0]=1
c=2

while c<=n*m:
    if 0<=x+a<=n-1 and 0<=y+b<=m-1 and w[x+a][y+b]==0:
        w[x+a][y+b]=c
        c+=1
        x+=a
        y+=b
    else:
        if b==1:
            b=0
            a=1
        elif a==1:
            a=0
            b=-1
        elif b==-1:
            b=0
            a=-1
        elif a==-1:
            a=0
            b=1
print(w)
for k in range(n):
    for l in range(m):
        w[k][l]*=k
print(w)