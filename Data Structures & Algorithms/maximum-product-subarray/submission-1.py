class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        max_end=nums[0]
        min_end=nums[0]
        for x in nums[1:]:
            prev_max,prev_min=max_end,min_end
            
            max_end = max(x, x * prev_max, x * prev_min)
            min_end = min(x, x * prev_max, x * prev_min)

            ans = max(ans, max_end)

        return ans