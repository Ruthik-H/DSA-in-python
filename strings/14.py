# longest common prefix
strs = ["flower","flow","flight"]
for j in range(min(len(word) for word in strs)):# j → tells us WHICH POSITION to examine like using the word flower we get len as 6 so range(6)
    for i in range(len(strs)):#  i → tells us WHICH WORD to examine
        if strs[i][j]!=strs[0][j]:
            print(strs[0][:j])

#min(len(word) for word in strs)) this is becuase see we havto pick the smallest number to iterate with the positions so 
# if we take the longest  one it will cause an index error so always pick the smaller one 

# The actual code 
# def longestCommonPrefix(self, strs: List[str]) -> str:

#     min_len = min(len(word) for word in strs)

#     for j in range(min_len):

#         for i in range(len(strs)):

#             if strs[i][j] != strs[0][j]:
#                 return strs[0][:j]

#     return strs[0][:min_len]