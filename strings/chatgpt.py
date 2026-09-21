# Longest Substring Without Repeating Characters
s = "pwwkew"
left=0
max_len=0
for i in range(len(s)):
    sw=s[left:i+1]
    while len(sw)!=len(set(sw)):
        left+=1
        sw=s[left:i+1]
    if len(sw)>max_len:
        max_len=len(sw)
print(max_len)
