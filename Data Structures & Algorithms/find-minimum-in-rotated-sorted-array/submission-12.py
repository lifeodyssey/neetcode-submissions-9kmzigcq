class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        while(left<n-1):
            if nums[left+1]>nums[left]:
                left+=1
            else:
                return nums[left+1]
                
        if left==n-1:
            return nums[0]