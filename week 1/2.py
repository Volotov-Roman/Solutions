f=open("input.txt",'r')
g=open("output.txt",'w')
t=f.readline()
t=t.split()
a=int(t[0])
oper=f.readline()
if oper == '+':
    for i in range(len(t)-1):
        a=a+int(t[i+1])
elif oper == '-':
    for i in range(len(t)-1):
        a=a-int(t[i+1])
else:
    for i in range(len(t)-1):
        a=a*int(t[i+1])
g.write(str(a))
f.close()
g.close()