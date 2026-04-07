class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=set(nums)
        if len(count)<len(nums):
            return True
        else:
            return False