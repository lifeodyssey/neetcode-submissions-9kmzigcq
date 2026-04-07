class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        visited=set()

        def dfs(cur):
            visited.add(cur)
            for nei in g[cur]:
                if nei in visited:
                    continue
                dfs(nei)
        count=0
        for node in range(n):
            if node in visited:
                continue
            count+=1
            dfs(node)
        return count