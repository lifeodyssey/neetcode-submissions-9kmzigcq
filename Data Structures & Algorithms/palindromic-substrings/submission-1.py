class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 1
        count=0
        def expand(l:int,r:int)->int:
            cnt=0
            while(l>=0 and r<n and s[l]==s[r]):
                cnt+=1
                l=l-1
                r=r+1
            return cnt
        for c in range(n):
            count+=expand(c,c)
            count+=expand(c,c+1)
        return count