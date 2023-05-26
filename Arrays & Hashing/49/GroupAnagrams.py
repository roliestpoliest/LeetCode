# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s in groups:
                groups[s].append(strs[i])
            else:
                groups[s] = [strs[i]]

        return(groups.values())