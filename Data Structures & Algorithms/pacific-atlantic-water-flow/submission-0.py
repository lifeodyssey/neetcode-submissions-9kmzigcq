class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        pac=set()
        atl=set()

        def dfs(r,c,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))

            for dr,dc in dirs:
                 nr,nc=r+dr,c+dc
                 if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                 if heights[nr][nc]<heights[r][c]:
                    continue
                 dfs(nr,nc,visited)
        
        for c in range(cols):
            dfs(0,c,pac)
        for r in range(rows):
            dfs(r,0,pac)
        
        for c in range(cols):
            dfs(rows-1,c,atl)
        for r in range(rows):
            dfs(r,cols-1,atl)
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
