def tri(n,a,depth=1):
    if n%2!=0 and depth==n//2+1:
        print(a*depth)
        return
    if n%2==0 and depth==h//2:
        print(a*depth)
        print(a*depth)
        return
    print(a*depth)
    tri(n,a,depth=depth+1)
    print(a * depth)
t=input().split()
n=int(t[0])
a=t[1]
tri(n,a)