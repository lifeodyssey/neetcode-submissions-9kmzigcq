class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        dp=[[False]*n for _ in range(n)]
        bestL,bestR=0,0
        for length in range(1,n+1):
            for i in range(0,n-length+1):
                j=i+length-1

                if s[i]==s[j]:
                    if length<=3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]

                if dp[i][j] and (j-i>bestR-bestL):
                    bestL,bestR=i,j
        return s[bestL:bestR+1]