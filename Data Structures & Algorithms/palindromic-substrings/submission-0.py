class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 1
        count=0
        for i in range(n):
            for j in range(i,n):
                if self.isPal(s,i,j):
                    count+=1
        return count
    def isPal(self,s:str,l:int,r:int)->bool:
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True