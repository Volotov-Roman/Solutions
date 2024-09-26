s=input().split()
a=int(s[0])
b=int(s[1])

t=[i for i in range(1,min(a,b)+1) if (a%i==0 and b%i==0)]
d=max(t)                                                          #наиб. общ. делитель

w=[]
ans0=[]
index=[]

for i in range(a*b):
    for j in range(a * b):
        w.append([i,j])               #матрица с потенциальными значениями x,y

for k in w:
    if k[0]*a+k[1]*b==d:
        ans0.append(k)
    elif -k[0]*a+k[1]*b==d:
        ans0.append([-k[0],k[1]])
    elif k[0] * a - k[1] * b == d:
        ans0.append([k[0], -k[1]])
    elif -k[0] * a - k[1] * b == d:
        ans0.append([-k[0], -k[1]])        #список из пар (x,y), удовл. условию задачи

z=[]
for an in ans0:
    z.append(abs(an[0])+abs(an[1]))
k=min(z)
for r in range(len(z)):
    if k==z[r]:
        index.append(r)              #выделяем из прошлого списка номера пар с минимальной суммой модулей

y=[]
for an1 in index:
    y.append(ans0[an1][0])                 #список со значениями x, ищем пару с мин. x
k=min(y)
for l in y:
    if k==l:
        dig=index[l]
        print(ans0[dig][0], ans0[dig][1], d)
        break
