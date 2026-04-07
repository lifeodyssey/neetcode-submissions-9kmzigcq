class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        visited=set()
        def dfs(cur:int,prev:int)->bool:
            if cur in visited:
                return False
            visited.add(cur)
            for nei in g[cur]:
                if nei==prev:
                    continue
                if dfs(nei,cur)==False:
                    return False
            return True
        
        if dfs(0,-1)==False:
            return False
        return len(visited)==n