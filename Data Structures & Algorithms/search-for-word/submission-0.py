class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        L=len(word)
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c,k):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            if board[r][c]!=word[k]:
                return False
            if k==L-1:
                return True

            temp=board[r][c]
            board[r][c]="#"
            for dr,dc in dirs:
                if dfs(r+dr,c+dc,k+1):
                    board[r][c]=temp
                    return True
            board[r][c]=temp
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True 
        return False