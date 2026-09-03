s = "egg"
t = "add"
mapping={}
reverse_mapping={}
for i ,ch in enumerate(s):
    if ch in mapping:
        if mapping[ch]!=t[i]:
            print("not isomorphic")
            break
    else:
        if t[i] in reverse_mapping:
            print("Not isomorphic")
            break
        mapping[ch]=t[i]
        reverse_mapping[t[i]]=ch

else:
    print("isomorphic")
    


