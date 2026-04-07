class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf=amount+1
        memo={}
        def dfs(rem:int)->int:
            if rem==0:
                return 0
            if rem<0:
                return inf
            if rem in memo:
                return memo[rem]
            best=inf
            for c in coins:
                best=min(best,1+dfs(rem-c))
            memo[rem]=best
            return best
        ans=dfs(amount)
        return -1 if ans==inf else ans