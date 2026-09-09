# Maximum Nesting Depth of the Parentheses
s = "(1+(2*3)+((8)/4))+1"
count=0
max_count=0
for i in s:
    if i=="(":
        count+=1
    if i==")":
        count-=1
    if count>max_count:
        max_count=count





