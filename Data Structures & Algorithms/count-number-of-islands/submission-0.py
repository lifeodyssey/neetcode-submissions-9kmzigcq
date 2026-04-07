class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c]!='1':
                return
            grid[r][c]='0'

            for dr,dc in dirs:
                dfs(r+dr,c+dc)
        
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1': 
                    dfs(r,c)                   
                    count+=1
        return count