class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in nums:
            # start of a sequence
            if (n-1) not in numsSet:
                length = 0
                temp = n
                while (temp) in numsSet:
                    length += 1
                    temp += 1
                if length > longest:
                    longest  = length
        return longest