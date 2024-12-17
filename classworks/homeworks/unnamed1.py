a=int(input())
b=int(input())
c=int(input())
if a==0:
    if b==0:
        if c==0:
            print("true for all real x")
        else:
            print("NO")
    else:
        print(-c/b)
else:
    if b*b==4*a*c:
        print(-b/2*a)
    if b*b>4*a*c:
        print((-b+((b*b-4*a*c)**(1/2)))/(2*a),(-b-((b*b-4*a*c)**(1/2)))/(2*a))
