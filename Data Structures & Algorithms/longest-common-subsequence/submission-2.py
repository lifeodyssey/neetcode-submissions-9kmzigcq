class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}

        def dfs(i, j):
            if i == m or j == n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                ans = 1 + dfs(i + 1, j + 1)
            else:
                ans = max(dfs(i + 1, j), dfs(i, j + 1))

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)