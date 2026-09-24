class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a=0
        b={}
        for ch in t:
            if ch in b:
                b[ch]+=1
            else:
                b[ch]=1
        c={}
        formed=0
        required=len(b)
        min_len=float('inf')
        min_window=""
        for j in range(len(s)):
            ch=s[j]
            if ch in c:
                c[ch]+=1
            else:
                c[ch]=1
            if ch in b and c[ch]==b[ch]:
                formed+=1
            while formed==required:
                if j-a+1<min_len:
                    min_len=j-a+1
                    min_window=s[a:j+1]
                left_char=s[a]
                c[left_char]-=1
                if left_char in b and c[left_char]<b[left_char]:
                    formed-=1
                a+=1
        return min_window