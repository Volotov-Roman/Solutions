a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a==c or b==d or b+a==d+c or abs(b-a)==abs(d-c):
    print("YES")
else:
    print("NO")