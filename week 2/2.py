s=input().split()
n=int(s[0])
str0=str(s[1])
str1=[]
str2=[]
for i in range(len(str0)):
    str1.append(str0[i])
for j in range(int(len(str1)/n)):
    for k in range(-1,-n-1,-1):
        str2.append(str1[j*n+n+k])
print(''.join(str2))