from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        indexed_nums.sort(key=lambda x: x[1])
        
        leftIndex = 0
        rightIndex = len(indexed_nums) - 1
        
        while leftIndex < rightIndex:
            currentSum = indexed_nums[leftIndex][1] + indexed_nums[rightIndex][1]
            if currentSum == target:
                index=[indexed_nums[leftIndex][0] , indexed_nums[rightIndex][0] ]
                index.sort()
                return index
            elif currentSum < target:
                leftIndex += 1
            else:
                rightIndex -= 1
        
