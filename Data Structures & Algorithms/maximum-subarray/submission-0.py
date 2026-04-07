class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        maxSum=nums[0]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                maxSum=max(maxSum,s)
        return maxSum
            