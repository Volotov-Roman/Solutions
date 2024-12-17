n=int(input())
d=[]
m={}
for i in range(n):
    d.append(input())
k = int(input())
for d0 in d:
    if d0 in m:
        m[f'{d0}']+=1
    else:
        m[f'{d0}']=1
a=[[key, m[key]] for key in m.keys()]
a.sort(key=lambda z:z[1])
for i in range(k):
    print(a[-1-i][0])