class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if j-i == len(set(s[i:j])):
                    maxLen = max(j-i,maxLen)
                else:
                    break
        return maxLen