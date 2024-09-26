def fac(n,s=[]):
    if n==1:
        print(s)
        return
    else:
        for i in range(2,n+1):
            if n%i==0:
                s.append(i)
                n=int(n/i)
                break
        return fac(n)
n=int(input())
fac(n)