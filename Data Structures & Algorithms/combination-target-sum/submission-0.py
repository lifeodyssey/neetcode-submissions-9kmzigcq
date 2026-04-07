class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        path=[]
        def backtrack(start:int,remain:int)->None:
            if remain==0:
                result.append(path.copy())
                return
            if remain<0:
                return
            
            for i in range (start,len(nums)):
                num=nums[i]
                if num>remain:
                    break
                path.append(num)
                backtrack(i,remain-num)
                path.pop()
        backtrack(0,target)
        return result
        