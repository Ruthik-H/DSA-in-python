s1 = "abc", s2 = "abb", s3 = "ab"
dict1={}
dict2={}
count=0
for i in range(len(s1)):
    if s1[i] in dict1:
        dict1[i]+=1
    else:
        dict1=1
for j in range(len(s2)):
    if s2[j] in dict2:
        dict2[j]+=1
    else:
        dict2=1
if dict1==dict2:
    print()
