class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not (nums == set(nums))
        