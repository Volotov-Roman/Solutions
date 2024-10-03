a=input()
if a==a[::-1]:
    if len(a)%2==1:
        if a[len(a)//2] in ["A","H","I","M","O","T","U","V","W","X","Y","1","8"]:
            print(a+" is a mirrored palindrome")
        else:
            print(a+" is a regular palindrome")
    else:
        print(a + " is a regular palindrome")
elif a.replace("3","E").replace("L","J").replace("2","S").replace("5","Z")==a[::-1].replace("3","E").replace("L","J").replace("2","S").replace("5","Z"):
    print(a+" is a mirrored string")
else:
    print(a+" is not a palindrome")