class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = dict()
        tCount = dict()
        for c in s:
            if c in sCount:
                sCount[c] +=1
            else:
                sCount[c] = 1
        for c in t:
            if c in tCount:
                tCount[c] +=1
            else:
                tCount[c] = 1

        if sCount == tCount:
            return True
        else:
            return False