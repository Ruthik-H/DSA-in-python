height = [8,7,2,1]
a=0
b=len(height)-1
max_cap=0
while a<=b:
    c=b-a
    d=min(height[a],height[b])*c
    if height[a]<height[b]:
        a+=1
    else:
        b-=1
    if d>max_cap:
        max_cap=d
print(max_cap)


