class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {} # value : index
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in previous:
                return [previous[difference], i]
            previous[n] = i
        return
