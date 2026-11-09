class Solution:

    def encode(self, strs: List[str]) -> str:
        payload = ''
        for item in strs:
            payload += str(len(item)) + '#' + item
        return payload

    def decode(self, s: str) -> List[str]:
        length = 0
        i = 0
        results = []
        while i != len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            tmp = s[j+1:j+1+length]
            results.append(tmp)
            i = j + 1 + length
        return results
            

        