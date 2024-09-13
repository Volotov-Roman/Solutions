N=input()
b=int(input())
c=int(input())
d=0
e=''
for i in range(len(N)):
    d=d+(int(N[-1-i]))*(b**i)
while d>=c:
    e=e+str(d%c)
    d=d//c
e=e+str(d)
print(e[::-1])