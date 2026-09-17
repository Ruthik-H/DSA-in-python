#Repeated String Match
a = "abcd"
b = "cdabcdab"
count=0
for i in range(len(b)-len(a)+1):
    if b[i:i+len(a)]==a:
        print(count)
    else:
        a+=a
        count+=1
    