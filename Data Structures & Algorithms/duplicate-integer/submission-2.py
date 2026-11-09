class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not (nums == list(set(nums)))
        