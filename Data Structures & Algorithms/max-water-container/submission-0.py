class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxArea=0
        right=n-1
        for left in range(n):
            right=n-1
            while left<right:
                currentArea=(right-left)*min(heights[left],heights[right])
                maxArea=max(maxArea,currentArea)
                right-=1
        
        return maxArea