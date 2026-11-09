class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(list(set(nums)))
        total = 1
        maxTotal = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                total += 1
            else:
                maxTotal = max(maxTotal, total)
                total = 1
        return max(maxTotal, total)