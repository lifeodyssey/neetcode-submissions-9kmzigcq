class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxLength=1
        l=len(nums)
        if l==0:
            return 0
        for i in range(l):
            currentLength=1
            nextVal=nums[i]+1
            for j in range(i+1,l):
                if nums[j]==nums[j-1]:
                    continue
                if nums[j]==nextVal:
                    currentLength+=1
                    nextVal+=1
                else:
                    break
            maxLength=max(maxLength,currentLength)
        return maxLength