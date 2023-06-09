class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for n in range(len(nums)):
            l = n + 1
            r = len(nums) - 1
            if n > 0 and nums[n-1] == nums[n]:
                continue
            while l < r:
                threeSum = nums[n] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[n], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return res