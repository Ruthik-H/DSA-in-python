digits = [4,3,2,1]
num=0
a=[]
for i in range(len(digits)):
    num=num*10+digits[i]
num+=1
for j in str(num):
    a.append(int(j))
print(a)