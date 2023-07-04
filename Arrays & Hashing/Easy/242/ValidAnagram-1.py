class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # map : {character : frequency}
        sMap = {}
        tMap = {}

        for c in range(len(s)):
            sMap[s[c]] = 1 + sMap.get(s[c], 0)
            tMap[t[c]] = 1 + tMap.get(t[c], 0)

        return sMap == tMap

        