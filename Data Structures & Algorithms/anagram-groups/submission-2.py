class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myset = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in myset:
                myset[key].append(item)
            else:
                myset[key] = [item]
        return list(myset.values())
