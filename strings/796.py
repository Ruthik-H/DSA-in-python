# Rotate strings 
# this iam doing using sliding window
s = "abcde"
goal = "cdeab"
if len(s)!=len(goal):
    print("false")
# a=s+s
# for i in range(len(s)):
#     w_s=a[i:i+len(s)]
#     if w_s==goal:
#         found=True
#         break
# if found:
#     print("True")
# else:
#     print("False")

#for optimal solution just easy way 
if goal in s+s:
    print("True")
else:
    print("False")