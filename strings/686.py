class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count=1
        original=a
        while b not in a:
            a+=original
            count+=1
            if count > len(b) // len(original) + 2:
                return -1
        return count
        