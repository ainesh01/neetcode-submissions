class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l = 0
        out = 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) +1
            
            if (r-l+1) - max(charCount.values())  > k:
                charCount[s[l]] -=1
                l +=1

            out = max(out, r - l +1)
        return out
              