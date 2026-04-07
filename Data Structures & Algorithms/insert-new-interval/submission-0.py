class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        result=[]
        for start, end in sortedIntervals:
            if not result:
                result.append([start,end])
            else:
                prevStart,prevEnd=result[-1]
                if start<=prevEnd:
                    result[-1][1]=max(prevEnd,end)
                else:
                    result.append([start,end])
        return result