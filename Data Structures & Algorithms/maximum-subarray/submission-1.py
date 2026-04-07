class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestEnd=nums[0]
        ans=nums[0]

        for x in nums[1:]:
            bestEnd=max(x,bestEnd+x)
            ans=max(ans,bestEnd)
        return ans
            