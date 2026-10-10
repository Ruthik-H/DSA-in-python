l1=['A','B','c']
l2=['1','2','3']
dict1={}
j=0
for i in range(len(l1)):
    dict1[l1[i]]=l2[j]
    j+=1
print(dict1)