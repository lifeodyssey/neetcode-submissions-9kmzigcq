class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        memo={}
        def dfs(r,c):
            if r>=rows or c>=cols:
                return 0
            if obstacleGrid[r][c]==1:
                return 0
            if r==rows-1 and c==cols-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)]=dfs(r+1,c)+dfs(r,c+1)
            return memo[(r,c)]
        return dfs(0,0)