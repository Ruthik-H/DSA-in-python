s = "ADOBECODEBANC"
t = "ABC"
a=0
b={}
min_len=float('inf')
min_window=""
for i in range(len(t)):
    if t[i] in b:
        b[t[i]]+=1
    else:
        b[t[i]]=1
for i in range(len(s)):
    w_s=s[a:i+1]
    c={}
    for j in range(len(w_s)):
        if w_s[j] in c:
            c[w_s[j]]+=1
        else:
            c[w_s[j]]=1
    valid=True
    for ch in b:
        if ch not in c or c[ch]<b[ch]:
            valid=False
            break
    if valid:
        if len(w_s)<min_len:
            min_len=len(w_s)
            min_window=w_s
    else:
        a+=1
print(min_window)
