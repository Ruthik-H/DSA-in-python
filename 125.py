# palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=[]
        for i in s:
            if i.isalnum():
                new.append(i)

        #two pointer 
        i=0
        j=len(new)-1
        while i<j:
            if new[i]==new[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        