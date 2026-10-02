# s="([)]"
# count1=0
# count2=0
# count3=0
# for i in range(len(s)):
#    if s[i]=='(':
#       count1+=1
#    elif s[i]=='[':
#       count2+=1
#    elif s[i]=='{':
#       count3+=1
#    elif s[i]==')':
#       count1-=1
#    elif s[i]==']':
#       count2-=1
#    elif s[i]=='}':
#       count3-=1

# if count1==0 and  count2==0 and count3==0:
#    print(True)
# else:
#    print(False)


    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif ch == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif ch == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
        return len(stack) == 0