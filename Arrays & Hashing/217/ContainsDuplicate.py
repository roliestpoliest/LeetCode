class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {} # num : val
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
            if freq[n] > 1:
                return True
        return False