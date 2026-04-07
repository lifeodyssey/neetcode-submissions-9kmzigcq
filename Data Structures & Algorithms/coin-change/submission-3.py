class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf=amount+1
        dp=[inf]*(amount+1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], dp[x - c] + 1)

        return -1 if dp[amount] == inf else dp[amount]