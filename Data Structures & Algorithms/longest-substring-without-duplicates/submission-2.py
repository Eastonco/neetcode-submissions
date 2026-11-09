class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0
        res = total
        seen = set()
        for c in s:
            if c not in seen:
                seen.add(c)
                total += 1
            else: 
                res = max(total, res)
                total = 0
                seen.clear()
            lastSeen = c  
        return max(total, res)

        