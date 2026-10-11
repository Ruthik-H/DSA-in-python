n = 4
a=[1]
while len(a)<=n:
    temp=[]
    for x in a:
        if 2*x-1<=n:
            temp.append(2*x-1)
    for x in a:
        if 2*x<=n:
            temp.append(2*x)
    a=temp
print(a)
