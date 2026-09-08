s = "anagram"
t = "nagaram"
if len(s)!=len(t):
    print("false")
dict1={}
dict2={}
for ch in s:
    if ch in dict1:
        dict1[ch]+=1
    else:
        dict1[ch]=1
for i in t:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
if dict1==dict2:
    print("true")
else:
    print("False")

#optimal solution 

# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False

#     freq = [0] * 26

#     for ch in s:
#         freq[ord(ch) - ord('a')] += 1

#     for ch in t:
#         freq[ord(ch) - ord('a')] -= 1

#     for count in freq:
#         if count != 0:
#             return False

#     return True