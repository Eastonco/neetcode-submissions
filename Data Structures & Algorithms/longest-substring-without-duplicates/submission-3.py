class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        seen = set()
        for c in s:
            if c not in seen:
                seen.add(c)
            else: 
                maxLen = max(len(seen), maxLen)
                seen.clear()
        return max(len(seen), maxLen)

        