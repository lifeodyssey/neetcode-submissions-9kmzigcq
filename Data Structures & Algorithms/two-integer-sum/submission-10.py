class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i, x in enumerate(nums):
            need=target-x
            if need in index:
                return[index[need],i]
            index[x]=i