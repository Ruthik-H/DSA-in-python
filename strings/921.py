# Minimum Add to Make Parentheses Valid
s = "((((()"
open=0
add=0
for i in s:
    if i=="(":
        open+=1
    else:
        if open>0:
            open-=1
        else:
            add+=1
print(open+add)