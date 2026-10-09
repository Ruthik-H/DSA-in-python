s = ")()())"
count=0
for i in range(len(s)):
    if s[i]=='(':
        count+=1
    elif s[i]==')':
        count-=1
print(abs(count)*2)