class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = j = 0

        maxLen = 0



        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                maxLen = max(maxLen, j-i)
            else:
                seen.remove(s[i])
                i += 1
        
        return maxLen




        