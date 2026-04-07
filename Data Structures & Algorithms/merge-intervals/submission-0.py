class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        result=[]
        for start,end in intervals:
            if not result:
                result.append([start,end])
            else:
                prevStart,prevEnd=result[-1]

                if prevEnd>=start:
                    result[-1][1]=max(prevEnd,end)
                else:
                    result.append([start,end])
        return result