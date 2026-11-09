class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items = defaultdict(list)
        for item in strs:
            sortedString = ''.join(sorted(item))
            items[sortedString].append(item)
        return [items.values()]


        