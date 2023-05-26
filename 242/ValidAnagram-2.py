class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sMap, tMap = {}, {}

        for i, letter in enumerate(s):
            if letter in sMap:
                sMap[letter] += 1
            else:
                sMap[letter] = 1

        for i, letter in enumerate(t):
            if letter in tMap:
                tMap[letter] += 1
            else:
                tMap[letter] = 1

        return sMap == tMap