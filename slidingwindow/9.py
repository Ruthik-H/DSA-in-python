x=-121  
c=str(x)
a=0
b=len(c)-1
while a<b:
    if c[a]!=c[b]:
        print("True")
    a+=1
    b-=1
    print("False")
