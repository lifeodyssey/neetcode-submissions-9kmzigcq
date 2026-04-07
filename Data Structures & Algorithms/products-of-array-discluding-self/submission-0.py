class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[1]*n
        leftProd=1
        for i in range(n):
            ans[i]=leftProd
            leftProd*=nums[i]
        rightProd=1
        for i in range(n-1,-1,-1):
            ans[i]*=rightProd
            rightProd *= nums[i]  
        return ans