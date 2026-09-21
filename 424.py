s = "AABABBA"
k = 1
left=0
freq={}
for i in range(len(s)):
    if s[i] in freq:
        freq[s[i]]+=1
    else:
        freq[s[i]]=1

print(freq)