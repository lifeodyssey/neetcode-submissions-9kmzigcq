class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        best=0
        def dfs(i,last_val,length):
            nonlocal best
            if i==n:
                best=max(best,length)
                return
            dfs(i+1,last_val,length)
            if nums[i]>last_val:
                dfs(i+1,nums[i],length+1)
        dfs(0,float('-inf'),0)
        return best