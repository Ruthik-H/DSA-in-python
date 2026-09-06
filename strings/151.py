# reverse the string
# two pointers
s = "the sky is blue"
a=s.split()
z=len(a)-1
b=0
while b<z:
    a[z],a[b]=a[b],a[z]
    z-=1
    b+=1
print(" ".join(a))
