class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(s[i:j]) == len(set(s[i:j])):
                    maxLen = max(len(s[i:j]),maxLen)
                else:
                    break
        return maxLen