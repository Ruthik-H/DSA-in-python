s = "aabcb"
add=[]
for i in range(len(s)):
    for j in range(i, len(s)):
        substring=s[i:j+1]
        dict1={}
        for ch in substring:
            if ch not in dict1:
                dict1[ch]=1
            else:
                dict1[ch]+=1
        
        add.append(max(dict1.values())-min(dict1.values()))
print(sum(add))

