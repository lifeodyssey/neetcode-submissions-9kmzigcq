class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for c in range(9):
            row=board[c][:]
            col=[board[r][c] for r in range(len(board))] 
            if self.isContainDuplicate(row) or self.isContainDuplicate(col):
                return False
        for box_r in range(3):
            for box_c in range(3):
                start_r = box_r * 3
                start_c = box_c * 3

                subbox = []
                for r in range(start_r, start_r + 3):
                    for c in range(start_c, start_c + 3):
                        subbox.append(board[r][c])

                if self.isContainDuplicate(subbox):
                    return False
        return True
    def isContainDuplicate(self,strs:List[str])->bool:
        strDict=defaultdict(int)
        for s in strs:
            if s=='.':
                continue
            
            strDict[s]+=1
            if strDict[s]>1:
                return True
        return False