class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        for i in range(1, l):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        for i in range(l-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res