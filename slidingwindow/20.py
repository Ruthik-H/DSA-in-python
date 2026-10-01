s="([)]"
count1=0
count2=0
count3=0
for i in range(len(s)):
   if s[i]=='(':
      count1+=1
   elif s[i]=='[':
      count2+=1
   elif s[i]=='{':
      count3+=1
   elif s[i]==')':
      count1-=1
   elif s[i]==']':
      count2-=1
   elif s[i]=='}':
      count3-=1

if count1==0 and  count2==0 and count3==0:
   print(True)
else:
   print(False)


    
   