class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        bestL,bestR=0,0
        def expand(l:int,r:int):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1
        for c in range(n):
            l1,r1=expand(c,c)
            if r1-l1>bestR-bestL:
                bestL,bestR=l1,r1
            l2,r2=expand(c,c+1)
            if r2-l2>bestR-bestL:
                bestL,bestR=l2,r2
        return s[bestL:bestR+1]