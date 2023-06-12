class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1, len(s)):
                if(s[j] not in temp):
                    temp += s[j]
                else:
                    break
            longest = max(longest, len(temp))
        return longest