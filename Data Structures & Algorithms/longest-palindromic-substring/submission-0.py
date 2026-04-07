class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        bestL,bestR=0,0
        for i in range(n):
            for j in range(i,n):
                if j-i>bestR-bestL and self.isPal(s,i,j):
                    bestL,bestR=i,j
        return s[bestL:bestR+1]
    def isPal(self,s:str,l:int,r:int)->bool:
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True