class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {} # val : count
        for i, n in enumerate(nums):
            if n in map:
                map[n] += 1
                return True
            else:
                map[n] = 1
        return False