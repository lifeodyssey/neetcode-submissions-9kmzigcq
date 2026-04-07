class Solution:
    def rob(self, nums: List[int]) -> int:
        def robLinear(arr):
            prev2=0
            prev1=0
            for x in arr:
                cur=max(prev1,prev2+x)
                prev2,prev1=prev1,cur
            return prev1
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        return max(robLinear(nums[:-1]),robLinear(nums[1:]))