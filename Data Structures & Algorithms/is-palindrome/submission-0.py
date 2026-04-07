class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        i=0
        s="".join(c.lower() for c in s if c.isalnum())
        n=len(s)

        while i<n/2:
            j=n-i-1
            if s[i]!=s[j]:
                return False
            i=i+1
        return True