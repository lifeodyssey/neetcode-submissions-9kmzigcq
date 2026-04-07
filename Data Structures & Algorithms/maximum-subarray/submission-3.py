class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        cur_sum=0

        for x in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=x
            ans=max(ans,cur_sum)
        return ans
            